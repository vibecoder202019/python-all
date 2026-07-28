"""
Module 05 — Đáp án bài tập
Chạy: python exercises/solutions/solutions.py

YÊU CẦU ĐỀ BÀI:
  - Viết hàm get_github_user: lấy tên và số repo public từ GitHub API
  - Viết hàm parse_apache_log: parse dòng log Apache thành dict
  - Viết decorator @retry: thử lại hàm khi gặp lỗi (tối đa N lần)

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In thông tin user GitHub (ví dụ: tiangolo)
  - parse_apache_log trả về dict với ip, timestamp, method, path, status, size
  - fetch_url tự retry khi request thất bại
"""

import re
import time
import functools
import requests


# ── Bài 1: Lấy thông tin user GitHub ──
def get_github_user(username: str) -> dict:
    """Lấy thông tin user từ GitHub API."""
    response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
    response.raise_for_status()
    data = response.json()
    return {"name": data.get("name"), "public_repos": data["public_repos"]}


# ── Bài 2: Parse log Apache ──
def parse_apache_log(line: str) -> dict | None:
    """Parse một dòng log Apache Common Log Format."""
    # Pattern: IP - - [timestamp] "METHOD path PROTO" status size
    pattern = r'(\S+) - - \[([^\]]+)\] "(\S+) (\S+) (\S+)" (\d+) (\d+)'
    match = re.match(pattern, line)
    if not match:
        return None  # dòng không khớp format
    return {
        "ip": match.group(1),
        "timestamp": match.group(2),
        "method": match.group(3),
        "path": match.group(4),
        "status": int(match.group(6)),
        "size": int(match.group(7)),
    }


# ── Bài 3: Decorator retry ──
def retry(max_attempts: int = 3, delay: float = 1):
    """Decorator — thử lại hàm khi gặp exception."""
    def decorator(func):
        @functools.wraps(func)  # giữ nguyên tên và docstring của hàm gốc
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise  # hết lượt thử → ném lỗi ra ngoài
                    print(f"  Attempt {attempt} failed: {e}. Retry in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.5)
def fetch_url(url: str) -> str:
    """Fetch URL với retry tự động."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.text[:100]


if __name__ == "__main__":
    user = get_github_user("tiangolo")
    print(f"GitHub user: {user}")

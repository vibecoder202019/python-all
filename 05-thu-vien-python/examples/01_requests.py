"""
Module 05 — Ví dụ 1: Thư viện requests (HTTP client)
Chạy: python examples/01_requests.py

YÊU CẦU ĐỀ BÀI:
  - Gửi GET request tới GitHub API và đọc JSON response
  - Gửi POST request với payload JSON tới httpbin.org
  - Xử lý lỗi HTTP (404), ConnectionError, Timeout

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In thông tin repo FastAPI (tên, stars, ngôn ngữ, mô tả)
  - In status code và JSON đã gửi qua POST
  - Bắt và in HTTP Error khi gọi endpoint 404
"""

import requests


# ── Demo GET request ──
def demo_get():
    """Demo GET request — lấy thông tin repo từ GitHub API."""
    print("=== GET: GitHub API ===")
    url = "https://api.github.com/repos/tiangolo/fastapi"
    response = requests.get(url, timeout=10)  # timeout tránh treo vô hạn
    response.raise_for_status()  # ném exception nếu status >= 400
    data = response.json()
    print(f"  Repo: {data['full_name']}")
    print(f"  Stars: {data['stargazers_count']:,}")
    print(f"  Language: {data['language']}")
    print(f"  Description: {data['description'][:80]}...")


# ── Demo POST request ──
def demo_post():
    """Demo POST request — gửi JSON payload."""
    print("\n=== POST: httpbin.org ===")
    payload = {
        "user": "minh",
        "action": "predict",
        "features": [5.1, 3.5, 1.4, 0.2],
    }
    # json= tự serialize dict → JSON và set Content-Type
    response = requests.post("https://httpbin.org/post", json=payload, timeout=10)
    result = response.json()
    print(f"  Status: {response.status_code}")
    print(f"  Sent JSON: {result['json']}")


# ── Demo xử lý lỗi ──
def demo_error_handling():
    """Demo xử lý lỗi HTTP, kết nối và timeout."""
    print("\n=== Error Handling ===")
    try:
        response = requests.get("https://httpbin.org/status/404", timeout=5)
        response.raise_for_status()  # 404 → raise HTTPError
    except requests.HTTPError as e:
        print(f"  HTTP Error: {e}")
    except requests.ConnectionError:
        print("  Connection failed")
    except requests.Timeout:
        print("  Request timed out")


if __name__ == "__main__":
    demo_get()
    demo_post()
    demo_error_handling()

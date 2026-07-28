"""Đáp án Module 05"""
import re
import time
import functools
import requests


def get_github_user(username: str) -> dict:
    response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
    response.raise_for_status()
    data = response.json()
    return {"name": data.get("name"), "public_repos": data["public_repos"]}


def parse_apache_log(line: str) -> dict | None:
    pattern = r'(\S+) - - \[([^\]]+)\] "(\S+) (\S+) (\S+)" (\d+) (\d+)'
    match = re.match(pattern, line)
    if not match:
        return None
    return {
        "ip": match.group(1),
        "timestamp": match.group(2),
        "method": match.group(3),
        "path": match.group(4),
        "status": int(match.group(6)),
        "size": int(match.group(7)),
    }


def retry(max_attempts: int = 3, delay: float = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"  Attempt {attempt} failed: {e}. Retry in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.5)
def fetch_url(url: str) -> str:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.text[:100]


if __name__ == "__main__":
    user = get_github_user("tiangolo")
    print(f"GitHub user: {user}")

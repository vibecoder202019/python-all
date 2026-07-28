"""Module 05 — requests HTTP client"""
import requests


def demo_get():
    print("=== GET: GitHub API ===")
    url = "https://api.github.com/repos/tiangolo/fastapi"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(f"  Repo: {data['full_name']}")
    print(f"  Stars: {data['stargazers_count']:,}")
    print(f"  Language: {data['language']}")
    print(f"  Description: {data['description'][:80]}...")


def demo_post():
    print("\n=== POST: httpbin.org ===")
    payload = {
        "user": "minh",
        "action": "predict",
        "features": [5.1, 3.5, 1.4, 0.2],
    }
    response = requests.post("https://httpbin.org/post", json=payload, timeout=10)
    result = response.json()
    print(f"  Status: {response.status_code}")
    print(f"  Sent JSON: {result['json']}")


def demo_error_handling():
    print("\n=== Error Handling ===")
    try:
        response = requests.get("https://httpbin.org/status/404", timeout=5)
        response.raise_for_status()
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

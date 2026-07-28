"""Đáp án bài tập FastAPI — tham khảo"""
import re
import time
from fastapi import FastAPI, Request, HTTPException, Depends, Header
from fastapi.testclient import TestClient

# --- Bài 1: Search users ---
def search_users_example():
    """Thêm vào routers/users.py"""
    code = '''
@router.get("/search")
def search_users(q: str = ""):
    results = [u for u in _users_db.values() if q.lower() in u["name"].lower()]
    return results
'''
    print("Bài 1 — Thêm endpoint search:")
    print(code)


# --- Bài 2: Email validation ---
def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


# --- Bài 4: Logging middleware ---
def logging_middleware_example():
    code = '''
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start
    print(f"{request.method} {request.url.path} → {response.status_code} ({duration:.3f}s)")
    return response
'''
    print("Bài 4 — Logging middleware:")
    print(code)


# --- Bài 5: API Key auth ---
API_KEYS = {"secret-key-123": "admin", "demo-key-456": "user"}

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return API_KEYS[x_api_key]


if __name__ == "__main__":
    search_users_example()
    print(f"\nBài 2 — validate_email('test@mail.com'): {validate_email('test@mail.com')}")
    print(f"  validate_email('invalid'): {validate_email('invalid')}")
    logging_middleware_example()

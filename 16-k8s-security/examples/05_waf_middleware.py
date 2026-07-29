#!/usr/bin/env python3
"""
Module 16 — Ví dụ 05: FastAPI WAF Middleware (SQLi + Rate Limit)

Chạy:
  pip install fastapi uvicorn
  uvicorn examples.05_waf_middleware:app --reload --port 8080

Test:
  curl "http://localhost:8080/search?q=hello"           # OK
  curl "http://localhost:8080/search?q=' OR 1=1--"     # 403 Blocked
"""
from __future__ import annotations

import sys
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import RateLimiter, detect_sql_injection, sanitize_input

app = FastAPI(title="WAF Demo — Module 16")
limiter = RateLimiter(max_requests=20, window_seconds=60)


@app.middleware("http")
async def waf_middleware(request: Request, call_next):
    """Middleware WAF — kiểm tra mọi request trước khi vào handler."""
    client_ip = request.client.host if request.client else "unknown"

    # 1. Rate limit — chống DDoS
    rate_result = limiter.is_allowed(client_ip)
    if not rate_result.passed:
        return JSONResponse(status_code=429, content={"error": "Too Many Requests", "detail": rate_result.detail})

    # 2. Kiểm tra query params — chống SQLi
    for key, value in request.query_params.items():
        sqli = detect_sql_injection(value)
        if not sqli.passed:
            return JSONResponse(status_code=403, content={"error": "Blocked by WAF", "threat": "sqli", "detail": sqli.detail})

    # 3. Kiểm tra path — chống path traversal
    if ".." in str(request.url.path):
        return JSONResponse(status_code=403, content={"error": "Path traversal blocked"})

    return await call_next(request)


@app.get("/search")
def search(q: str = ""):
    """Endpoint demo — tìm kiếm an toàn."""
    safe_q = sanitize_input(q)
    return {"query": safe_q, "results": [], "message": "WAF passed — query an toàn"}


@app.get("/health")
def health():
    return {"status": "ok", "waf": "enabled"}

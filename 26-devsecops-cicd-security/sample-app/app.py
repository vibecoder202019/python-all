"""
Sample FastAPI app for DevSecOps lab.

Cố ý chứa pattern yếu để Bandit/Semgrep bắt được trong lab
(không dùng code này cho production).
"""
from __future__ import annotations

import hashlib
import os
import subprocess

from fastapi import FastAPI, Query

app = FastAPI(title="devsecops-lab-app", version="0.1.0")

# LAB-ONLY: hardcoded-looking secret pattern (Gitleaks may flag in CI)
# In real apps use env / Vault — never commit real credentials.
LAB_DEMO_API_KEY = os.environ.get("LAB_DEMO_API_KEY", "lab-not-a-real-secret")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/hash")
def weak_hash(data: str = Query("demo")) -> dict[str, str]:
    # LAB intentional weak crypto — Bandit B324 (MD5). Production: use sha256+.
    digest = hashlib.md5(data.encode()).hexdigest()
    return {"algo": "md5", "digest": digest}


@app.get("/run")
def run_echo(msg: str = Query("hello")) -> dict[str, str]:
    # LAB: shell=True pattern — avoid in real code; Semgrep/Bandit may warn
    # Still constrain input for safety in this teaching repo.
    safe = "".join(c for c in msg if c.isalnum() or c in " -_")[:80]
    out = subprocess.check_output(["echo", safe], text=True)  # safer than shell=True
    return {"echo": out.strip(), "demo_key_set": bool(LAB_DEMO_API_KEY)}


@app.get("/")
def root() -> dict[str, str]:
    return {"app": "devsecops-lab-app", "hint": "See Module 26 pipeline"}

#!/usr/bin/env python3
"""Ví dụ 03 — Audit security headers (fixture response headers)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "project"))

from common import audit_security_headers

WEAK = {
    "content-type": "text/html",
    "server": "nginx",
}
STRONG = {
    "strict-transport-security": "max-age=31536000; includeSubDomains",
    "content-security-policy": "default-src 'self'",
    "x-frame-options": "DENY",
    "x-content-type-options": "nosniff",
    "referrer-policy": "strict-origin-when-cross-origin",
    "permissions-policy": "camera=(), microphone=()",
}


def main() -> None:
    print("=== 03: Security headers audit ===\n")
    for name, headers in (("weak-site", WEAK), ("hardened-site", STRONG)):
        r = audit_security_headers(headers)
        icon = "OK " if r.passed else "GAP"
        print(f"[{icon}] {name} score={r.score}")
        print(f"       {r.detail}")
        print()


if __name__ == "__main__":
    main()

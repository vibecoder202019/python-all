#!/usr/bin/env python3
"""Ví dụ 04 — Sanitize input chống XSS/SQLi (defense)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "project"))

from common import sanitize_user_input

SAMPLES = [
    "hello world",
    "<script>alert(1)</script>",
    "search' OR 1=1--",
    "https://ok.example/path",
]


def main() -> None:
    print("=== 04: Input sanitizer (OWASP-ish) ===\n")
    for raw in SAMPLES:
        safe, r = sanitize_user_input(raw)
        icon = "OK " if r.passed else "BLOCK"
        print(f"[{icon}] in={raw!r}")
        print(f"       out={safe!r}  score={r.score}")
        if r.findings:
            print(f"       {r.detail}")
        print()


if __name__ == "__main__":
    main()

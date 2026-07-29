#!/usr/bin/env python3
"""Module 16 — Ví dụ 01: Phát hiện SQL Injection."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import detect_sql_injection

SAMPLES = [
    ("admin", True),
    ("' OR '1'='1", False),
    ("'; DROP TABLE users; --", False),
    ("1 UNION SELECT password FROM users", False),
    ("user@example.com", True),
]

def main():
    print("=== Ví dụ 01: SQL Injection Detection ===\n")
    for payload, expect_safe in SAMPLES:
        result = detect_sql_injection(payload)
        status = "✅ AN TOÀN" if result.passed else "🚫 CHẶN"
        expected = "✓" if result.passed == expect_safe else "✗ SAI"
        print(f"  Input : {payload!r}")
        print(f"  Kết quả: {status} — {result.detail} [{expected}]")
        print()

if __name__ == "__main__":
    main()

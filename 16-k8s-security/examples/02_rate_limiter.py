#!/usr/bin/env python3
"""Module 16 — Ví dụ 02: Rate Limiter chống DDoS/brute-force."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import RateLimiter

def main():
    print("=== Ví dụ 02: Rate Limiter (Anti-DDoS) ===\n")
    limiter = RateLimiter(max_requests=5, window_seconds=10)

    print("Giả lập 8 request từ cùng IP trong 10 giây (giới hạn 5):\n")
    for i in range(1, 9):
        result = limiter.is_allowed("192.168.1.100")
        icon = "✅" if result.passed else "🚫"
        print(f"  Request #{i}: {icon} {result.detail}")

if __name__ == "__main__":
    main()

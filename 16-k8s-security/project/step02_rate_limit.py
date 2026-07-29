"""Module 16 — Bước 2: Rate Limiter Anti-DDoS."""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import RateLimiter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--requests", type=int, default=8)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    print("=== Bước 2: Rate Limiter ===\n")
    limiter = RateLimiter(max_requests=args.limit, window_seconds=10)
    for i in range(1, args.requests + 1):
        r = limiter.is_allowed("client-1")
        print(f"  #{i}: {'✅' if r.passed else '🚫'} {r.detail}")

if __name__ == "__main__":
    main()

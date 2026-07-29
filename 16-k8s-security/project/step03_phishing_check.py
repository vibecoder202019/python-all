"""Module 16 — Bước 3: Phishing URL Checker."""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import check_phishing_url

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", nargs="?", default="https://paypal-verify.xyz/login")
    args = parser.parse_args()
    print("=== Bước 3: Phishing Checker ===\n")
    r = check_phishing_url(args.url)
    print(f"URL: {args.url}")
    print(f"{'✅ AN TOÀN' if r.passed else '🚫 NGHI NGỜ'} (score={r.score}): {r.detail}")

if __name__ == "__main__":
    main()

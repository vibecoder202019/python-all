#!/usr/bin/env python3
"""Module 16 — Ví dụ 03: Phát hiện URL Phishing."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import check_phishing_url

URLS = [
    "https://github.com/login",
    "http://192.168.1.1/login-verify-account",
    "https://paypal-secure-update.xyz/confirm-password",
    "https://google.com@evil-site.tk/steal",
    "https://mybank.com/dashboard",
]

def main():
    print("=== Ví dụ 03: Phishing URL Detection ===\n")
    for url in URLS:
        result = check_phishing_url(url)
        icon = "✅" if result.passed else "🚫"
        print(f"  {icon} [{result.score:3d}] {url}")
        if not result.passed:
            print(f"       → {result.detail}")
        print()

if __name__ == "__main__":
    main()

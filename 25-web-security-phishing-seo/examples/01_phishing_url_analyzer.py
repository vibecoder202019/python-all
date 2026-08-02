#!/usr/bin/env python3
"""Ví dụ 01 — Phân tích URL phishing (awareness)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "project"))

from common import analyze_phishing_url

URLS_FILE = ROOT / "data" / "sample_urls.txt"


def main() -> None:
    print("=== 01: Phishing URL analyzer ===\n")
    urls = [u.strip() for u in URLS_FILE.read_text().splitlines() if u.strip()]
    for url in urls:
        r = analyze_phishing_url(url)
        icon = "OK " if r.passed else "RISK"
        print(f"[{icon}] score={r.score:3d}  {url}")
        if r.findings:
            for f in r.findings:
                print(f"         - {f}")
        print()


if __name__ == "__main__":
    main()

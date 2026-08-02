#!/usr/bin/env python3
"""Ví dụ 02 — Red flags trong email phishing (fixture text)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "project"))

from common import analyze_email_text

EMAILS_FILE = ROOT / "data" / "sample_emails.txt"


def main() -> None:
    print("=== 02: Email phishing red flags ===\n")
    raw = EMAILS_FILE.read_text()
    blocks = [b.strip() for b in raw.split("---") if b.strip()]
    for i, block in enumerate(blocks, 1):
        r = analyze_email_text(block)
        subject = next(
            (ln.split(":", 1)[1].strip() for ln in block.splitlines() if ln.lower().startswith("subject:")),
            f"email-{i}",
        )
        icon = "OK " if r.passed else "RISK"
        print(f"[{icon}] score={r.score:3d}  {subject}")
        for f in r.findings:
            print(f"         - {f}")
        print()


if __name__ == "__main__":
    main()

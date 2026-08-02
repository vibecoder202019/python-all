#!/usr/bin/env python3
"""Ví dụ 05 — SEO integrity audit trên fixture chủ site."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "project"))

from common import SiteAuditInput, audit_seo_integrity

FIXTURE = ROOT / "data" / "gsc_fixture_compromised.json"


def main() -> None:
    print("=== 05: SEO / Search integrity audit ===\n")
    data = json.loads(FIXTURE.read_text())
    site = SiteAuditInput(
        robots_txt=data["robots_txt"],
        sitemap_urls=data["sitemap_urls"],
        indexed_suspicious_paths=data["indexed_suspicious_paths"],
        security_issues=data["security_issues"],
        manual_actions=data["manual_actions"],
        spammy_outbound_links=data["spammy_outbound_links"],
    )
    r = audit_seo_integrity(site)
    icon = "OK " if r.passed else "ALERT"
    print(f"[{icon}] site={data['site']} score={r.score}")
    for f in r.findings:
        print(f"  - {f}")
    print()
    print("→ Mục tiêu: phát hiện site BỊ XÂM NHẬP / spam — rồi cleanup, không phải tấn công đối thủ.")


if __name__ == "__main__":
    main()

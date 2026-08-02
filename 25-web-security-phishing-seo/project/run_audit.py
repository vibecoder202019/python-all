#!/usr/bin/env python3
"""Project — Pipeline audit phòng thủ end-to-end."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "project"))

from common import (
    SiteAuditInput,
    analyze_email_text,
    analyze_phishing_url,
    audit_security_headers,
    audit_seo_integrity,
    sanitize_user_input,
    triage_ranking_drop,
)


def main() -> None:
    print("=== Module 25 project: Web defense audit pipeline ===\n")

    # 1) URLs
    urls = [u.strip() for u in (ROOT / "data" / "sample_urls.txt").read_text().splitlines() if u.strip()]
    risky_urls = [u for u in urls if not analyze_phishing_url(u).passed]
    print(f"[1] Phishing URLs flagged: {len(risky_urls)}/{len(urls)}")

    # 2) Emails
    blocks = [b.strip() for b in (ROOT / "data" / "sample_emails.txt").read_text().split("---") if b.strip()]
    risky_mails = [b for b in blocks if not analyze_email_text(b).passed]
    print(f"[2] Phishing emails flagged: {len(risky_mails)}/{len(blocks)}")

    # 3) Headers
    headers_r = audit_security_headers({"content-type": "text/html"})
    print(f"[3] Headers gaps: score={headers_r.score} ({'OK' if headers_r.passed else 'NEED FIX'})")

    # 4) Input
    _, inj = sanitize_user_input("<script>alert(1)</script>")
    print(f"[4] XSS sample blocked: {not inj.passed}")

    # 5) SEO integrity + triage
    fixture = json.loads((ROOT / "data" / "gsc_fixture_compromised.json").read_text())
    seo = audit_seo_integrity(
        SiteAuditInput(
            robots_txt=fixture["robots_txt"],
            sitemap_urls=fixture["sitemap_urls"],
            indexed_suspicious_paths=fixture["indexed_suspicious_paths"],
            security_issues=fixture["security_issues"],
            manual_actions=fixture["manual_actions"],
            spammy_outbound_links=fixture["spammy_outbound_links"],
        )
    )
    plan = triage_ranking_drop(fixture)
    print(f"[5] SEO integrity score={seo.score} → triage branch={plan['branch']} ({plan['priority']})")
    print("    Next steps:")
    for step in plan["steps"][:3]:
        print(f"      - {step}")

    report = {
        "risky_urls": len(risky_urls),
        "risky_emails": len(risky_mails),
        "headers_score": headers_r.score,
        "seo_score": seo.score,
        "triage": plan["branch"],
    }
    out = ROOT / "data" / "last_audit_report.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"\n✓ Wrote {out.relative_to(ROOT)}")
    print("Remember: defense & recovery only — do not attack third parties.")


if __name__ == "__main__":
    main()

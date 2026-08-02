#!/usr/bin/env python3
"""
Module 12 — Ví dụ 07: Website LIVE or DIE

Chạy: python examples/07_website_live_or_die.py
      python examples/07_website_live_or_die.py --url https://example.com --name Example

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU:
  1. Kiểm tra danh sách website → trạng thái rõ ràng LIVE / DIE.
  2. In latency + lý do khi DIE.
  3. Summary: bao nhiêu LIVE / DIE.
═══════════════════════════════════════════════════════════════════════════
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "project"))

from monitoring import SiteCheck, check_website, summarize_sites

try:
    import yaml
except ImportError:
    yaml = None


DEFAULT_SITES = [
    {"name": "Example", "url": "https://example.com"},
    {"name": "GitHub", "url": "https://github.com"},
    {"name": "Dead local", "url": "http://127.0.0.1:19999/"},
]


def load_sites(path: Path | None) -> list[dict]:
    if path and path.exists() and yaml is not None:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return list(data.get("websites") or DEFAULT_SITES)
    return list(DEFAULT_SITES)


def main() -> None:
    parser = argparse.ArgumentParser(description="Website LIVE / DIE checker")
    parser.add_argument("--config", default="", help="YAML websites list")
    parser.add_argument("--url", action="append", default=[], help="URL bổ sung")
    parser.add_argument("--name", action="append", default=[], help="Tên tương ứng --url")
    parser.add_argument("--timeout", type=float, default=5.0)
    args = parser.parse_args()

    module = Path(__file__).resolve().parents[1]
    cfg = Path(args.config) if args.config else module / "data" / "websites.yaml"
    sites = load_sites(cfg if cfg.exists() else None)

    for i, url in enumerate(args.url):
        name = args.name[i] if i < len(args.name) else url
        sites.append({"name": name, "url": url})

    print("=== Website LIVE / DIE ===\n")
    results: list[SiteCheck] = []
    for s in sites:
        r = check_website(
            s.get("name", s["url"]),
            s["url"],
            timeout=args.timeout,
            expect_status=s.get("expect_status"),
            expect_body_contains=s.get("expect_body_contains"),
        )
        results.append(r)
        icon = "🟢" if r.state == "LIVE" else "🔴"
        print(f"{icon} {r.state:4s}  {r.name:20s}  {r.latency_ms:6.0f}ms  {r.reason}")
        print(f"       {r.url}")

    summary = summarize_sites(results)
    print(f"\nSummary: {summary['live']} LIVE / {summary['die']} DIE (total {summary['total']})")
    print("✓ Done" if summary["die"] == 0 else "⚠ Có site DIE — kiểm tra ngay")


if __name__ == "__main__":
    main()

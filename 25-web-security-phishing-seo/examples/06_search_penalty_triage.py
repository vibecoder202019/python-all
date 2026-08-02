#!/usr/bin/env python3
"""Ví dụ 06 — Triage ranking drop (Search Console-like fixture)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "project"))

from common import triage_ranking_drop


def run(path: Path) -> None:
    data = json.loads(path.read_text())
    plan = triage_ranking_drop(data)
    print(f"--- {path.name} ({data.get('site')}) ---")
    print(f"branch={plan['branch']}  priority={plan['priority']}")
    for i, step in enumerate(plan["steps"], 1):
        print(f"  {i}. {step}")
    print(f"note: {plan['note']}")
    print()


def main() -> None:
    print("=== 06: Ranking drop triage ===\n")
    for name in ("gsc_fixture_compromised.json", "gsc_fixture_core_update.json"):
        run(ROOT / "data" / name)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Ví dụ 01 — Liệt kê AWX job templates."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "project"))

from awx_client import AwxClient, AwxConfig


def main() -> None:
    print("=== 01: List AWX job templates ===\n")
    client = AwxClient(AwxConfig.from_env(force_demo="--demo" in sys.argv or True))
    for t in client.list_job_templates():
        print(f"[{t['id']:>3}] {t['name']}")
        print(f"      playbook={t.get('playbook')} project={t.get('project')}")
        print(f"      {t.get('description', '')}\n")


if __name__ == "__main__":
    main()

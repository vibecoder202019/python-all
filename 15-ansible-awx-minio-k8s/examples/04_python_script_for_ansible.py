#!/usr/bin/env python3
"""
Module 15 — Ví dụ 04: Python script dùng với Ansible script module trên AWX

Script này được playbook AWX gọi:
  - script: scripts/process_data.py --name "{{ user_name }}"

Chạy local để test:
  python examples/04_python_script_for_ansible.py
  python examples/04_python_script_for_ansible.py --name "Học viên"
"""
from __future__ import annotations

import argparse
import json
import platform
import sys
from datetime import datetime, timezone


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="AWX User")
    args = parser.parse_args()

    # Output JSON — Ansible parse bằng filter from_json
    result = {
        "message": f"Xin chào {args.name}!",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "hostname": platform.node(),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

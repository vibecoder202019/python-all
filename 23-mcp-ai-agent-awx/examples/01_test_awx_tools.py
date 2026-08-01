#!/usr/bin/env python3
"""Test AWX tools trực tiếp (không MCP) — demo hoặc AWX thật."""
import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from lib import awx_tools


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--launch", metavar="TEMPLATE_NAME")
    args = parser.parse_args()

    demo = args.demo or os.environ.get("AWX_DEMO_MODE", "").lower() in ("1", "true")

    print("=== Templates ===")
    print(awx_tools.list_templates_json(demo=demo))

    if args.launch:
        print("\n=== Launch ===")
        print(
            awx_tools.launch_job_json(
                template_name=args.launch,
                extra_vars={"user_name": "MCP-Lab"},
                demo=demo,
            )
        )


if __name__ == "__main__":
    main()

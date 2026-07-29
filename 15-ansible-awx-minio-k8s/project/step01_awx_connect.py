"""
Module 15 — Dự án Bước 1: Kết nối AWX API

Chạy: python project/step01_awx_connect.py --demo
      python project/step01_awx_connect.py
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import get_awx_client, handle_awx_error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    print("=== Bước 1: AWX Connect ===\n")

    if args.demo:
        print("🔍 DEMO — cần AWX thật để chạy không --demo")
        print("  export AWX_URL=http://localhost:8052")
        print("  export AWX_TOKEN=your-token")
        return

    try:
        ctx = get_awx_client()
        templates = ctx.client.list_job_templates()
        print(f"✅ Kết nối AWX: {ctx.base_url}")
        print(f"   Job Templates: {len(templates)}")
    except Exception as e:
        print(handle_awx_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

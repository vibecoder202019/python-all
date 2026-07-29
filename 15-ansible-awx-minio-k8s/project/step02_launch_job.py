"""
Module 15 — Dự án Bước 2: Launch Job Template

Chạy: python project/step02_launch_job.py --demo
      python project/step02_launch_job.py --template-id 7
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import get_awx_client, handle_awx_error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template-id", type=int)
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    print("=== Bước 2: Launch Job ===\n")

    if args.demo:
        print("🔍 DEMO: POST /api/v2/job_templates/{id}/launch/")
        return

    if not args.template_id:
        print("❌ Cần --template-id (xem id bằng step01 hoặc examples/01)")
        sys.exit(1)

    try:
        ctx = get_awx_client()
        result = ctx.client.launch_job(args.template_id)
        print(f"✅ Job launched: id={result.get('job')}")
    except Exception as e:
        print(handle_awx_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

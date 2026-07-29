#!/usr/bin/env python3
"""
Module 15 — Ví dụ 02: Launch Job Template từ Python

Chạy:
  python examples/02_launch_job.py --template-name "Python Hello World"
  python examples/02_launch_job.py --template-id 7 --wait
  python examples/02_launch_job.py --demo   # không cần AWX — in mô phỏng
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import get_awx_client, handle_awx_error


def demo_mode():
    """Chế độ demo — không cần AWX thật."""
    print("=== DEMO MODE (không cần AWX) ===\n")
    print("Mô phỏng launch job:")
    print("  POST /api/v2/job_templates/7/launch/")
    print('  Body: {"extra_vars": {"user_name": "Demo"}}')
    print("  Response: {\"job\": 42}")
    print("\nPoll job:")
    print("  GET /api/v2/jobs/42/ → status: running → successful")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template-id", type=int)
    parser.add_argument("--template-name")
    parser.add_argument("--extra-vars", help='JSON, ví dụ \'{"user_name":"Lab"}\'')
    parser.add_argument("--wait", action="store_true")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    if args.demo:
        demo_mode()
        return

    print("=== Ví dụ 02: Launch Job ===\n")

    try:
        ctx = get_awx_client()
        template_id = args.template_id

        if args.template_name:
            tmpl = ctx.client.get_template_by_name(args.template_name)
            if not tmpl:
                print(f"❌ Không tìm thấy template: {args.template_name}")
                sys.exit(1)
            template_id = tmpl["id"]
            print(f"📋 Template: {args.template_name} (id={template_id})")

        if not template_id:
            print("❌ Cần --template-id hoặc --template-name (hoặc --demo)")
            sys.exit(1)

        extra = json.loads(args.extra_vars) if args.extra_vars else None
        result = ctx.client.launch_job(template_id, extra_vars=extra)
        job_id = result.get("job")
        print(f"✅ Launched job id={job_id}")

        if args.wait and job_id:
            print("\n⏳ Đang đợi...")
            job = ctx.client.wait_for_job(job_id)
            print(f"Kết quả: {job.get('status')}")
            if job.get("status") == "successful":
                print("\n--- STDOUT ---")
                print(ctx.client.get_job_stdout(job_id))

    except Exception as e:
        print(handle_awx_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

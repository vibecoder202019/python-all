"""
Module 15 — Dự án Bước 5: Poll job status và lấy stdout

Chạy: python project/step05_monitor_job.py --job-id 42 --demo
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import get_awx_client, handle_awx_error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--job-id", type=int)
    parser.add_argument("--wait", action="store_true")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    print("=== Bước 5: Monitor Job ===\n")

    if args.demo:
        print("🔍 DEMO: GET /api/v2/jobs/{id}/ → poll đến successful")
        return

    if not args.job_id:
        print("❌ Cần --job-id")
        sys.exit(1)

    try:
        ctx = get_awx_client()
        if args.wait:
            job = ctx.client.wait_for_job(args.job_id)
        else:
            job = ctx.client.get_job(args.job_id)
        print(f"Job {args.job_id}: {job.get('status')}")
        if job.get("status") == "successful":
            print("\n--- STDOUT ---")
            print(ctx.client.get_job_stdout(args.job_id)[:500])
    except Exception as e:
        print(handle_awx_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Module 15 — Dự án Bước 6: AWX Automation CLI (hoàn chỉnh)

CLI tích hợp: list templates, launch job, upload MinIO, monitor.

Chạy:
  python project/step06_final.py --help
  python project/step06_final.py list-templates
  python project/step06_final.py launch --template-id 7 --wait
  python project/step06_final.py upload-report --demo
  python project/step06_final.py pipeline --demo
"""
from __future__ import annotations

import argparse
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import (
    get_awx_client,
    save_json_report,
    upload_to_minio,
    handle_awx_error,
)


def cmd_list_templates(_args):
    ctx = get_awx_client()
    for t in ctx.client.list_job_templates():
        print(f"  {t['id']:4d}  {t['name']}")


def cmd_launch(args):
    ctx = get_awx_client()
    extra = None
    if args.extra_vars:
        import json
        extra = json.loads(args.extra_vars)
    result = ctx.client.launch_job(args.template_id, extra_vars=extra)
    job_id = result.get("job")
    print(f"✅ Job id={job_id}")
    if args.wait and job_id:
        job = ctx.client.wait_for_job(job_id)
        print(f"Status: {job.get('status')}")


def cmd_upload_report(args):
    if args.demo:
        print("🔍 DEMO upload report → MinIO")
        return
    path = tempfile.mktemp(suffix=".json")
    save_json_report(
        {"cli": "awx-automation", "at": datetime.now(timezone.utc).isoformat()},
        path,
    )
    uri = upload_to_minio(path, args.bucket, f"reports/cli_{Path(path).stem}.json")
    Path(path).unlink(missing_ok=True)
    print(f"✅ {uri}")


def cmd_pipeline(args):
    if args.demo:
        print("🔍 DEMO pipeline: report → MinIO → AWX launch")
        return
    cmd_upload_report(argparse.Namespace(demo=False, bucket="awx-artifacts"))
    if args.template_id:
        cmd_launch(argparse.Namespace(
            template_id=args.template_id, extra_vars=None, wait=args.wait
        ))


def main():
    parser = argparse.ArgumentParser(
        description="AWX Automation CLI — Module 15 Final Project",
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list-templates", help="Liệt kê Job Template")

    p_launch = sub.add_parser("launch", help="Launch job")
    p_launch.add_argument("--template-id", type=int, required=True)
    p_launch.add_argument("--extra-vars")
    p_launch.add_argument("--wait", action="store_true")

    p_upload = sub.add_parser("upload-report", help="Upload report lên MinIO")
    p_upload.add_argument("--bucket", default="awx-artifacts")
    p_upload.add_argument("--demo", action="store_true")

    p_pipe = sub.add_parser("pipeline", help="Report + MinIO + AWX")
    p_pipe.add_argument("--template-id", type=int)
    p_pipe.add_argument("--wait", action="store_true")
    p_pipe.add_argument("--demo", action="store_true")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    try:
        if args.command == "list-templates":
            cmd_list_templates(args)
        elif args.command == "launch":
            cmd_launch(args)
        elif args.command == "upload-report":
            cmd_upload_report(args)
        elif args.command == "pipeline":
            cmd_pipeline(args)
    except Exception as e:
        print(handle_awx_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

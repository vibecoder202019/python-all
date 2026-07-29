#!/usr/bin/env python3
"""
Module 15 — Ví dụ 06: Pipeline đầy đủ Python → AWX → MinIO

Luồng:
  1. Tạo report JSON bằng Python
  2. Upload lên MinIO
  3. (Tuỳ chọn) Launch AWX job

Chạy:
  python examples/06_full_pipeline.py --demo
  python examples/06_full_pipeline.py --upload-only
  python examples/06_full_pipeline.py --launch-template "Python Hello World"
"""
import argparse
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import get_awx_client, save_json_report, upload_to_minio, handle_awx_error


def demo_mode():
    print("=== DEMO: Full Pipeline ===\n")
    print("1. Python tạo report.json")
    print("2. boto3 upload → s3://awx-artifacts/reports/")
    print("3. requests POST → AWX launch job template")
    print("4. Poll GET /api/v2/jobs/{id}/ → successful")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--upload-only", action="store_true")
    parser.add_argument("--launch-template")
    parser.add_argument("--wait", action="store_true")
    args = parser.parse_args()

    if args.demo:
        demo_mode()
        return

    print("=== Ví dụ 06: Full Pipeline ===\n")

    # Bước 1: Tạo report
    report = {
        "pipeline": "python-awx-minio",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "step": "generate_report",
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        report_path = f.name
    save_json_report(report, report_path)
    print(f"[1/3] ✅ Report: {report_path}")

    # Bước 2: Upload MinIO
    try:
        uri = upload_to_minio(report_path, "awx-artifacts", f"reports/pipeline_{Path(report_path).stem}.json")
        print(f"[2/3] ✅ MinIO: {uri}")
    except Exception as e:
        print(f"[2/3] ⚠️  MinIO skip: {handle_awx_error(e)}")

    Path(report_path).unlink(missing_ok=True)

    if args.upload_only:
        return

    # Bước 3: Launch AWX job (tuỳ chọn)
    if args.launch_template:
        try:
            ctx = get_awx_client()
            tmpl = ctx.client.get_template_by_name(args.launch_template)
            if not tmpl:
                print(f"[3/3] ❌ Template không tồn tại: {args.launch_template}")
                sys.exit(1)
            result = ctx.client.launch_job(tmpl["id"])
            job_id = result.get("job")
            print(f"[3/3] ✅ AWX job launched: id={job_id}")
            if args.wait and job_id:
                job = ctx.client.wait_for_job(job_id)
                print(f"       Status: {job.get('status')}")
        except Exception as e:
            print(f"[3/3] ⚠️  AWX skip: {handle_awx_error(e)}")
    else:
        print("[3/3] ⏭️  Bỏ qua AWX (thêm --launch-template 'Tên Template')")


if __name__ == "__main__":
    main()

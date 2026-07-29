#!/usr/bin/env python3
"""
Module 15 — Ví dụ 05: Upload file lên MinIO bằng boto3 (S3 API)

Chạy (cần MinIO đang chạy + port-forward):
  kubectl port-forward svc/minio 9000:9000 -n minio
  python examples/05_minio_boto3.py
  python examples/05_minio_boto3.py --demo
"""
import argparse
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import save_json_report, upload_to_minio, handle_awx_error


def demo_mode():
    print("=== DEMO: MinIO Upload ===\n")
    print("boto3.client('s3', endpoint_url='http://localhost:9000')")
    print("client.upload_file('report.json', 'awx-artifacts', 'reports/report.json')")
    print("→ s3://awx-artifacts/reports/report.json")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--bucket", default="awx-artifacts")
    args = parser.parse_args()

    if args.demo:
        demo_mode()
        return

    print("=== Ví dụ 05: MinIO boto3 Upload ===\n")

    # Tạo file report mẫu
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        report_path = f.name

    save_json_report(
        {"module": 15, "status": "demo", "message": "Upload từ Python boto3"},
        report_path,
    )
    print(f"📄 Report: {report_path}")

    try:
        uri = upload_to_minio(
            report_path,
            bucket=args.bucket,
            object_key=f"reports/{Path(report_path).name}",
        )
        print(f"✅ Uploaded: {uri}")
    except Exception as e:
        print(handle_awx_error(e))
        print("\n💡 Gợi ý:")
        print("  bash scripts/02-deploy-minio.sh")
        print("  kubectl port-forward svc/minio 9000:9000 -n minio")
        sys.exit(1)
    finally:
        Path(report_path).unlink(missing_ok=True)


if __name__ == "__main__":
    main()

"""
Module 15 — Dự án Bước 3: Upload artifact lên MinIO

Chạy: python project/step03_minio_upload.py --demo
      python project/step03_minio_upload.py
"""
import argparse
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import save_json_report, upload_to_minio, handle_awx_error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    print("=== Bước 3: MinIO Upload ===\n")

    if args.demo:
        print("🔍 DEMO: boto3 → MinIO S3 API")
        return

    report_path = tempfile.mktemp(suffix=".json")
    save_json_report({"step": 3, "module": 15}, report_path)

    try:
        uri = upload_to_minio(report_path, "awx-artifacts", "reports/step03.json")
        print(f"✅ Uploaded: {uri}")
    except Exception as e:
        print(handle_awx_error(e))
        sys.exit(1)
    finally:
        Path(report_path).unlink(missing_ok=True)


if __name__ == "__main__":
    main()

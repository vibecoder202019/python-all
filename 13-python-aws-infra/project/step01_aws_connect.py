"""
Dự án Bước 1 — Kết nối và xác minh AWS credentials
Chạy: python project/step01_aws_connect.py --demo
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import get_context, handle_aws_error


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    print("=== Bước 1: AWS Connect ===\n")
    try:
        ctx = get_context()
        print(f"✅ Connected to AWS")
        print(f"   Region:  {ctx.region}")
        print(f"   Account: {ctx.account_id}")
        print(f"   ARN:     {ctx.arn}")
    except Exception as e:
        print(handle_aws_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

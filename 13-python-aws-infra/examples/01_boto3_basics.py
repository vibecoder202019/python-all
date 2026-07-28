"""
Module 13 — Ví dụ 1: boto3 cơ bản — Session, credentials, STS

Chạy: python examples/01_boto3_basics.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Tạo boto3 Session với region từ AWS_DEFAULT_REGION.
  2. Gọi STS get_caller_identity — in Account, ARN, UserId.
  3. Liệt kê 5 region EC2; so sánh S3 client vs resource.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - Region và Session region.
  - Caller Identity (Account 12 số, ARN, UserId).
  - 5 region names; "S3 client list_buckets: N bucket(s)".
  - Thiếu credentials → "❌ Chưa cấu hình credentials".
═══════════════════════════════════════════════════════════════════════════
"""
import os
import sys

try:
    import boto3
    from botocore.exceptions import NoCredentialsError, ClientError
except ImportError:
    print("pip install boto3")
    sys.exit(1)


def main():
    print("=== boto3 Basics ===\n")

    region = os.environ.get("AWS_DEFAULT_REGION", "ap-southeast-1")
    print(f"1. Region: {region}")

    session = boto3.Session(region_name=region)
    print(f"   Session region: {session.region_name}")

    try:
        sts = session.client("sts")
        identity = sts.get_caller_identity()
        print(f"\n2. Caller Identity:")
        print(f"   Account: {identity['Account']}")
        print(f"   ARN:     {identity['Arn']}")
        print(f"   UserId:  {identity['UserId']}")
    except NoCredentialsError:
        print("\n❌ Chưa cấu hình credentials")
        print("   Chạy: aws configure")
        print("   Hoặc: export AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=...")
        return

    print(f"\n3. Available regions (EC2, first 5):")
    ec2 = session.client("ec2")
    regions = ec2.describe_regions()["Regions"][:5]
    for r in regions:
        print(f"   {r['RegionName']:20s} {r['Endpoint']}")

    print(f"\n4. Low-level client vs Resource:")
    s3_client = session.client("s3")
    s3_resource = session.resource("s3")
    buckets_client = s3_client.list_buckets().get("Buckets", [])
    print(f"   S3 client list_buckets: {len(buckets_client)} bucket(s)")
    print(f"   S3 resource type: {type(s3_resource).__name__}")

    print("\n✓ Done")


if __name__ == "__main__":
    main()

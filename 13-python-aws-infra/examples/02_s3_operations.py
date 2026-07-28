"""
AWS 02 — S3: list buckets, upload file, bucket info
Chạy: python examples/02_s3_operations.py
"""
import io
import sys
from datetime import datetime

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError
except ImportError:
    print("pip install boto3")
    sys.exit(1)

PROJECT_TAG = "python-all-learn"


def main():
    print("=== S3 Operations ===\n")

    try:
        s3 = boto3.client("s3")
    except NoCredentialsError:
        print("❌ Chưa cấu hình AWS credentials")
        return

    # List buckets
    buckets = s3.list_buckets().get("Buckets", [])
    print(f"1. Buckets ({len(buckets)}):")
    for b in buckets[:10]:
        print(f"   {b['Name']:40s} created {b['CreationDate'].strftime('%Y-%m-%d')}")

    # Upload demo file to first bucket or dry-run
    demo_key = f"demo/upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    demo_content = f"Python All Learn — S3 demo at {datetime.now().isoformat()}"

    if buckets:
        bucket = buckets[0]["Name"]
        print(f"\n2. Upload demo file → s3://{bucket}/{demo_key}")
        try:
            s3.put_object(
                Bucket=bucket,
                Key=demo_key,
                Body=demo_content.encode(),
                Tagging=f"Project={PROJECT_TAG}",
            )
            print("   ✓ Upload thành công")

            obj = s3.head_object(Bucket=bucket, Key=demo_key)
            print(f"   Size: {obj['ContentLength']} bytes")

            s3.delete_object(Bucket=bucket, Key=demo_key)
            print("   ✓ Đã xóa file demo (cleanup)")
        except ClientError as e:
            print(f"   ❌ {e.response['Error']['Code']}: {e.response['Error']['Message']}")
    else:
        print("\n2. Không có bucket — bỏ qua upload demo")
        print("   (Tạo bucket ở project step03 với --apply)")

    print("\n3. S3 API patterns:")
    print("   s3.list_buckets()           — liệt kê")
    print("   s3.put_object(Bucket, Key)  — upload")
    print("   s3.get_object(Bucket, Key)  — download")
    print("   s3.delete_object(Bucket, Key) — xóa")

    print("\n✓ Done")


if __name__ == "__main__":
    main()

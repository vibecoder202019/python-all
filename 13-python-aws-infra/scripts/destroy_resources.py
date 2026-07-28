"""
Xóa tài nguyên AWS có tag Project=python-all-learn
Chạy: python scripts/destroy_resources.py
      python scripts/destroy_resources.py --apply
"""
import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import get_context, handle_aws_error, PROJECT_TAG_KEY, PROJECT_TAG_VALUE

MODULE_DIR = Path(__file__).parent.parent
STATE_FILE = MODULE_DIR / "data" / "state.json"


def terminate_instances(ec2, apply: bool):
    reservations = ec2.describe_instances(
        Filters=[
            {"Name": f"tag:{PROJECT_TAG_KEY}", "Values": [PROJECT_TAG_VALUE]},
            {"Name": "instance-state-name", "Values": ["running", "stopped", "pending"]},
        ]
    )["Reservations"]
    instance_ids = [i["InstanceId"] for r in reservations for i in r["Instances"]]

    print(f"🖥️  EC2 instances to terminate: {instance_ids or '(none)'}")
    if apply and instance_ids:
        ec2.terminate_instances(InstanceIds=instance_ids)
        print("   ⏳ Waiting for termination...")
        time.sleep(5)


def delete_security_groups(ec2, apply: bool):
    sgs = ec2.describe_security_groups(
        Filters=[{"Name": f"tag:{PROJECT_TAG_KEY}", "Values": [PROJECT_TAG_VALUE]}]
    )["SecurityGroups"]

    print(f"🔒 Security Groups to delete: {[sg['GroupId'] for sg in sgs] or '(none)'}")
    if apply:
        for sg in sgs:
            try:
                ec2.delete_security_group(GroupId=sg["GroupId"])
                print(f"   ✅ Deleted {sg['GroupId']}")
            except ec2.exceptions.ClientError as e:
                print(f"   ⚠️  {sg['GroupId']}: {e.response['Error']['Code']}")


def delete_s3_bucket(s3, bucket_name: str, apply: bool):
    print(f"🪣 S3 bucket to delete: {bucket_name or '(none)'}")
    if not apply or not bucket_name:
        return
    try:
        objects = s3.list_objects_v2(Bucket=bucket_name).get("Contents", [])
        if objects:
            s3.delete_objects(
                Bucket=bucket_name,
                Delete={"Objects": [{"Key": o["Key"]} for o in objects]},
            )
        s3.delete_bucket(Bucket=bucket_name)
        print(f"   ✅ Deleted s3://{bucket_name}")
    except s3.exceptions.NoSuchBucket:
        print(f"   ℹ️  Bucket not found")
    except Exception as e:
        print(f"   ⚠️  {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"=== Destroy Resources [{mode}] ===\n")

    try:
        ctx = get_context()
        ec2 = ctx.session.client("ec2")
        s3 = ctx.session.client("s3")

        state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
        bucket = state.get("s3_bucket")

        terminate_instances(ec2, args.apply)
        delete_security_groups(ec2, args.apply)
        delete_s3_bucket(s3, bucket, args.apply)

        if args.apply and STATE_FILE.exists():
            STATE_FILE.unlink()
            print("\n✅ State file cleared")

        print(f"\n{'✅ Destroyed' if args.apply else 'ℹ️  Dry-run done — thêm --apply để xóa thật'}")
    except Exception as e:
        print(handle_aws_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

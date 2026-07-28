"""
Dự án Bước 3 — Tạo S3 bucket
Chạy: python project/step03_create_s3.py --demo
      python project/step03_create_s3.py --apply
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import (
    get_context, handle_aws_error, load_infra_config,
    default_tags, dry_run_message, PROJECT_TAG_VALUE,
)

MODULE_DIR = Path(__file__).parent.parent
STATE_FILE = MODULE_DIR / "data" / "state.json"


def get_bucket_name(account_id: str, prefix: str) -> str:
    return f"{prefix}-{account_id}".lower()


def create_s3(apply: bool):
    config = load_infra_config(MODULE_DIR / "data" / "infra_config.yaml")
    ctx = get_context(config.get("region"))
    bucket_name = get_bucket_name(ctx.account_id, config["s3"]["bucket_prefix"])

    dry_run_message(
        "Create S3 Bucket",
        f"s3://{bucket_name} (versioning={config['s3']['versioning']})",
        apply,
    )

    if not apply:
        return bucket_name

    s3 = ctx.session.client("s3")
    try:
        if ctx.region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": ctx.region},
            )
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f"   ℹ️  Bucket đã tồn tại: {bucket_name}")
    except Exception as e:
        if "BucketAlreadyExists" in str(e):
            print(f"   ❌ Bucket name đã được dùng globally: {bucket_name}")
            return None
        raise

    s3.put_bucket_tagging(
        Bucket=bucket_name,
        Tagging={"TagSet": default_tags()},
    )

    if config["s3"].get("versioning"):
        s3.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={"Status": "Enabled"},
        )

    # Save state
    import json
    state = {}
    if STATE_FILE.exists():
        state = json.loads(STATE_FILE.read_text())
    state["s3_bucket"] = bucket_name
    STATE_FILE.write_text(json.dumps(state, indent=2))

    print(f"   ✅ Created: s3://{bucket_name}")
    return bucket_name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    print("=== Bước 3: Create S3 Bucket ===\n")
    try:
        create_s3(apply=args.apply)
    except Exception as e:
        print(handle_aws_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

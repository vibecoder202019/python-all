"""
AWS 04 — IAM: users, roles, policies (read-only)
Chạy: python examples/04_iam_security.py
"""
import sys

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError
except ImportError:
    print("pip install boto3")
    sys.exit(1)


def main():
    print("=== IAM Security (Read-only) ===\n")

    try:
        iam = boto3.client("iam")
        sts = boto3.client("sts")
    except NoCredentialsError:
        print("❌ Chưa cấu hình AWS credentials")
        return

    identity = sts.get_caller_identity()
    print(f"1. Current identity: {identity['Arn']}")

    # Current user info
    try:
        user = iam.get_user()
        username = user["User"]["UserName"]
        print(f"   IAM User: {username}")

        keys = iam.list_access_keys(UserName=username)["AccessKeyMetadata"]
        print(f"   Access keys: {len(keys)}")
        for k in keys:
            print(f"     {k['AccessKeyId']}  {k['Status']}  created {k['CreateDate'].strftime('%Y-%m-%d')}")
    except ClientError:
        print("   (Role/assumed identity — không phải IAM user trực tiếp)")

    # Account summary
    summary = iam.get_account_summary()["SummaryMap"]
    print(f"\n2. Account summary:")
    print(f"   Users:  {summary.get('Users', 0)}")
    print(f"   Roles:  {summary.get('Roles', 0)}")
    print(f"   Groups: {summary.get('Groups', 0)}")
    print(f"   Policies: {summary.get('Policies', 0)}")

    # Roles sample
    roles = iam.list_roles(MaxItems=5)["Roles"]
    print(f"\n3. IAM Roles (first 5):")
    for role in roles:
        print(f"   {role['RoleName']:40s} {role['Arn'][-30:]}")

    print(f"\n4. Least Privilege principles:")
    print("   ✓ Chỉ cấp quyền cần thiết")
    print("   ✓ Dùng IAM Role thay vì Access Key trên EC2")
    print("   ✓ Bật MFA cho console access")
    print("   ✓ Rotate access keys định kỳ")
    print("   ✓ Tag resources để audit")

    print("\n✓ Done")


if __name__ == "__main__":
    main()

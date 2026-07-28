"""
AWS 03 — EC2: instances, regions, AMIs
Chạy: python examples/03_ec2_basics.py
"""
import sys

try:
    import boto3
    from botocore.exceptions import NoCredentialsError
except ImportError:
    print("pip install boto3")
    sys.exit(1)


def main():
    print("=== EC2 Basics ===\n")

    try:
        ec2 = boto3.client("ec2")
        ec2_resource = boto3.resource("ec2")
    except NoCredentialsError:
        print("❌ Chưa cấu hình AWS credentials")
        return

    # Instances
    reservations = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running", "stopped", "pending"]}]
    )["Reservations"]

    instances = [i for r in reservations for i in r["Instances"]]
    print(f"1. EC2 Instances ({len(instances)}):")
    for inst in instances[:5]:
        name = next((t["Value"] for t in inst.get("Tags", []) if t["Key"] == "Name"), "—")
        print(f"   {inst['InstanceId']}  {inst['InstanceType']:10s}  {inst['State']['Name']:10s}  {name}")

    # AMIs — Amazon Linux 2023
    print(f"\n2. Amazon Linux 2023 AMIs (latest 3):")
    amis = ec2.describe_images(
        Owners=["amazon"],
        Filters=[
            {"Name": "name", "Values": ["al2023-ami-2023*-x86_64"]},
            {"Name": "state", "Values": ["available"]},
        ],
    )["Images"]
    amis.sort(key=lambda x: x["CreationDate"], reverse=True)
    for ami in amis[:3]:
        print(f"   {ami['ImageId']}  {ami['Name'][:50]}")

    # Instance types pricing tier
    print(f"\n3. Instance types phổ biến (Free Tier):")
    for itype, desc in [
        ("t3.micro", "1 vCPU, 1GB — Free Tier eligible"),
        ("t3.small", "2 vCPU, 2GB"),
        ("t3.medium", "2 vCPU, 4GB"),
    ]:
        print(f"   {itype:12s} {desc}")

    # Security groups count
    sgs = ec2.describe_security_groups()["SecurityGroups"]
    print(f"\n4. Security Groups: {len(sgs)}")

    print("\n✓ Done")


if __name__ == "__main__":
    main()

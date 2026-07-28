"""
Module 13 — Dự án Bước 2: Inventory tài nguyên AWS

Chạy: python project/step02_list_resources.py --demo

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Liệt kê EC2, S3 buckets, VPCs, Security Groups trong region.
  2. Đếm instances có tag Project=python-all-learn.
  3. In summary dạng bảng text.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - "📊 AWS Inventory — region" với counts EC2/S3/VPC/SG.
  - "N tagged python-all-learn" cho EC2.
═══════════════════════════════════════════════════════════════════════════
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import get_context, handle_aws_error, PROJECT_TAG_KEY, PROJECT_TAG_VALUE


def inventory(ctx):
    ec2 = ctx.session.client("ec2")
    s3 = ctx.session.client("s3")
    vpc = ctx.session.client("ec2")

    instances = [
        i for r in ec2.describe_instances()["Reservations"]
        for i in r["Instances"]
        if i["State"]["Name"] != "terminated"
    ]
    buckets = s3.list_buckets().get("Buckets", [])
    vpcs = vpc.describe_vpcs()["Vpcs"]
    sgs = ec2.describe_security_groups()["SecurityGroups"]

    tagged = [
        i for i in instances
        if any(t["Key"] == PROJECT_TAG_KEY and t["Value"] == PROJECT_TAG_VALUE
               for t in i.get("Tags", []))
    ]

    print(f"📊 AWS Inventory — {ctx.region}")
    print(f"   EC2 instances:     {len(instances)} ({len(tagged)} tagged {PROJECT_TAG_VALUE})")
    print(f"   S3 buckets:        {len(buckets)}")
    print(f"   VPCs:              {len(vpcs)}")
    print(f"   Security Groups:   {len(sgs)}")

    if instances:
        print(f"\n   EC2 (top 5):")
        for inst in instances[:5]:
            name = next((t["Value"] for t in inst.get("Tags", []) if t["Key"] == "Name"), "—")
            print(f"     {inst['InstanceId']}  {inst['InstanceType']}  {inst['State']['Name']}  {name}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    print("=== Bước 2: Resource Inventory ===\n")
    try:
        inventory(get_context())
    except Exception as e:
        print(handle_aws_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

"""
Module 13 — Dự án Bước 4: Tạo Security Group

Chạy: python project/step04_security_group.py --demo
      python project/step04_security_group.py --apply

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Tạo SG trong default VPC theo infra_config.yaml (ingress SSH/HTTP).
  2. Gắn tag dự án; lưu sg_id vào state.json.
  3. DRY-RUN mặc định; --apply tạo thật.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - dry_run_message với tên SG và rules.
  - --apply: "✅ Created sg-..." và cập nhật state.json.
═══════════════════════════════════════════════════════════════════════════
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import (
    get_context, handle_aws_error, load_infra_config,
    default_tags, dry_run_message, tag_dict,
)

MODULE_DIR = Path(__file__).parent.parent
STATE_FILE = MODULE_DIR / "data" / "state.json"


def create_security_group(apply: bool):
    config = load_infra_config(MODULE_DIR / "data" / "infra_config.yaml")
    ctx = get_context(config.get("region"))
    sg_config = config["security_group"]
    ec2 = ctx.session.client("ec2")

    vpc_id = ec2.describe_vpcs(Filters=[{"Name": "isDefault", "Values": ["true"]}])["Vpcs"][0]["VpcId"]

    dry_run_message(
        "Create Security Group",
        f"{sg_config['name']} in VPC {vpc_id}",
        apply,
    )

    for rule in sg_config["ingress"]:
        print(f"         Ingress: {rule['protocol']}:{rule['port']} from {rule['cidr']}")

    if not apply:
        return

    try:
        sg = ec2.create_security_group(
            GroupName=sg_config["name"],
            Description=sg_config["description"],
            VpcId=vpc_id,
            TagSpecifications=[{
                "ResourceType": "security-group",
                "Tags": default_tags() + [{"Key": "Name", "Value": sg_config["name"]}],
            }],
        )
        sg_id = sg["GroupId"]
    except ec2.exceptions.ClientError as e:
        if "InvalidGroup.Duplicate" in str(e):
            existing = ec2.describe_security_groups(
                Filters=[{"Name": "group-name", "Values": [sg_config["name"]]}]
            )["SecurityGroups"]
            sg_id = existing[0]["GroupId"]
            print(f"   ℹ️  SG đã tồn tại: {sg_id}")
        else:
            raise

    for rule in sg_config["ingress"]:
        try:
            ec2.authorize_security_group_ingress(
                GroupId=sg_id,
                IpPermissions=[{
                    "IpProtocol": rule["protocol"],
                    "FromPort": rule["port"],
                    "ToPort": rule["port"],
                    "IpRanges": [{"CidrIp": rule["cidr"], "Description": rule.get("description", "")}],
                }],
            )
        except ec2.exceptions.ClientError as e:
            if "InvalidPermission.Duplicate" not in str(e):
                raise

    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    state["security_group_id"] = sg_id
    STATE_FILE.write_text(json.dumps(state, indent=2))

    print(f"   ✅ Security Group: {sg_id}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    print("=== Bước 4: Security Group ===\n")
    try:
        create_security_group(apply=args.apply)
    except Exception as e:
        print(handle_aws_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

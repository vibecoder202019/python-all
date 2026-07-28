"""
Dự án Bước 5 — Launch EC2 instance
Chạy: python project/step05_ec2_instance.py --demo
      python project/step05_ec2_instance.py --apply
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import (
    get_context, handle_aws_error, load_infra_config,
    default_tags, dry_run_message,
)

MODULE_DIR = Path(__file__).parent.parent
STATE_FILE = MODULE_DIR / "data" / "state.json"


def find_latest_ami(ec2, pattern: str) -> str:
    amis = ec2.describe_images(
        Owners=["amazon"],
        Filters=[
            {"Name": "name", "Values": [pattern]},
            {"Name": "state", "Values": ["available"]},
        ],
    )["Images"]
    amis.sort(key=lambda x: x["CreationDate"], reverse=True)
    return amis[0]["ImageId"]


def launch_ec2(apply: bool):
    config = load_infra_config(MODULE_DIR / "data" / "infra_config.yaml")
    ctx = get_context(config.get("region"))
    ec2_config = config["ec2"]
    ec2 = ctx.session.client("ec2")

    ami_id = find_latest_ami(ec2, ec2_config["ami_name_pattern"])

    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    sg_id = state.get("security_group_id", "sg-DRYRUN")

    user_data_path = MODULE_DIR / "data" / "user_data.sh"
    user_data = user_data_path.read_text() if user_data_path.exists() else "#!/bin/bash\necho ready"

    dry_run_message(
        "Launch EC2",
        f"{ec2_config['instance_type']} | AMI {ami_id} | SG {sg_id}",
        apply,
    )

    if not apply:
        return

    if sg_id == "sg-DRYRUN":
        print("   ❌ Chạy step04 với --apply trước để tạo Security Group")
        return

    tags = default_tags() + [{"Key": "Name", "Value": "python-all-learn-ec2"}]

    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=ec2_config["instance_type"],
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=[sg_id],
        UserData=user_data,
        BlockDeviceMappings=[{
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "VolumeSize": ec2_config["volume_size_gb"],
                "VolumeType": "gp3",
                "DeleteOnTermination": True,
            },
        }],
        TagSpecifications=[{
            "ResourceType": "instance",
            "Tags": tags,
        }],
    )

    instance_id = response["Instances"][0]["InstanceId"]
    state["instance_id"] = instance_id
    STATE_FILE.write_text(json.dumps(state, indent=2))

    print(f"   ✅ Instance launched: {instance_id}")
    print(f"   ⏳ Chờ instance running...")
    waiter = ec2.get_waiter("instance_running")
    waiter.wait(InstanceIds=[instance_id], WaiterConfig={"Delay": 5, "MaxAttempts": 24})

    desc = ec2.describe_instances(InstanceIds=[instance_id])["Reservations"][0]["Instances"][0]
    public_ip = desc.get("PublicIpAddress", "N/A")
    print(f"   Public IP: {public_ip}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    print("=== Bước 5: Launch EC2 ===\n")
    try:
        launch_ec2(apply=args.apply)
    except Exception as e:
        print(handle_aws_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

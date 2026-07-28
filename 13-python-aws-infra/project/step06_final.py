"""
Dự án Bước 6 — AWS Infra Builder CLI hoàn chỉnh
Chạy: python project/step06_final.py --help
      python project/step06_final.py status
      python project/step06_final.py deploy --apply
      python project/step06_final.py destroy --apply
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import get_context, handle_aws_error, load_infra_config, PROJECT_TAG_KEY, PROJECT_TAG_VALUE

MODULE_DIR = Path(__file__).parent.parent
STATE_FILE = MODULE_DIR / "data" / "state.json"
VERSION = "1.0.0"


def cmd_status():
    ctx = get_context()
    ec2 = ctx.session.client("ec2")
    s3 = ctx.session.client("s3")

    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}

    print(f"=== AWS Infra Builder v{VERSION} ===")
    print(f"Account: {ctx.account_id}  Region: {ctx.region}\n")

    print("📁 State file:")
    for k, v in state.items():
        print(f"   {k}: {v}")

    tagged_instances = [
        i for r in ec2.describe_instances()["Reservations"]
        for i in r["Instances"]
        if i["State"]["Name"] != "terminated"
        and any(t["Key"] == PROJECT_TAG_KEY and t["Value"] == PROJECT_TAG_VALUE
                for t in i.get("Tags", []))
    ]
    print(f"\n🏷️  Tagged resources ({PROJECT_TAG_VALUE}):")
    print(f"   EC2: {len(tagged_instances)} instance(s)")
    for inst in tagged_instances:
        ip = inst.get("PublicIpAddress", "no public IP")
        print(f"     {inst['InstanceId']}  {inst['State']['Name']}  {ip}")

    if state.get("s3_bucket"):
        try:
            s3.head_bucket(Bucket=state["s3_bucket"])
            print(f"   S3:  s3://{state['s3_bucket']} ✅")
        except Exception:
            print(f"   S3:  s3://{state['s3_bucket']} ❌ not found")


def cmd_deploy(apply: bool):
    steps = [
        ("step03_create_s3.py", "S3 Bucket"),
        ("step04_security_group.py", "Security Group"),
        ("step05_ec2_instance.py", "EC2 Instance"),
    ]
    import subprocess
    for script, name in steps:
        print(f"\n── Deploy: {name} ──")
        args = ["python", str(Path(__file__).parent / script)]
        if apply:
            args.append("--apply")
        result = subprocess.run(args, capture_output=False)
        if result.returncode != 0:
            print(f"❌ Failed at: {name}")
            return
    print("\n✅ Deploy complete!" if apply else "\n✅ Dry-run complete!")


def cmd_destroy(apply: bool):
    if not apply:
        print("DRY-RUN — dùng: destroy --apply")
        import subprocess
        subprocess.run(["python", str(MODULE_DIR / "scripts" / "destroy_resources.py")])
        return
    import subprocess
    subprocess.run(["python", str(MODULE_DIR / "scripts" / "destroy_resources.py"), "--apply"])


def main():
    parser = argparse.ArgumentParser(prog="aws-infra-builder", description="AWS Infra Builder CLI")
    parser.add_argument("--version", action="version", version=f"aws-infra-builder {VERSION}")
    parser.add_argument("--demo", action="store_true")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="Xem trạng thái infra")
    p_deploy = sub.add_parser("deploy", help="Deploy stack (S3 + SG + EC2)")
    p_deploy.add_argument("--apply", action="store_true")
    p_destroy = sub.add_parser("destroy", help="Xóa tài nguyên")
    p_destroy.add_argument("--apply", action="store_true")

    args = parser.parse_args()

    try:
        if args.demo:
            cmd_status()
            print()
            cmd_deploy(apply=False)
        elif args.command == "status":
            cmd_status()
        elif args.command == "deploy":
            cmd_deploy(apply=args.apply)
        elif args.command == "destroy":
            cmd_destroy(apply=args.apply)
        else:
            parser.print_help()
    except Exception as e:
        print(handle_aws_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

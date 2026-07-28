"""
Module 13 — Ví dụ 6: Generate CloudFormation template từ Python

Chạy: python examples/06_generate_template.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Tạo dict CloudFormation template (S3 bucket, Security Group).
  2. Ghi ra data/generated/stack.yaml và stack.json.
  3. In summary Resources và Parameters.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - "Generated: .../stack.yaml" và ".../stack.json".
  - "Resources: LearnBucket, LearnSecurityGroup, ...".
  - "✓ Done".
═══════════════════════════════════════════════════════════════════════════
"""
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

MODULE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = MODULE_DIR / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_cfn_stack(name: str = "python-all-learn-stack") -> dict:
    """Tạo CloudFormation template cho stack học tập."""
    return {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Description": "Python All Learn — Demo infrastructure stack",
        "Parameters": {
            "InstanceType": {
                "Type": "String",
                "Default": "t3.micro",
                "AllowedValues": ["t3.micro", "t3.small"],
            },
        },
        "Resources": {
            "LearnBucket": {
                "Type": "AWS::S3::Bucket",
                "Properties": {
                    "BucketName": {"Fn::Sub": "${AWS::StackName}-artifacts-${AWS::AccountId}"},
                    "Tags": [{"Key": "Project", "Value": "python-all-learn"}],
                },
            },
            "LearnSecurityGroup": {
                "Type": "AWS::EC2::SecurityGroup",
                "Properties": {
                    "GroupDescription": "SG for python-all-learn",
                    "SecurityGroupIngress": [
                        {"IpProtocol": "tcp", "FromPort": 80, "ToPort": 80, "CidrIp": "0.0.0.0/0"},
                    ],
                    "Tags": [{"Key": "Project", "Value": "python-all-learn"}],
                },
            },
        },
        "Outputs": {
            "BucketName": {
                "Value": {"Ref": "LearnBucket"},
                "Export": {"Name": f"{name}-BucketName"},
            },
            "SecurityGroupId": {
                "Value": {"Ref": "LearnSecurityGroup"},
            },
        },
    }


def main():
    print("=== Generate Infrastructure Template ===\n")

    template = generate_cfn_stack()

    json_path = OUTPUT_DIR / "stack_template.json"
    json_path.write_text(json.dumps(template, indent=2), encoding="utf-8")
    print(f"1. CloudFormation JSON: {json_path}")

    if yaml:
        yaml_path = OUTPUT_DIR / "stack_template.yaml"
        yaml_path.write_text(yaml.dump(template, default_flow_style=False), encoding="utf-8")
        print(f"2. CloudFormation YAML: {yaml_path}")
    else:
        print("2. pip install pyyaml để export YAML")

    print(f"\n3. Deploy với AWS CLI:")
    print(f"   aws cloudformation create-stack \\")
    print(f"     --stack-name python-all-learn-stack \\")
    print(f"     --template-body file://{json_path}")

    print(f"\n4. IaC options:")
    print("   • CloudFormation — native AWS, YAML/JSON")
    print("   • Terraform — multi-cloud, HCL")
    print("   • CDK — Python/TypeScript → CloudFormation")
    print("   • boto3 — imperative, script automation")

    print("\n✓ Done")


if __name__ == "__main__":
    main()

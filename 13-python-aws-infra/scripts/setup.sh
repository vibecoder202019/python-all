#!/usr/bin/env bash
# Module 13 — Setup AWS environment (chạy 1 lần)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

echo "=== Module 13: Setup AWS Environment ==="

cd "$ROOT_DIR"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

pip install -q --upgrade pip
pip install -q boto3 pyyaml

mkdir -p "$MODULE_DIR/data"

cat > "$MODULE_DIR/data/infra_config.yaml" << 'EOF'
project: python-all-learn
region: ap-southeast-1

s3:
  bucket_prefix: python-all-learn-artifacts
  versioning: true

ec2:
  instance_type: t3.micro
  ami_name_pattern: "al2023-ami-2023*-x86_64"
  key_name: python-all-learn-key
  volume_size_gb: 8

security_group:
  name: python-all-learn-sg
  description: Security group for learning project
  ingress:
    - port: 22
      protocol: tcp
      cidr: "0.0.0.0/0"
      description: SSH (lab only)
    - port: 80
      protocol: tcp
      cidr: "0.0.0.0/0"
      description: HTTP

tags:
  Project: python-all-learn
  ManagedBy: python-all-learn
  Environment: learning
EOF

cat > "$MODULE_DIR/data/user_data.sh" << 'EOF'
#!/bin/bash
yum update -y
yum install -y python3 python3-pip
echo "Python All Learn — EC2 ready" > /var/www/html/index.html 2>/dev/null || \
  echo "Python All Learn — EC2 ready" > /home/ec2-user/ready.txt
EOF

echo "✓ boto3 installed"
echo "✓ Config: data/infra_config.yaml"
echo ""
echo "Kiểm tra credentials:"
echo "  bash scripts/check_credentials.sh"
echo ""
echo "Chạy tiếp:"
echo "  bash 13-python-aws-infra/scripts/run_all_examples.sh"
echo "  bash 13-python-aws-infra/scripts/run_project.sh"

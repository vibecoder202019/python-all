#!/usr/bin/env bash
# Kiểm tra AWS credentials
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || true

echo "=== AWS Credentials Check ==="

if command -v aws &>/dev/null; then
  echo "AWS CLI: $(aws --version 2>&1)"
  if aws sts get-caller-identity &>/dev/null; then
    aws sts get-caller-identity
    echo "✅ Credentials OK"
    exit 0
  fi
fi

python3 - << 'PY' 2>/dev/null && exit 0 || true
import boto3
from botocore.exceptions import NoCredentialsError
try:
    id = boto3.client("sts").get_caller_identity()
    print(f"Account: {id['Account']}")
    print(f"ARN:     {id['Arn']}")
    print("✅ Credentials OK (boto3)")
except NoCredentialsError:
    raise SystemExit(1)
PY

echo "❌ Chưa cấu hình AWS credentials"
echo ""
echo "Cấu hình bằng 1 trong các cách:"
echo "  aws configure"
echo "  export AWS_ACCESS_KEY_ID=..."
echo "  export AWS_SECRET_ACCESS_KEY=..."
echo "  export AWS_DEFAULT_REGION=ap-southeast-1"
exit 1

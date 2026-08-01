#!/usr/bin/env bash
# Module 15 — Cài môi trường AWX + MinIO + Python (chạy 1 lần)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

echo "=== Module 15: Setup AWX + MinIO + Python ==="

cd "$ROOT_DIR"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

pip install -q --upgrade pip
pip install -q requests boto3 pyyaml

mkdir -p "$MODULE_DIR/data"

cat > "$MODULE_DIR/data/awx.env.example" << 'EOF'
# Copy thành awx.env và điền token thật
AWX_URL=http://localhost:8052
AWX_TOKEN=your-awx-api-token-here
MINIO_ENDPOINT=http://localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin123
EOF

pip install -q requests boto3 pyyaml

echo "✓ Dependencies: requests, boto3"
echo "  (Tùy chọn AWX CLI: bash scripts/06-setup-awx-cli.sh)"
echo "  (Tùy chọn Terraform AWX: terraform/awx-client/)"
echo "✓ Sample config: data/awx.env.example"
echo ""
echo "Triển khai K8s (cần Docker Desktop K8s):"
echo "  bash 15-ansible-awx-minio-k8s/scripts/01-check-prerequisites.sh"
echo "  bash 15-ansible-awx-minio-k8s/scripts/02-deploy-minio.sh"
echo "  bash 15-ansible-awx-minio-k8s/scripts/03-deploy-awx-operator.sh"
echo "  bash 15-ansible-awx-minio-k8s/scripts/04-deploy-awx-instance.sh"
echo ""
echo "Chạy ví dụ Python (demo — không cần AWX):"
echo "  bash 15-ansible-awx-minio-k8s/scripts/run_all_examples.sh --demo"

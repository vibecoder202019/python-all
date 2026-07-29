#!/usr/bin/env bash
# Module 15 — Chạy tất cả examples tuần tự
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"
DEMO="${1:-}"

cd "$ROOT_DIR"
# shellcheck disable=SC1091
source .venv/bin/activate 2>/dev/null || true

echo "=== Module 15: Run All Examples ==="
echo ""

run() {
  local file="$1"
  shift
  echo "────────────────────────────────────────"
  echo "▶ $file"
  echo "────────────────────────────────────────"
  python "$MODULE_DIR/examples/$file" "$@"
  echo ""
}

if [ "$DEMO" = "--demo" ]; then
  run "01_awx_api_basics.py" 2>/dev/null || echo "(skip — cần AWX_TOKEN)"
  run "02_launch_job.py" --demo
  run "03_list_resources.py" --demo
  run "04_python_script_for_ansible.py" --name "Demo"
  run "05_minio_boto3.py" --demo
  run "06_full_pipeline.py" --demo
else
  run "04_python_script_for_ansible.py" --name "Module15"
  run "01_awx_api_basics.py" || echo "⚠️  01 skip — set AWX_TOKEN"
  run "02_launch_job.py" --demo
  run "03_list_resources.py" --demo
  run "05_minio_boto3.py" --demo || echo "⚠️  05 skip — cần MinIO"
  run "06_full_pipeline.py" --demo
fi

echo "✅ Hoàn tất examples"

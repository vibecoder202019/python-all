#!/usr/bin/env bash
# Module 15 — Chạy dự án 6 bước tuần tự
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"
DEMO="${1:---demo}"

cd "$ROOT_DIR"
# shellcheck disable=SC1091
source .venv/bin/activate 2>/dev/null || true

echo "=== Module 15: Run Project (6 steps) ==="
echo ""

for step in step01_awx_connect step02_launch_job step03_minio_upload \
            step04_ansible_script step05_monitor_job step06_final; do
  echo "────────────────────────────────────────"
  echo "▶ project/${step}.py"
  echo "────────────────────────────────────────"
  if [ "$step" = "step04_ansible_script" ]; then
    python "$MODULE_DIR/project/${step}.py" --name "Project"
  elif [ "$step" = "step06_final" ]; then
    python "$MODULE_DIR/project/${step}.py" pipeline --demo
  else
    python "$MODULE_DIR/project/${step}.py" "$DEMO"
  fi
  echo ""
done

echo "✅ Hoàn tất project 6 bước"
echo ""
echo "CLI hoàn chỉnh:"
echo "  python 15-ansible-awx-minio-k8s/project/step06_final.py --help"

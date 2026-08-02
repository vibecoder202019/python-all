#!/usr/bin/env bash
set -euo pipefail
MODULE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPATH="$MODULE_DIR/project${PYTHONPATH:+:$PYTHONPATH}"
export AWX_DEMO=true
cd "$MODULE_DIR"
echo "=== Module 28 examples (demo) ==="
for f in \
  01_awx_list_job_templates.py \
  02_awx_launch_job.py \
  03_bridge_create_deploy_task.py \
  04_backstage_catalog_entity.py \
  05_full_flow_demo.py
do
  echo ""
  echo "▶ examples/$f"
  python3 "examples/$f"
done
echo ""
echo "✓ All examples done"

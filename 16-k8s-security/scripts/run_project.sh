#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"
cd "$ROOT_DIR" && source .venv/bin/activate 2>/dev/null || true

echo "=== Module 16: Project 6 steps ==="
python "$MODULE_DIR/project/step01_sql_guard.py" --demo
python "$MODULE_DIR/project/step02_rate_limit.py"
python "$MODULE_DIR/project/step03_phishing_check.py"
python "$MODULE_DIR/project/step04_port_scan_detect.py"
python "$MODULE_DIR/project/step05_k8s_manifests.py"
python "$MODULE_DIR/project/step06_final.py" check-all --demo
echo "✅ Done — CLI: python project/step06_final.py --help"

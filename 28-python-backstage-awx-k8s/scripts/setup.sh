#!/usr/bin/env bash
set -euo pipefail
MODULE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$MODULE_DIR"
echo "=== Module 28 setup ==="
python3 -m pip install -q -r project/requirements.txt
cp -n data/.env.example data/.env 2>/dev/null || true
echo "✓ deps OK"
echo "  Next: bash scripts/01-check-prerequisites.sh"
echo "        bash scripts/02-run-all-examples.sh"
echo "        bash scripts/03-run-bridge.sh"

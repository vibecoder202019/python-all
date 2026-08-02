#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"

echo "=== Prerequisites Module 26 ==="
python3 --version
test -f "$MODULE_DIR/sample-app/app.py"
test -f "$MODULE_DIR/pipelines/github-actions/devsecops.yml"
test -f "$MODULE_DIR/policy/severity-gate.yaml"

echo "Optional tools:"
for t in gitleaks trivy docker syft; do
  if command -v "$t" >/dev/null 2>&1; then
    echo "  ✓ $t"
  else
    echo "  · $t (missing — stage sẽ skip)"
  fi
done
echo "✓ Core files OK"

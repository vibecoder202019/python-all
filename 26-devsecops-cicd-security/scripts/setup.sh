#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"
APP="$MODULE_DIR/sample-app"

cd "$ROOT_DIR"
echo "=== Module 26 setup ==="
[ ! -d .venv ] && python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
pip install -q --upgrade pip
pip install -q -r "$APP/requirements.txt" pytest httpx bandit pip-audit pyyaml
mkdir -p "$MODULE_DIR/reports"
echo "✓ Python scan tools ready (bandit, pip-audit)"
echo "  Optional CLI: brew install gitleaks trivy syft"
echo "  Next: bash 26-devsecops-cicd-security/scripts/02-run-local-pipeline.sh"

#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"
cd "$ROOT_DIR"

echo "=== Module 25 setup ==="
[ ! -d .venv ] && python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
pip install -q --upgrade pip
# stdlib-only module; ensure python works
python -c "import json, urllib.parse, html; print('stdlib OK')"
mkdir -p "$MODULE_DIR/data"
echo "✓ Ready"
echo "  bash 25-web-security-phishing-seo/scripts/02-run-all-examples.sh"
echo "  bash 25-web-security-phishing-seo/scripts/03-run-project.sh"

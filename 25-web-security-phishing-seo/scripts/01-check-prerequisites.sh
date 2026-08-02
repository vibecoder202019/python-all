#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

echo "=== Prerequisites Module 25 ==="
python3 --version
test -f "$MODULE_DIR/project/common.py"
test -f "$MODULE_DIR/data/sample_urls.txt"
test -f "$MODULE_DIR/data/gsc_fixture_compromised.json"
echo "✓ Files OK"
echo "Ethics: lab phòng thủ — không tấn công site / SEO bên thứ ba."

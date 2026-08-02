#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
rm -rf "$MODULE_DIR/reports"
mkdir -p "$MODULE_DIR/reports"
echo "✓ Cleared reports/"
docker rmi devsecops-lab-app:local 2>/dev/null || true

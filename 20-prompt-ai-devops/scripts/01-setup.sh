#!/usr/bin/env bash
# Setup Module 20 — tạo thư mục notes, kiểm tra Python
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$ROOT/notes"
python3 --version
echo "Module 20 ready. Open: $ROOT/README.md"
echo "Templates: $ROOT/prompts/templates/rcto-base.md"

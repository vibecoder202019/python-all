#!/usr/bin/env bash
# Chạy lab: bash scripts/02-run-lab.sh basic 01
set -euo pipefail
LEVEL="${1:?Usage: $0 basic|intermediate|advanced LAB_NUM}"
NUM="${2:?Usage: $0 basic 01}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(dirname "$SCRIPT_DIR")/labs/${LEVEL}"
LAB_FILE=$(ls "$LAB_DIR"/lab${NUM}-*.md 2>/dev/null | head -1)

if [ -z "$LAB_FILE" ]; then
  echo "❌ Không tìm thấy lab ${NUM} trong ${LEVEL}/"
  exit 1
fi

echo "=== Lab ${NUM} (${LEVEL}) ==="
echo "File: $LAB_FILE"
echo ""
echo "Mở file lab và làm theo từng bước."
echo "Verify: bash scripts/03-verify-lab.sh ${NUM}"
echo ""
head -40 "$LAB_FILE"

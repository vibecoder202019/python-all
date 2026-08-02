#!/usr/bin/env bash
# Helper — kiểm tra nhanh site CỦA BẠN (headers + gợi ý tool).
# Usage: TARGET=https://staging.example.com bash scripts/04-self-check-headers.sh
set -euo pipefail

TARGET="${TARGET:-}"
if [[ -z "$TARGET" ]]; then
  echo "Usage: TARGET=https://staging.YOUR_DOMAIN bash $0"
  echo "Chỉ dùng domain bạn sở hữu / được ủy quyền."
  exit 1
fi

echo "=== Self-check headers: $TARGET ==="
echo "Xác nhận bạn có quyền test URL này trước khi tiếp tục."
echo ""

curl -sI --max-time 15 "$TARGET" | tee /tmp/m25-headers.txt
echo ""
echo "--- Security-related headers ---"
grep -iE '^(strict-transport-security|content-security-policy|x-frame-options|x-content-type-options|referrer-policy|permissions-policy):' /tmp/m25-headers.txt \
  || echo "(chưa thấy header bảo mật phổ biến — cân nhắc thêm HSTS/CSP/X-Frame-Options)"

echo ""
echo "Tiếp theo (tuỳ chọn):"
echo "  lighthouse \"$TARGET\" --view"
echo "  nuclei -u \"$TARGET\" -severity http/misconfiguration -rate-limit 50"
echo "  # ZAP baseline — xem docs/03-authorized-self-assessment.md"
echo "  bash scripts/02-run-all-examples.sh"

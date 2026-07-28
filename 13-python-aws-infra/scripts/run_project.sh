#!/usr/bin/env bash
# Chạy dự án AWS Infra Builder — 6 bước tuần tự
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

APPLY=""
if [[ "${1:-}" == "--apply" ]]; then
  APPLY="--apply"
  echo "⚠️  MODE: APPLY — sẽ tạo tài nguyên thật trên AWS!"
  read -r -p "Nhập 'yes' để xác nhận: " confirm
  [[ "$confirm" == "yes" ]] || { echo "Đã hủy."; exit 1; }
else
  echo "MODE: DRY-RUN (thêm --apply để tạo thật)"
fi

STEPS=(
  "step01_aws_connect.py"
  "step02_list_resources.py"
  "step03_create_s3.py"
  "step04_security_group.py"
  "step05_ec2_instance.py"
  "step06_final.py"
)

echo "=== AWS Infra Builder — 6 bước ==="
echo ""

for i in "${!STEPS[@]}"; do
  step="${STEPS[$i]}"
  num=$((i + 1))
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  Bước $num/6: $step"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  python "$MODULE_DIR/project/$step" --demo $APPLY 2>/dev/null || \
    python "$MODULE_DIR/project/$step" $APPLY
  echo ""
done

echo "🎉 Hoàn thành AWS Infra Builder!"
if [[ -n "$APPLY" ]]; then
  echo "⚠️  Nhớ xóa tài nguyên: bash scripts/destroy_infra.sh --apply"
fi

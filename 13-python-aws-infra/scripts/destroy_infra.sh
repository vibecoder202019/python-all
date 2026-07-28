#!/usr/bin/env bash
# Xóa tài nguyên AWS có tag Project=python-all-learn
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

if [[ "${1:-}" != "--apply" ]]; then
  echo "DRY-RUN — chỉ liệt kê tài nguyên sẽ xóa"
  echo "Thêm --apply để xóa thật: bash scripts/destroy_infra.sh --apply"
  python "$MODULE_DIR/scripts/destroy_resources.py"
  exit 0
fi

echo "⚠️  Sẽ XÓA tài nguyên có tag Project=python-all-learn"
read -r -p "Nhập 'yes' để xác nhận: " confirm
[[ "$confirm" == "yes" ]] || { echo "Đã hủy."; exit 1; }

python "$MODULE_DIR/scripts/destroy_resources.py" --apply

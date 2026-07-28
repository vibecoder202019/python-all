#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

STEPS=(
  "step01_schema.sql"
  "step02_seed_data.sql"
  "step03_functions.sql"
  "step04_triggers.sql"
  "step05_views.sql"
  "step06_final.sql"
)

echo "=== Dự án Thư viện Sách — 6 bước ==="

python "$SCRIPT_DIR/run_sql.py" "$MODULE_DIR/project/00_reset_library.sql" 2>/dev/null || true

for i in "${!STEPS[@]}"; do
  step="${STEPS[$i]}"
  num=$((i + 1))
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  Bước $num/6: $step"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  python "$SCRIPT_DIR/run_sql.py" "$MODULE_DIR/project/$step"
done

echo ""
echo "🎉 Database Thư viện hoàn chỉnh!"
echo "   psql: bash scripts/psql_shell.sh"
echo "   Demo: SELECT * FROM v_overdue_loans;"

#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

EXAMPLES=(
  "01_sql_co_ban.sql|CRUD + UPDATE 10% → mong đợi 5 sách, thống kê"
  "02_joins_aggregation.sql|JOIN + HAVING → mong đợi NNÁ/Murakami=2 sách"
  "03_functions_plpgsql.sql|4 function → mong đợi NNÁ=2 sách, tổng kho"
  "04_triggers.sql|Trigger audit → mong đợi audit_log có UPDATE"
  "05_views_indexes.sql|View + Index → mong đợi 3 tác giả, 2 members"
)

echo "=== Chạy ví dụ PostgreSQL (Module 14) ==="
echo "Mỗi file in ra: YÊU CẦU + KẾT QUẢ MONG ĐỢI — đối chiếu output với bảng trong file"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "▶ Ví dụ 00: Reset schema demo"
python "$SCRIPT_DIR/run_sql.py" "$MODULE_DIR/examples/00_reset_demo.sql"

for entry in "${EXAMPLES[@]}"; do
  ex="${entry%%|*}"
  desc="${entry#*|}"
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "▶ ${ex} — ${desc}"
  python "$SCRIPT_DIR/run_sql.py" "$MODULE_DIR/examples/$ex"
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "▶ Ví dụ 06: Python psycopg2 — JOIN, function, transaction"
python "$MODULE_DIR/examples/06_python_psycopg2.py"

echo ""
echo "✓ Hoàn thành! Đối chiếu output với 'KẾT QUẢ MONG ĐỢI' trong từng file."
echo "  Tiếp: bash scripts/run_project.sh"

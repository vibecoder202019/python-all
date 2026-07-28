#!/usr/bin/env bash
# Module 14 — Setup PostgreSQL via Docker (chạy 1 lần)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

echo "=== Module 14: Setup PostgreSQL ==="

cd "$ROOT_DIR"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install -q --upgrade pip
pip install -q psycopg2-binary

cd "$MODULE_DIR"

if ! command -v docker &>/dev/null; then
  echo "❌ Docker chưa cài. Cài Docker Desktop: https://docker.com/products/docker-desktop"
  exit 1
fi

echo "Khởi động PostgreSQL container..."
docker compose up -d

echo "Chờ PostgreSQL sẵn sàng..."
for i in $(seq 1 30); do
  if docker compose exec -T postgres pg_isready -U learn_user -d learn_db &>/dev/null; then
    echo "✓ PostgreSQL ready!"
    break
  fi
  sleep 1
  if [ "$i" -eq 30 ]; then
    echo "❌ Timeout waiting for PostgreSQL"
    exit 1
  fi
done

echo ""
echo "Kết nối:"
echo "  Host: localhost:5433  DB: learn_db  User: learn_user  Pass: learn_pass"
echo ""
echo "Chạy tiếp:"
echo "  bash 14-postgresql-tu-hoc/scripts/run_all_examples.sh"
echo "  bash 14-postgresql-tu-hoc/scripts/run_project.sh"
echo "  bash 14-postgresql-tu-hoc/scripts/psql_shell.sh"

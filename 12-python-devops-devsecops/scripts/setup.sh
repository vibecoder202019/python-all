#!/usr/bin/env bash
# Module 12 — Cài môi trường DevOps (chạy 1 lần)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

echo "=== Module 12: Setup DevOps Environment ==="

cd "$ROOT_DIR"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

pip install -q --upgrade pip
pip install -q pyyaml httpx python-dotenv

# Tạo sample data cho demo
mkdir -p "$MODULE_DIR/data"
cat > "$MODULE_DIR/data/sample.log" << 'EOF'
[2024-01-15 10:00:01] INFO: Server started on port 8000
[2024-01-15 10:00:05] INFO: Database connected
[2024-01-15 10:01:23] WARNING: High memory usage: 85%
[2024-01-15 10:02:45] ERROR: Connection timeout to redis:6379
[2024-01-15 10:03:10] INFO: Retry successful
[2024-01-15 10:05:00] ERROR: Failed to process request id=12345
[2024-01-15 10:06:30] WARNING: Disk usage above 80%
[2024-01-15 10:10:00] INFO: Health check passed
[2024-01-15 10:15:22] ERROR: Authentication failed for user admin
[2024-01-15 10:20:00] INFO: Scheduled backup completed
EOF

cat > "$MODULE_DIR/data/config.yaml" << 'EOF'
app:
  name: demo-api
  port: 8000
  env: staging
services:
  - name: api
    url: http://localhost:8000
    health: /health
  - name: redis
    host: localhost
    port: 6379
EOF

cat > "$MODULE_DIR/data/.env.example" << 'EOF'
API_KEY=demo-key-not-real
DATABASE_URL=postgresql://user:pass@localhost/db
EOF

echo "✓ Dependencies installed"
echo "✓ Sample data created in data/"
echo ""
echo "Chạy tiếp:"
echo "  bash 12-python-devops-devsecops/scripts/run_all_examples.sh"
echo "  bash 12-python-devops-devsecops/scripts/run_project.sh"

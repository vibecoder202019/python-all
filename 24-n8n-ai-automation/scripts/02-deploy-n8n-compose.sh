#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
COMPOSE_DIR="$MODULE_DIR/docker-compose"
WITH_OLLAMA=0

for arg in "$@"; do
  [[ "$arg" == "--with-ollama" ]] && WITH_OLLAMA=1
done

echo "=== Deploy n8n (Docker Compose) ==="
command -v docker >/dev/null || { echo "Cần Docker Desktop"; exit 1; }

cd "$COMPOSE_DIR"
cp -n .env.example .env 2>/dev/null || true

if [[ "$WITH_OLLAMA" -eq 1 ]]; then
  echo "Kèm Ollama (AI miễn phí)..."
  docker compose --profile ollama up -d
  echo "Chờ Ollama..."
  sleep 5
  docker exec ollama-lab ollama pull "${OLLAMA_MODEL:-llama3.2:1b}" || true
  echo "Ollama: http://localhost:11434"
else
  docker compose up -d n8n
fi

echo ""
echo "✓ n8n UI: http://localhost:5678"
echo "  User: admin / Pass: n8n-lab-pass"
echo ""
echo "Ollama trên host (khuyến nghị): ollama serve && ollama pull llama3.2:1b"
echo "Hoặc deploy kèm Docker: bash scripts/02-deploy-n8n-compose.sh --with-ollama"

#!/usr/bin/env bash
# Dung Terrakube docker compose stack
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COMPOSE_DIR="$ROOT/.cache/terrakube-upstream/docker-compose"

if [[ ! -d "$COMPOSE_DIR" ]]; then
  echo "Chua deploy — khong co $COMPOSE_DIR"
  exit 1
fi

cd "$COMPOSE_DIR"
docker compose down -v
echo "Da teardown Terrakube compose."
echo "Network terrakube-network giu lai — xoa: docker network rm terrakube-network"

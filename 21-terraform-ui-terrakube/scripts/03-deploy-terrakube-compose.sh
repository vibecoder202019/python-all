#!/usr/bin/env bash
# Clone Terrakube upstream + mkcert + docker compose up
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CACHE="$ROOT/.cache/terrakube-upstream"
REPO="${TERRAKUBE_REPO:-https://github.com/terrakube-io/terrakube.git}"
BRANCH="${TERRAKUBE_BRANCH:-main}"

echo "=== Deploy Terrakube Docker Compose ==="

# Docker network
if ! docker network inspect terrakube-network &>/dev/null; then
  echo "Tao docker network terrakube-network..."
  docker network create terrakube-network \
    -d bridge \
    --subnet 10.25.25.0/24 \
    --gateway 10.25.25.254
fi

# Clone / update
if [[ ! -d "$CACHE/.git" ]]; then
  mkdir -p "$ROOT/.cache"
  git clone --depth 1 --branch "$BRANCH" "$REPO" "$CACHE"
else
  echo "Repo da co tai $CACHE (bo qua pull — xoa .cache de clone lai)"
fi

COMPOSE_DIR="$CACHE/docker-compose"
if [[ ! -f "$COMPOSE_DIR/docker-compose.yaml" && ! -f "$COMPOSE_DIR/docker-compose.yml" ]]; then
  echo "Khong tim thay docker-compose trong $COMPOSE_DIR"
  exit 1
fi

cd "$COMPOSE_DIR"

echo "Tao HTTPS certificates (mkcert)..."
mkcert -install 2>/dev/null || true
mkcert -key-file key.pem -cert-file cert.pem platform.local "*.platform.local"
CAROOT_PATH="$(mkcert -CAROOT)/rootCA.pem"
cp "$CAROOT_PATH" rootCA.pem

echo "Docker compose up..."
docker compose up -d --force-recreate

echo ""
echo "=== Deploy xong ==="
echo "Doi 1-2 phut: bash $ROOT/scripts/04-wait-healthy.sh"
echo "UI: https://terrakube.platform.local"
echo "Login: admin@example.com / admin"
echo "Logs: cd $COMPOSE_DIR && docker compose logs -f"

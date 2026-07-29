#!/usr/bin/env bash
# Kiểm tra Docker, mkcert, git cho Terrakube lab
set -euo pipefail

ok=0
check() {
  if command -v "$1" &>/dev/null; then
    echo "  OK   $1 — $(eval "$2" 2>/dev/null | head -1 || echo present)"
  else
    echo "  MISS $1"
    ok=1
  fi
}

echo "=== Module 21 — Prerequisites ==="
check docker "docker --version"
check git "git --version"
check mkcert "mkcert -version"
if docker compose version &>/dev/null; then
  echo "  OK   docker compose — $(docker compose version | head -1)"
else
  echo "  MISS docker compose"
  ok=1
fi

if [[ $ok -ne 0 ]]; then
  echo ""
  echo "Cài thiếu:"
  echo "  macOS: brew install mkcert nss && mkcert -install"
  echo "  Docker Desktop: https://www.docker.com/products/docker-desktop/"
  exit 1
fi
echo ""
echo "San sang deploy Terrakube. Tiep: scripts/02-prepare-hosts.sh --print"

#!/usr/bin/env bash
# Module 17 — Build Docker image
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT="$(dirname "$SCRIPT_DIR")/project"
IMAGE="${IMAGE:-go-task-api:latest}"

echo "=== Build Docker image: $IMAGE ==="
docker build -t "$IMAGE" "$PROJECT"
echo "✅ docker images | grep go-task-api"

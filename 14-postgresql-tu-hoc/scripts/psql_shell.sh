#!/usr/bin/env bash
# Mở psql shell tương tác
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"

cd "$MODULE_DIR"
docker compose exec postgres psql -U learn_user -d learn_db

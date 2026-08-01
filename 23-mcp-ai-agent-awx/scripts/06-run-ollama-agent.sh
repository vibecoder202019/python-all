#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate"
set -a
[ -f "$MODULE_DIR/config/.env" ] && source "$MODULE_DIR/config/.env"
set +a

exec python "$MODULE_DIR/ai-agent/ollama_agent.py" "$@"

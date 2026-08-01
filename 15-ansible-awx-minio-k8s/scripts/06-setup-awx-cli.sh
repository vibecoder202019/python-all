#!/usr/bin/env bash
# Cai awxkit (awx CLI) + huong dan config
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

MODE="${1:-install}"

install_cli() {
  cd "$ROOT_DIR"
  [ -d .venv ] || python3 -m venv .venv
  # shellcheck disable=SC1091
  source .venv/bin/activate
  pip install -q --upgrade pip awxkit
  echo "OK awx $(awx --version 2>/dev/null || awx --help | head -1)"
  echo ""
  echo "Config mau: $MODULE_DIR/awx-cli/credentials.example"
  echo "Doc: $MODULE_DIR/docs/07-awx-client-cli-terraform.md"
}

test_cli() {
  if ! command -v awx &>/dev/null; then
    echo "Chua cai awx — chay: $0 install"
    exit 1
  fi
  : "${AWX_HOST:?Set AWX_HOST=http://localhost:8052}"
  : "${AWX_TOKEN:?Set AWX_TOKEN from AWX UI}"
  export AWX_VERIFY_SSL="${AWX_VERIFY_SSL:-false}"
  echo "=== awx ping ==="
  awx ping
  echo ""
  echo "=== awx me ==="
  awx me
  echo ""
  echo "=== job templates ==="
  awx job_templates list -f json | head -c 2000
  echo ""
}

case "$MODE" in
  install) install_cli ;;
  --test)  test_cli ;;
  *)
    echo "Usage: $0 [install|--test]"
    exit 1
    ;;
esac

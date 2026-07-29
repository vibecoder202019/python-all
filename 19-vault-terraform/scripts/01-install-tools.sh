#!/usr/bin/env bash
# Cai dat / kiem tra Terraform + Vault + jq
set -euo pipefail

MODE="${1:---check}"

check_cmd() {
  if command -v "$1" &>/dev/null; then
    echo "  OK  $1 — $($1 --version 2>&1 | head -1 || $1 version 2>&1 | head -1)"
    return 0
  else
    echo "  MISS $1"
    return 1
  fi
}

do_check() {
  echo "=== Kiem tra cong cu Module 19 ==="
  local ok=0
  check_cmd terraform || ok=1
  check_cmd vault || ok=1
  check_cmd jq || ok=1
  if [[ $ok -eq 0 ]]; then
    echo ""
    echo "San sang hoc Vault + Terraform!"
  else
    echo ""
    echo "Thieu cong cu. Chay: $0 --install (macOS Homebrew)"
    exit 1
  fi
}

do_install() {
  if [[ "$(uname -s)" != "Darwin" ]]; then
    echo "Auto-install chi ho tro macOS (Homebrew)."
    echo "Linux: xem docs/01-cai-dat.md"
    exit 1
  fi
  if ! command -v brew &>/dev/null; then
    echo "Can cai Homebrew truoc: https://brew.sh"
    exit 1
  fi
  brew tap hashicorp/tap
  brew install hashicorp/tap/terraform hashicorp/tap/vault jq
  do_check
}

case "$MODE" in
  --check)  do_check ;;
  --install) do_install ;;
  *) echo "Usage: $0 [--check|--install]"; exit 1 ;;
esac

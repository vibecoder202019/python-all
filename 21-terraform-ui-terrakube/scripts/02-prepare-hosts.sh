#!/usr/bin/env bash
# Huong dan / kiem tra /etc/hosts cho Terrakube local domains
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOSTS_FILE="$ROOT/config/hosts-entries.txt"
MODE="${1:---print}"

check_hosts() {
  local missing=0
  while read -r line; do
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    local host
    host=$(echo "$line" | awk '{print $2}')
    if grep -q "$host" /etc/hosts 2>/dev/null; then
      echo "  OK   $host"
    else
      echo "  MISS $host"
      missing=1
    fi
  done < "$HOSTS_FILE"
  return $missing
}

case "$MODE" in
  --print)
    echo "=== Them vao /etc/hosts ==="
    cat "$HOSTS_FILE"
    echo ""
    echo "macOS/Linux:"
    echo "  sudo sh -c 'cat $HOSTS_FILE >> /etc/hosts'"
    echo ""
    echo "Kiem tra: $0 --check"
    ;;
  --check)
    echo "=== Kiem tra /etc/hosts ==="
    if check_hosts; then
      echo "Hosts OK"
    else
      echo "Chua du entries — chay --print"
      exit 1
    fi
    ;;
  *)
    echo "Usage: $0 [--print|--check]"
    exit 1
    ;;
esac

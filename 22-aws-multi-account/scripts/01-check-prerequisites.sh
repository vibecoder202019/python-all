#!/usr/bin/env bash
set -euo pipefail
echo "=== Module 22 Prerequisites ==="
ok=0
check() { command -v "$1" &>/dev/null && echo "  OK $1" || { echo "  MISS $1"; ok=1; }; }
check aws
check terraform
check jq
if aws sts get-caller-identity &>/dev/null; then
  echo "  OK AWS credentials"
  aws sts get-caller-identity
else
  echo "  MISS AWS credentials — aws configure"
  ok=1
fi
[[ $ok -eq 0 ]] || exit 1
echo "San sang lab multi-account."

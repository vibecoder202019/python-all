#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT="$(dirname "$MODULE_DIR")"
echo "=== Prerequisites Module 27 ==="
python3 --version
test -f "$MODULE_DIR/templates/ADR-template.md"
test -f "$MODULE_DIR/data/governance_fixture.json"
echo "Recommended prior modules (presence check):"
for m in 12-python-devops-devsecops 13-python-aws-infra 19-vault-terraform 22-aws-multi-account 26-devsecops-cicd-security; do
  if [[ -d "$ROOT/$m" ]]; then echo "  ✓ $m"; else echo "  · $m (missing — vẫn học lý thuyết được)"; fi
done
echo "✓ OK"

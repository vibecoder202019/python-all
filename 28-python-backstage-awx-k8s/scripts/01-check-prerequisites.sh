#!/usr/bin/env bash
set -euo pipefail
MODULE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ok=0
fail=0
check() {
  if "$@"; then echo "✓ $*"; ok=$((ok+1)); else echo "✗ $*"; fail=$((fail+1)); fi
}
echo "=== Module 28 prerequisites ==="
command -v python3 >/dev/null && echo "✓ python3" || { echo "✗ python3"; fail=$((fail+1)); }
python3 -c "import requests, fastapi, yaml" 2>/dev/null && echo "✓ python deps" || echo "⚠ pip install -r project/requirements.txt"
test -f "$MODULE_DIR/data/awx_fixture.json" && echo "✓ AWX fixture"
test -f "$MODULE_DIR/project/bridge_server.py" && echo "✓ bridge_server"
test -f "$MODULE_DIR/backstage/template.yaml" && echo "✓ Backstage template"
test -f "$MODULE_DIR/terraform/main.tf" && echo "✓ Terraform"
test -f "$MODULE_DIR/ansible/deploy-app.yml" && echo "✓ Ansible playbook"
test -f "$MODULE_DIR/k8s/demo-app.yaml" && echo "✓ K8s manifests"
command -v terraform >/dev/null && echo "✓ terraform CLI" || echo "⚠ terraform optional"
command -v kubectl >/dev/null && echo "✓ kubectl" || echo "⚠ kubectl optional (lab K8s)"
command -v ansible-playbook >/dev/null && echo "✓ ansible" || echo "⚠ ansible optional"
echo "Live AWX: set AWX_URL + AWX_TOKEN in data/.env"
echo "Demo: AWX_DEMO=true (default khi thiếu URL)"
exit 0

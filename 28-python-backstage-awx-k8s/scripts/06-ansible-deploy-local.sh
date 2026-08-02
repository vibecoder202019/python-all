#!/usr/bin/env bash
# Chạy Ansible playbook local (giống AWX sẽ chạy) — cần kubectl + ansible + kubernetes collection.
set -euo pipefail
MODULE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
command -v ansible-playbook >/dev/null || { echo "pip/ansible: ansible-playbook"; exit 1; }
command -v kubectl >/dev/null || { echo "Cần kubectl"; exit 1; }

ansible-galaxy collection install kubernetes.core >/dev/null 2>&1 || true

cd "$MODULE_DIR/ansible"
ansible-playbook -i inventory/localhost.ini deploy-app.yml \
  -e app_name="${APP_NAME:-demo-api}" \
  -e namespace="${NAMESPACE:-platform-apps}" \
  -e image="${IMAGE:-nginx:1.27-alpine}" \
  -e replicas="${REPLICAS:-2}"

kubectl get deploy,svc -n "${NAMESPACE:-platform-apps}"
echo "✓ Ansible deploy xong"

#!/usr/bin/env bash
# Module 17 — Kiểm tra Go + Helm
set -euo pipefail
echo "=== Module 17: Prerequisites ==="
command -v go &>/dev/null && go version && echo "✅ Go" || echo "❌ Cài Go: https://go.dev/dl/"
command -v docker &>/dev/null && echo "✅ Docker" || echo "⚠️  Docker (cần build image)"
command -v kubectl &>/dev/null && echo "✅ kubectl" || echo "⚠️  kubectl"
command -v helm &>/dev/null && helm version --short && echo "✅ Helm" || echo "⚠️  helm install: brew install helm"

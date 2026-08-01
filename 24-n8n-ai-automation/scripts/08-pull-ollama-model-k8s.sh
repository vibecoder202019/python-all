#!/usr/bin/env bash
set -euo pipefail
MODEL="${OLLAMA_MODEL:-llama3.2:1b}"
echo "=== Pull Ollama model trên K8s: $MODEL ==="
kubectl exec -n ai-automation deploy/ollama -- ollama pull "$MODEL"
kubectl exec -n ai-automation deploy/ollama -- ollama list

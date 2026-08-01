#!/usr/bin/env bash
# Cài / kiểm tra Ollama — AI miễn phí local
set -euo pipefail

echo "=== Ollama (free local AI) ==="

if command -v ollama &>/dev/null; then
  echo "✓ ollama CLI: $(ollama --version 2>/dev/null || ollama -v)"
else
  echo "Ollama chưa cài."
  echo ""
  echo "macOS:"
  echo "  brew install ollama"
  echo "  hoặc tải: https://ollama.com/download"
  echo ""
  echo "Linux:"
  echo "  curl -fsSL https://ollama.com/install.sh | sh"
  echo ""
  echo "Docker (Module 24 compose có service ollama):"
  echo "  bash 24-n8n-ai-automation/scripts/02-deploy-n8n-compose.sh --with-ollama"
  exit 1
fi

if curl -sf http://localhost:11434/api/tags >/dev/null 2>&1; then
  echo "✓ Ollama server đang chạy"
else
  echo "⚠ Ollama server chưa chạy — mở terminal: ollama serve"
fi

MODEL="${OLLAMA_MODEL:-llama3.2:1b}"
echo ""
echo "Pull model (lần đầu ~1GB, miễn phí):"
echo "  ollama pull $MODEL"
echo ""
read -r -p "Pull $MODEL ngay? [y/N] " ans
if [[ "${ans:-}" =~ ^[yY] ]]; then
  ollama pull "$MODEL"
fi

echo ""
echo "Test:"
echo "  ollama run $MODEL 'Xin chào'"
echo "  python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --once 'list awx templates'"

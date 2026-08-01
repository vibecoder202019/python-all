# Ollama — AI Agent miễn phí (không Cursor, không API key)

**Ollama** chạy LLM **local, 100% miễn phí** trên máy bạn. Module 23 dùng Ollama làm "bộ não" — hiểu câu chat → gọi AWX.

---

## Cài Ollama

### macOS

```bash
brew install ollama
ollama serve          # terminal 1 — giữ chạy
ollama pull llama3.2:1b   # model nhẹ, miễn phí (~1.3GB)
```

### Docker (cùng stack n8n Module 24)

```bash
bash 24-n8n-ai-automation/scripts/02-deploy-n8n-compose.sh --with-ollama
export OLLAMA_URL=http://localhost:11434
```

### Script lab

```bash
bash 23-mcp-ai-agent-awx/scripts/02-install-ollama.sh
```

---

## Chạy AI Agent chat

```bash
cd learn-python-ai
source .venv/bin/activate
export AWX_DEMO_MODE=1

# Chat tương tác
bash 23-mcp-ai-agent-awx/scripts/06-run-ollama-agent.sh

# Một câu
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --once "Liệt kê job template AWX"
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --once "Chạy job Python Hello World"
```

**Không có Ollama?** Dùng `--demo` hoặc `AWX_DEMO_MODE=1`.

---

## AWX thật (sau Module 15)

```bash
kubectl port-forward svc/awx-service 8052:80 -n awx
export AWX_URL=http://localhost:8052
export AWX_TOKEN=your-token
export AWX_DEMO_MODE=0
bash scripts/06-run-ollama-agent.sh
```

---

## Bridge API + Ollama (cho n8n)

Bridge endpoint **`POST /agent/chat`** — gửi câu tự nhiên, Ollama parse intent:

```bash
curl -X POST http://localhost:8090/agent/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: lab-bridge-key" \
  -d '{"message":"List all AWX job templates"}'
```

Response gồm `parsed_intent` + `result` từ AWX.

---

## Model gợi ý (miễn phí)

| Model | RAM | Ghi chú |
|-------|-----|---------|
| `llama3.2:1b` | ~2 GB | Mặc định lab, nhanh |
| `llama3.2:3b` | ~4 GB | Hiểu intent tốt hơn |
| `phi3:mini` | ~3 GB | Alternative |
| `gemma2:2b` | ~3 GB | Alternative |

Đổi model: `export OLLAMA_MODEL=llama3.2:3b`

---

## So sánh: Ollama vs Cursor MCP

| | **Ollama (khuyến nghị)** | Cursor MCP (tùy chọn) |
|---|--------------------------|------------------------|
| Chi phí | Miễn phí | Cần Cursor |
| Chạy ở đâu | Local / Docker | IDE |
| n8n tích hợp | `/agent/chat` | Khó hơn |
| Doc | File này | [optional-cursor-mcp.md](optional-cursor-mcp.md) |

---

**Tiếp:** [lab03-ollama-agent.md](../labs/intermediate/lab03-ollama-agent.md) → Module 24 n8n

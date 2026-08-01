# Hướng dẫn Manual — Module 23 (Ollama free AI)

> **Không cần Cursor.** AI miễn phí = **Ollama** local.

## Phần A — Cài Ollama

```bash
brew install ollama
ollama serve
```

Terminal mới:

```bash
ollama pull llama3.2:1b
ollama run llama3.2:1b "Xin chào"
```

Hoặc:

```bash
bash learn-python-ai/23-mcp-ai-agent-awx/scripts/02-install-ollama.sh
```

## Phần B — Setup Python

```bash
cd learn-python-ai
bash 23-mcp-ai-agent-awx/scripts/setup.sh
cp 23-mcp-ai-agent-awx/config/.env.example 23-mcp-ai-agent-awx/config/.env
export AWX_DEMO_MODE=1
export OLLAMA_MODEL=llama3.2:1b
```

## Phần C — Chat agent (free AI)

```bash
bash 23-mcp-ai-agent-awx/scripts/06-run-ollama-agent.sh
```

Hoặc một câu:

```bash
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --once "Liệt kê job template AWX"
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --once "Chạy job Python Hello World"
```

Demo không Ollama:

```bash
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --demo --once "list templates"
```

## Phần D — Bridge + Ollama (cho n8n)

Terminal 1:

```bash
bash 23-mcp-ai-agent-awx/scripts/04-run-agent-bridge.sh
```

Terminal 2:

```bash
curl http://localhost:8090/health
curl -X POST http://localhost:8090/agent/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: lab-bridge-key" \
  -d '{"message":"List AWX templates"}'
```

## Phần E — AWX thật (Module 15)

```bash
kubectl port-forward svc/awx-service 8052:80 -n awx
export AWX_URL=http://localhost:8052
export AWX_TOKEN=PASTE_TOKEN
export AWX_DEMO_MODE=0
bash 23-mcp-ai-agent-awx/scripts/06-run-ollama-agent.sh
```

## Phần F — Module 24 n8n

```bash
bash 24-n8n-ai-automation/scripts/02-deploy-n8n-compose.sh
# Import workflows/05-ollama-ai-chat-awx.json
```

## (Tùy chọn) Cursor MCP

Chỉ nếu bạn muốn — xem `docs/optional-cursor-mcp.md`

# Ollama + AWX + n8n

## Ollama (free AI)

```bash
ollama serve
ollama pull llama3.2:1b
export OLLAMA_URL=http://localhost:11434
export OLLAMA_MODEL=llama3.2:1b
```

## Chat agent CLI

```bash
bash 23-mcp-ai-agent-awx/scripts/06-run-ollama-agent.sh
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --once "list awx templates"
```

## Bridge AI endpoint

```bash
curl -X POST http://localhost:8090/agent/chat \
  -H "X-API-Key: lab-bridge-key" \
  -H "Content-Type: application/json" \
  -d '{"message":"Chạy job Python Hello World trên AWX"}'
```

## n8n webhook (Ollama capstone)

```
POST http://localhost:5678/webhook/ai-ops
Body: {"message":"list awx templates"}
```

Workflow: `workflows/05-ollama-ai-chat-awx.json`

## Không cần Cursor

MCP/Cursor → xem `docs/optional-cursor-mcp.md` (tùy chọn)

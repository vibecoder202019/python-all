# Lab 03 — AI Agent miễn phí với Ollama

**Thời gian:** 45 phút  
**Không cần Cursor, không cần API key trả phí.**

## Bước 1: Cài Ollama

```bash
brew install ollama
ollama serve
```

Terminal mới:

```bash
ollama pull llama3.2:1b
ollama run llama3.2:1b "Hello"
```

## Bước 2: Setup module

```bash
cd learn-python-ai
bash 23-mcp-ai-agent-awx/scripts/setup.sh
export AWX_DEMO_MODE=1
export OLLAMA_MODEL=llama3.2:1b
```

## Bước 3: Chat agent

```bash
bash 23-mcp-ai-agent-awx/scripts/06-run-ollama-agent.sh
```

Thử các câu:

- `Liệt kê job template trên AWX`
- `Chạy job Python Hello World`
- `quit`

## Bước 4: Một lệnh

```bash
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --once "launch job Python Hello World"
```

## Bước 5: Bridge + Ollama (chuẩn bị n8n)

Terminal 1:

```bash
bash 23-mcp-ai-agent-awx/scripts/04-run-agent-bridge.sh
```

Terminal 2:

```bash
curl -X POST http://localhost:8090/agent/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: lab-bridge-key" \
  -d '{"message":"Liệt kê template AWX"}'
```

## Checklist

- [ ] Ollama chạy, model đã pull
- [ ] Agent chat trả JSON templates (demo hoặc AWX thật)
- [ ] `/agent/chat` hoạt động

**Tiếp:** Module 24 — workflow n8n + Ollama

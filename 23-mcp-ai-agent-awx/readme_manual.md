# Hướng dẫn chạy Manual — Module 23: AI Agent + AWX (Ollama)

> Lệnh trích từ `setup.sh`, `01-check-prerequisites.sh`, `02-install-ollama.sh`, `04-run-agent-bridge.sh`, `05-test-mcp-tools.sh`, `06-run-ollama-agent.sh`.

## Phần A — Cài đặt Python (`scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r 23-mcp-ai-agent-awx/mcp-server/requirements.txt
pip install -r 23-mcp-ai-agent-awx/agent-bridge/requirements.txt
pip install httpx
cp -n 23-mcp-ai-agent-awx/config/.env.example 23-mcp-ai-agent-awx/config/.env
```

**Kiểm tra:**

```bash
python -c "import mcp, fastapi, uvicorn, httpx; print('OK')"
```

---

## Phần B — Kiểm tra môi trường (`scripts/01-check-prerequisites.sh`)

```bash
python3 --version
command -v uvicorn || pip install uvicorn
python3 -c "import mcp; print('mcp OK')"
kubectl get pods -n awx 2>/dev/null | head -5 || echo "AWX optional — dùng AWX_DEMO_MODE=1"
```

---

## Phần C — Cài Ollama (`scripts/02-install-ollama.sh`)

```bash
brew install ollama
ollama serve
```

Terminal mới:

```bash
ollama pull llama3.2:1b
curl -sf http://localhost:11434/api/tags
ollama run llama3.2:1b "Xin chào"
```

**Kiểm tra:**

```bash
curl -sf http://localhost:11434/api/tags | head -c 200
```

---

## Phần D — Cấu hình env

```bash
cd learn-python-ai/23-mcp-ai-agent-awx
cp config/.env.example config/.env
source ../.venv/bin/activate
set -a && source config/.env && set +a
export AWX_DEMO_MODE=1
export OLLAMA_MODEL=llama3.2:1b
```

---

## Phần E — Test tools demo (`scripts/05-test-mcp-tools.sh`)

```bash
cd learn-python-ai && source .venv/bin/activate
export AWX_DEMO_MODE=1
python 23-mcp-ai-agent-awx/examples/01_test_awx_tools.py --demo
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --demo --once "list templates"
```

---

## Phần F — Agent Bridge (`scripts/04-run-agent-bridge.sh`)

Terminal 1:

```bash
cd learn-python-ai/23-mcp-ai-agent-awx
source ../.venv/bin/activate
set -a && source config/.env && set +a
uvicorn agent-bridge.main:app --host 0.0.0.0 --port 8090 --reload
```

Terminal 2 — **Kiểm tra:**

```bash
curl -sf http://localhost:8090/health
curl -sf http://localhost:8090/health | python3 -m json.tool
curl -X POST http://localhost:8090/agent/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: lab-bridge-key" \
  -d '{"message":"List AWX job templates"}'
python learn-python-ai/23-mcp-ai-agent-awx/examples/02_call_bridge_api.py --intent list_templates
```

---

## Phần G — Chat Ollama (`scripts/06-run-ollama-agent.sh`)

```bash
cd learn-python-ai && source .venv/bin/activate
set -a && source 23-mcp-ai-agent-awx/config/.env && set +a
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py --once "Liệt kê job template AWX"
python 23-mcp-ai-agent-awx/ai-agent/ollama_agent.py
```

---

## Phần H — AWX thật (Module 15)

```bash
kubectl port-forward svc/awx-service 8052:80 -n awx
export AWX_URL=http://localhost:8052
export AWX_TOKEN=PASTE_TOKEN
export AWX_DEMO_MODE=0
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `01-check-prerequisites.sh` | B |
| `02-install-ollama.sh` | C |
| `05-test-mcp-tools.sh` | E |
| `04-run-agent-bridge.sh` | F |
| `06-run-ollama-agent.sh` | G |

**(Tùy chọn Cursor MCP:** `scripts/03-run-mcp-server.sh` — xem `docs/optional-cursor-mcp.md`)

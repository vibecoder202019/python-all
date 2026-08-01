# Module 23: AI Agent + AWX (Ollama miễn phí)

Xây **AI agent cá nhân** bằng **Ollama** (local, **100% miễn phí**) — chat tự nhiên → tự động hóa **Ansible AWX**, kết nối **n8n** (Module 24).

> **Không cần Cursor.** MCP/Cursor chỉ là [tùy chọn](docs/optional-cursor-mcp.md).  
> **Tiên quyết:** [Module 15 — AWX](../15-ansible-awx-minio-k8s/README.md)

---

## Kiến trúc (Ollama — luồng chính)

```
Bạn (chat) ──► Ollama (free) ──► intent JSON ──► AWX
                    ▲
n8n webhook ──► Agent Bridge /agent/chat ──► Ollama + AWX
```

---

## Chạy nhanh — AI miễn phí

```bash
# 1. Ollama (terminal 1)
brew install ollama
ollama serve
ollama pull llama3.2:1b

# 2. Setup Python (terminal 2)
cd learn-python-ai
bash 23-mcp-ai-agent-awx/scripts/setup.sh
export AWX_DEMO_MODE=1

# 3. Chat agent
bash 23-mcp-ai-agent-awx/scripts/06-run-ollama-agent.sh
# Thử: "Liệt kê job template AWX"
# Thử: "Chạy job Python Hello World"

# 4. Bridge cho n8n (terminal 3)
bash 23-mcp-ai-agent-awx/scripts/04-run-agent-bridge.sh

# 5. Test AI qua HTTP
curl -X POST http://localhost:8090/agent/chat \
  -H "Content-Type: application/json" \
  -H "X-API-Key: lab-bridge-key" \
  -d '{"message":"List AWX job templates"}'
```

Chi tiết: [docs/02-ollama-free-ai-agent.md](docs/02-ollama-free-ai-agent.md)

---

## Agent Bridge API

| Method | Path | Mô tả |
|--------|------|-------|
| POST | **`/agent/chat`** | **Chính** — chat + Ollama → AWX |
| POST | `/agent/run` | Intent cứng (không cần AI) |
| GET | `/health` | + trạng thái Ollama |

---

## Lộ trình học

| Lab | Nội dung |
|-----|----------|
| [lab01](labs/basic/lab01-mcp-concepts.md) | Agent, tools, automation |
| [lab03](labs/intermediate/lab03-ollama-agent.md) | **Ollama agent (chính)** |
| [lab04](labs/intermediate/lab04-agent-bridge.md) | Bridge + n8n |
| Capstone | [Module 24](../24-n8n-ai-automation/labs/capstone/README.md) |

---

## FAQ

**Có mất phí không?**  
Ollama + model `llama3.2:1b` chạy local — **miễn phí**. AWX/MinIO trên K8s local cũng miễn phí (Module 15).

**Máy yếu?**  
Dùng `llama3.2:1b` (~2GB RAM) hoặc `--demo` / `AWX_DEMO_MODE=1` không cần Ollama.

**Gemini/ChatGPT free?**  
Có thể mở rộng sau qua API free tier; lab chuẩn dùng Ollama offline.

---

[readme_manual.md](readme_manual.md) | [cheatsheet/mcp-awx.md](cheatsheet/mcp-awx.md)

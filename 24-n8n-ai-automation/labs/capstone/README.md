# Capstone Lab — Tự động hóa AI + AWX (Module 15 + 23 + 24)

**Thời gian:** 2–3 giờ  
**Mục tiêu:** Một pipeline kết nối **n8n → Agent Bridge → AWX → MinIO**

---

## Kiến trúc

```
Webhook/Schedule (n8n)
        │
        ▼
Agent Bridge :8090  ← Module 23
        │
        ▼
Ansible AWX         ← Module 15
        │
        ▼
MinIO (artifact)    ← Module 15
```

**Song song:** Cursor + MCP agent (Module 23) — cùng tools AWX, trigger bằng chat thay vì n8n.

---

## Phase 0 — Prerequisites

| Thành phần | Module | Kiểm tra |
|------------|--------|----------|
| AWX + MinIO trên K8s | 15 | `kubectl get pods -n awx -n minio` |
| MCP deps + Bridge | 23 | `bash 23-mcp-ai-agent-awx/scripts/setup.sh` |
| Docker | 24 | `docker compose version` |

Không có AWX? Bridge với `AWX_DEMO_MODE=1` vẫn chạy được capstone logic.

→ Chi tiết: [00-prerequisites.md](00-prerequisites.md)

---

## Phase 1 — Module 15 (AWX sẵn sàng)

```bash
kubectl port-forward svc/awx-service 8052:80 -n awx
export AWX_URL=http://localhost:8052
export AWX_TOKEN=your-token
```

Tạo Job Template **Python Hello World** trên AWX (nếu chưa có — theo Module 15).

---

## Phase 2 — Module 23 (Agent Bridge)

```bash
cd learn-python-ai/23-mcp-ai-agent-awx
cp config/.env.example config/.env
# AWX_DEMO_MODE=0 nếu dùng AWX thật

bash scripts/04-run-agent-bridge.sh
```

Test:

```bash
curl -H "X-API-Key: lab-bridge-key" http://localhost:8090/templates
```

---

## Phase 3 — Module 24 (n8n)

```bash
bash 24-n8n-ai-automation/scripts/02-deploy-n8n-compose.sh
open http://localhost:5678
```

Import workflow: `workflows/04-capstone-ai-ops.json` → **Activate**

→ [03-connect-mcp-bridge.md](03-connect-mcp-bridge.md)

---

## Phase 4 — End-to-end

```bash
bash 24-n8n-ai-automation/scripts/04-test-webhook.sh
```

Hoặc:

```bash
curl -X POST http://localhost:5678/webhook/awx-run \
  -u admin:n8n-lab-pass \
  -H "Content-Type: application/json" \
  -d '{"template_name":"Python Hello World","extra_vars":{"user_name":"capstone"}}'
```

→ [04-end-to-end.md](04-end-to-end.md)

---

## Phase 5 — AI miễn phí (Ollama) qua n8n

```bash
ollama serve && ollama pull llama3.2:1b
```

Import `workflows/05-ollama-ai-chat-awx.json` → Activate

```bash
curl -X POST http://localhost:5678/webhook/ai-ops \
  -u admin:n8n-lab-pass \
  -H "Content-Type: application/json" \
  -d '{"message":"List AWX job templates"}'
```

**Kỳ vọng:** JSON có `parsed_intent` + `result` từ Ollama + AWX.

---

## Phase 6 (tùy chọn) — Cursor MCP

Không bắt buộc. Xem Module 23 `docs/optional-cursor-mcp.md`.

---

## Checklist capstone

- [ ] n8n workflow chạy → bridge trả job id
- [ ] AWX job successful (hoặc demo mode)
- [ ] Hiểu sự khác MCP (chat) vs n8n (webhook/schedule)
- [ ] Teardown: `bash 24-n8n-ai-automation/scripts/06-teardown.sh`

---

## Mở rộng

- Schedule n8n mỗi sáng → health check AWX templates
- Thêm node Slack/Email báo kết quả job
- OpenAI node trong n8n parse intent → gọi `/agent/run` (AI orchestration)

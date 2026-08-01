# Module 24: n8n + Tích hợp AI Agent & AWX

Tự học **n8n** (workflow automation) — kết nối **Agent Bridge** (Module 23) và **AWX** (Module 15) thành **lab capstone liên thông**.

> **Tiên quyết:** [Module 15](../15-ansible-awx-minio-k8s/README.md), [Module 23](../23-mcp-ai-agent-awx/README.md)

---

## Mục tiêu

- Cài **n8n** bằng Docker Compose **hoặc Kubernetes** (`k8s-ai-automation/`)
- Tạo workflow webhook + schedule
- Gọi **Agent Bridge API** để launch AWX job
- Hoàn thành **capstone** 15 → 23 → 24

---

## Chạy nhanh

### Docker Compose (local)

```bash
cd learn-python-ai

# 1. Bridge (terminal 1)
bash 23-mcp-ai-agent-awx/scripts/setup.sh
bash 23-mcp-ai-agent-awx/scripts/04-run-agent-bridge.sh

# 2. n8n (terminal 2)
bash 24-n8n-ai-automation/scripts/01-check-prerequisites.sh
bash 24-n8n-ai-automation/scripts/02-deploy-n8n-compose.sh

# 3. UI
open http://localhost:5678
# admin / n8n-lab-pass
```

### Kubernetes (full stack trên cluster)

```bash
# AWX Module 15 đã deploy trên cluster (khuyến nghị)
bash 24-n8n-ai-automation/scripts/03-deploy-k8s.sh

# UI qua Ingress hoặc port-forward
kubectl port-forward -n ai-automation svc/n8n 5678:5678
open http://localhost:5678
```

Chi tiết: [docs/05-deploy-kubernetes.md](docs/05-deploy-kubernetes.md)

```bash
# Capstone guide
bash 24-n8n-ai-automation/scripts/05-run-capstone-demo.sh
```

Import workflow: `workflows/04-capstone-ai-ops.json`

---

## Kiến trúc capstone

Xem [labs/capstone/README.md](labs/capstone/README.md)

---

## Workflows có sẵn

| File | Mô tả |
|------|-------|
| `02-awx-list-templates.json` | Manual → list AWX templates |
| `04-capstone-ai-ops.json` | Webhook → launch job → response |

---

## Lộ trình

| Lab | Nội dung |
|-----|----------|
| [capstone/00](labs/capstone/00-prerequisites.md) | Prerequisites 15+23 |
| [capstone/03](labs/capstone/03-connect-mcp-bridge.md) | n8n ↔ Bridge |
| [capstone/04](labs/capstone/04-end-to-end.md) | End-to-end |

Docs: [docs/04-integrate-mcp-bridge.md](docs/04-integrate-mcp-bridge.md)

---

## Cấu trúc

```
24-n8n-ai-automation/
├── docker-compose/      # Compose local
├── k8s-ai-automation/   # n8n + bridge + Ollama trên K8s
├── workflows/
├── labs/capstone/
├── scripts/
└── docs/
```

---

## FAQ

**Cần OpenAI trong n8n không?**  
Capstone dùng **Ollama miễn phí** qua Bridge `/agent/chat`. Workflow `05-ollama-ai-chat-awx.json`.

**Không muốn Cursor?**  
Module 23 không bắt buộc Cursor — chỉ Ollama + Bridge.

**Teardown**

```bash
bash scripts/06-teardown.sh          # Compose
bash scripts/07-teardown-k8s.sh      # Kubernetes
```

---

[readme_manual.md](readme_manual.md) | [cheatsheet/n8n-awx.md](cheatsheet/n8n-awx.md)

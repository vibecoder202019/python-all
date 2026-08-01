# Lab Capstone 00 — Prerequisites

## Module 15 — AWX + MinIO

```bash
bash learn-python-ai/15-ansible-awx-minio-k8s/scripts/01-check-prerequisites.sh
bash learn-python-ai/15-ansible-awx-minio-k8s/scripts/02-deploy-minio.sh
bash learn-python-ai/15-ansible-awx-minio-k8s/scripts/03-deploy-awx-operator.sh
bash learn-python-ai/15-ansible-awx-minio-k8s/scripts/04-deploy-awx-instance.sh
```

Hoặc đã có AWX → skip deploy, chỉ cần token.

## Module 23 — Setup

```bash
bash learn-python-ai/23-mcp-ai-agent-awx/scripts/setup.sh
bash learn-python-ai/23-mcp-ai-agent-awx/scripts/01-check-prerequisites.sh
```

## Module 24 — Docker

```bash
docker --version
docker compose version
```

## Demo path (không AWX)

```bash
export AWX_DEMO_MODE=1
```

Vẫn học được n8n + bridge logic.

**Tiếp:** [README capstone](README.md)

# n8n ↔ Agent Bridge

## URLs

| Service | Compose (local) | Kubernetes |
|---------|-----------------|------------|
| n8n UI | http://localhost:5678 | http://n8n.local hoặc port-forward |
| Bridge API | http://localhost:8090 | http://agent-bridge.ai-automation.svc:8090 |
| Webhook capstone | POST .../webhook/awx-run | POST http://n8n.local/webhook/awx-run |

## Deploy K8s

```bash
bash scripts/03-deploy-k8s.sh
kubectl port-forward -n ai-automation svc/n8n 5678:5678
```

## Auth

- n8n: Basic `admin` / `n8n-lab-pass`
- Bridge: Header `X-API-Key: lab-bridge-key`

## Body capstone webhook

```json
{
  "template_name": "Python Hello World",
  "extra_vars": {"user_name": "n8n"}
}
```

## Bridge agent/run intents

- `list_templates`
- `launch_job` + `template_name` + `extra_vars`
- `job_status` + `job_id`

## Docker → host / K8s in-cluster

```
# Compose: n8n container → bridge trên host
http://host.docker.internal:8090

# K8s: n8n pod → bridge service
http://agent-bridge.ai-automation.svc.cluster.local:8090
```

# Lab 07 — Viết manifest K8s (Intermediate)

**45 phút**

Yêu cầu CKA-style (tự đặt prompt từ [write-deployment.md](../../prompts/kubernetes/write-deployment.md)):

- Deployment `prompt-lab-web`, nginx:1.25, 2 replicas
- Service ClusterIP port 80
- namespace `cka-lab`
- labels `lab=prompt-07`

Apply (nếu có cluster) hoặc dry-run client.

## Pass

YAML valid, không `:latest`, có resource requests.

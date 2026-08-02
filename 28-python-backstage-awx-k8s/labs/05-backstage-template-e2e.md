# Lab 05 — Backstage template (E2E giả lập)

Không bắt buộc cài full Backstage. Giả lập bước Scaffolder:

```bash
bash scripts/03-run-bridge.sh   # terminal 1

curl -s -X POST http://127.0.0.1:8090/api/scaffolder/run \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: dev-bridge-key-change-me' \
  -d '{
    "values": {
      "app_name": "from-backstage",
      "namespace": "platform-apps",
      "image": "nginx:1.27-alpine",
      "replicas": 2,
      "template_id": 7,
      "terraform_workspace": "labs"
    }
  }' | jq
```

Đăng ký `backstage/location.yaml` khi có Backstage instance (xem docs/03).

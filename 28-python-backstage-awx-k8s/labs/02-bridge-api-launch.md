# Lab 02 — Bridge API tạo deploy task

```bash
# Terminal 1
bash scripts/03-run-bridge.sh

# Terminal 2
bash scripts/08-test-bridge-api.sh
```

Tự gọi:

```bash
curl -s http://127.0.0.1:8090/health | jq
curl -s -X POST http://127.0.0.1:8090/api/v1/deploy \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: dev-bridge-key-change-me' \
  -d '{"app_name":"payments","namespace":"platform-apps","image":"nginx:1.27-alpine","replicas":3}' | jq
```

Swagger: http://127.0.0.1:8090/docs

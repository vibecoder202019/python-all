# AWX API — tạo task (launch job)

## Auth

```bash
# AWX UI → User → Tokens → Create
export AWX_URL=http://localhost:8052
export AWX_TOKEN=xxxxx
```

## Endpoints

| Method | Path | Mục đích |
|--------|------|----------|
| GET | `/api/v2/job_templates/` | Liệt kê template |
| POST | `/api/v2/job_templates/{id}/launch/` | **Tạo task / job** |
| GET | `/api/v2/jobs/{id}/` | Trạng thái job |

### Launch body

```json
{
  "extra_vars": {
    "app_name": "checkout",
    "namespace": "platform-apps",
    "image": "nginx:1.27-alpine",
    "replicas": 2
  }
}
```

## Qua Python (module này)

```python
from awx_client import AwxClient, AwxConfig
client = AwxClient(AwxConfig.from_env())
job = client.launch_job_template(7, extra_vars={"replicas": 3})
print(job["id"], job.get("status"))
```

## Qua Bridge API (khuyến nghị cho Backstage / CI)

```bash
curl -s -X POST http://127.0.0.1:8090/api/v1/jobs \
  -H 'Content-Type: application/json' \
  -H "X-API-Key: $BRIDGE_API_KEY" \
  -d '{"template_id":7,"extra_vars":{"app_name":"demo","replicas":2}}'
```

Shortcut deploy K8s:

```bash
curl -s -X POST http://127.0.0.1:8090/api/v1/deploy \
  -H 'Content-Type: application/json' \
  -H "X-API-Key: $BRIDGE_API_KEY" \
  -d '{"app_name":"demo-api","namespace":"platform-apps","image":"nginx:1.27-alpine","replicas":2}'
```

## Liên kết

- Module [15](../15-ansible-awx-minio-k8s/README.md) — deploy AWX lên K8s
- CLI: `python3 project/run_launch.py --demo launch --template-id 7`

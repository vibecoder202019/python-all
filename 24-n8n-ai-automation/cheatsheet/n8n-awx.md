# n8n ↔ Agent Bridge

## URLs

| Service | URL |
|---------|-----|
| n8n UI | http://localhost:5678 |
| Bridge API | http://localhost:8090 |
| Bridge Swagger | http://localhost:8090/docs |
| Webhook capstone | POST http://localhost:5678/webhook/awx-run |

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

## Docker → host

```
http://host.docker.internal:8090
```

# Cheatsheet — Module 28 Platform

```bash
# Demo examples
bash scripts/02-run-all-examples.sh

# Bridge
bash scripts/03-run-bridge.sh
bash scripts/08-test-bridge-api.sh

# API tạo task AWX
curl -X POST :8090/api/v1/jobs -H 'X-API-Key: …' -d '{"template_id":7,"extra_vars":{…}}'
curl -X POST :8090/api/v1/deploy -d '{"app_name":"x","namespace":"platform-apps","image":"nginx:1.27-alpine","replicas":2}'

# CLI
python3 project/run_launch.py --demo list
python3 project/run_launch.py --demo deploy --app-name x --image nginx:1.27-alpine

# Terraform / K8s / Ansible
bash scripts/04-terraform-plan.sh --auto
bash scripts/05-deploy-k8s-demo.sh
bash scripts/06-ansible-deploy-local.sh
bash scripts/07-teardown.sh
```

| Env | Nghĩa |
|-----|-------|
| `AWX_URL` / `AWX_TOKEN` | Live AWX |
| `AWX_DEMO=true` | Fixture |
| `BRIDGE_API_KEY` | Auth Bridge |
| `AWX_DEPLOY_TEMPLATE_ID` | Mặc định JT deploy |

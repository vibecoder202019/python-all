# Module 28 — Manual (từng lệnh)

## 0. Setup

```bash
cd learn-python-ai
bash 28-python-backstage-awx-k8s/scripts/setup.sh
bash 28-python-backstage-awx-k8s/scripts/01-check-prerequisites.sh
cp 28-python-backstage-awx-k8s/data/.env.example 28-python-backstage-awx-k8s/data/.env
```

## 1. Examples (demo)

```bash
bash 28-python-backstage-awx-k8s/scripts/02-run-all-examples.sh
```

## 2. Bridge API — tạo task AWX

```bash
# Terminal 1
bash 28-python-backstage-awx-k8s/scripts/03-run-bridge.sh

# Terminal 2
bash 28-python-backstage-awx-k8s/scripts/08-test-bridge-api.sh

# Tạo task thủ công
curl -s -X POST http://127.0.0.1:8090/api/v1/jobs \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: dev-bridge-key-change-me' \
  -d '{"template_id":7,"extra_vars":{"app_name":"manual","replicas":2}}'
```

## 3. Terraform namespace (cần cluster)

```bash
cp 28-python-backstage-awx-k8s/terraform/terraform.tfvars.example \
   28-python-backstage-awx-k8s/terraform/terraform.tfvars
bash 28-python-backstage-awx-k8s/scripts/04-terraform-plan.sh --auto
```

## 4. Deploy K8s

```bash
# Manifests tĩnh
bash 28-python-backstage-awx-k8s/scripts/05-deploy-k8s-demo.sh

# Ansible (giống AWX)
bash 28-python-backstage-awx-k8s/scripts/06-ansible-deploy-local.sh
```

## 5. Live AWX (Module 15)

```bash
# data/.env: AWX_URL, AWX_TOKEN, AWX_DEMO=false
python3 28-python-backstage-awx-k8s/project/run_launch.py list
python3 28-python-backstage-awx-k8s/project/run_launch.py deploy \
  --app-name demo --image nginx:1.27-alpine --replicas 2
```

## 6. Teardown

```bash
bash 28-python-backstage-awx-k8s/scripts/07-teardown.sh
```

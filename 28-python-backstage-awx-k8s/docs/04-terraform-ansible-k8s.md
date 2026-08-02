# Terraform + Ansible + Kubernetes

## Terraform (chuẩn bị nền)

```bash
bash scripts/04-terraform-plan.sh          # plan
bash scripts/04-terraform-plan.sh --auto   # apply namespace + quota
```

Tạo:
- Namespace `platform-apps`
- ResourceQuota (tuỳ chọn)
- ConfigMap `platform-meta` (gợi ý bridge / template id)

**Nguyên tắc:** Terraform = trạng thái lâu dài (ns, quota, network policy). App Deployment hàng ngày = Ansible/AWX (hoặc GitOps).

## Ansible (deploy app)

Playbook: `ansible/deploy-app.yml`  
AWX Job Template trỏ playbook này; `extra_vars` từ Bridge.

Chạy local (không qua AWX):

```bash
bash scripts/06-ansible-deploy-local.sh
# hoặc
APP_NAME=myapp IMAGE=nginx:1.27-alpine bash scripts/06-ansible-deploy-local.sh
```

## K8s manifests tĩnh

`k8s/demo-app.yaml` — apply nhanh để smoke-test cluster:

```bash
bash scripts/05-deploy-k8s-demo.sh
```

## Ghép với AWX thật (Module 15)

1. Deploy AWX (module 15)
2. Tạo Project trỏ git chứa `ansible/`
3. Tạo Job Template id=7 (hoặc sửa `AWX_DEPLOY_TEMPLATE_ID`)
4. `AWX_DEMO=false` + token → Bridge launch thật

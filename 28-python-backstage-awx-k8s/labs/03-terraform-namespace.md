# Lab 03 — Terraform tạo namespace

Cần: `terraform`, `kubectl`, cluster (kind / Docker Desktop).

```bash
kubectl config current-context   # ví dụ kind-lab-desktop
cp terraform/terraform.tfvars.example terraform/terraform.tfvars
# sửa kube_context cho khớp
bash scripts/04-terraform-plan.sh --auto
kubectl get ns platform-apps
kubectl get quota,cm -n platform-apps
```

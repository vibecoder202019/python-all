# Lab 06 — Workspace & Lifecycle (Intermediate)

**Thời gian:** 45 phút

## Bài tập

Trong `terraform/02-variables`:

```bash
terraform workspace new dev
terraform workspace new prod
terraform workspace select dev
terraform apply -var="environment=dev" -auto-approve
terraform workspace select prod
terraform apply -var="environment=prod" -auto-approve
terraform workspace list
```

So sánh state từng workspace trong `terraform.tfstate.d/`.

Thêm `lifecycle { prevent_destroy = true }` vào một resource — thử `destroy`.

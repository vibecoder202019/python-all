# Lab 02 — Variables & Outputs (Basic)

**Thời gian:** 30 phút

## Bài tập

1. Copy `terraform.tfvars.example` → `terraform.tfvars` với `environment=staging`
2. Apply và kiểm tra file `output/demo-app-staging.json`
3. Dùng `-var` không cần file tfvars:

```bash
terraform apply -var="environment=prod" -var="app_name=payment"
```

4. In output `config_path` bằng `terraform output -json | jq`

## Verify

File `output/demo-app-staging.json` tồn tại sau apply.

# Terraform environments

## management/

Chạy từ **management account** credentials (Organizations admin).

```bash
cd terraform/environments/management
cp terraform.tfvars.example terraform.tfvars
terraform init && terraform plan
```

Tạo OU lab + attach SCP. **Yêu cầu** Organizations đã enable (Console lab 01).

## dev-workload/

Deploy role + S3 bucket **trong dev account** qua `assume_role`.

```bash
cd terraform/environments/dev-workload
cp terraform.tfvars.example terraform.tfvars
# Sửa management_account_id, dev_account_id
terraform init && terraform plan
terraform apply   # khi sẵn sàng
```

## Modules

- `modules/cross-account-role` — IAM role trust management
- `modules/scp` — SCP attach OU
- `modules/organizational-unit` — OU standalone

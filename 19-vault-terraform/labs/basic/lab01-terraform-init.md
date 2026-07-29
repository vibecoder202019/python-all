# Lab 01 — Terraform init, plan, apply (Basic)

**Thời gian:** 30 phút

## Mục tiêu

- Hiểu workflow `init → plan → apply → destroy`
- Tạo file local bằng Terraform

## Bước 1 — Chạy example

```bash
cd 19-vault-terraform/terraform/01-hello
terraform init
terraform plan
terraform apply
```

Gõ `yes` khi được hỏi.

## Bước 2 — Kiểm tra

```bash
cat output/hello.txt
terraform show
terraform output
```

## Bước 3 — Sửa và apply lại

Sửa `content` trong `main.tf`, chạy lại `plan` — thấy diff `forces replacement` hoặc update.

## Bước 4 — Dọn dẹp

```bash
terraform destroy
bash ../../scripts/04-verify-lab.sh 01  # sau apply lai de test
```

## Verify

```bash
bash 19-vault-terraform/scripts/04-verify-lab.sh 01
```

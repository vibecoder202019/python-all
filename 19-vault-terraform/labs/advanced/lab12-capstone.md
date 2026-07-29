# Lab 12 — Capstone Project (Advanced)

**Thời gian:** 120 phút

## Yêu cầu

Hoàn thành pipeline:

1. Vault chạy + secret `secret/myapp/db`
2. Policy AppRole cho CI (read only)
3. Terraform `project/` tạo:
   - JSON config từ module
   - K8s Secret manifest YAML từ Vault data
4. Không có plaintext password trong Git

## Chạy

```bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'
bash vault/scripts/seed-secrets.sh
AUTO_APPROVE=yes bash scripts/03-run-terraform.sh project --auto
ls terraform/project/output/
```

## Verify

```bash
bash scripts/04-verify-lab.sh 12
```

## Mở rộng

- Deploy manifest lên K8s (Module 18)
- Thay local backend bằng S3 (Module 13)

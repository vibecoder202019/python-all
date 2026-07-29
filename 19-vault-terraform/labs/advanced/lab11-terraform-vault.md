# Lab 11 — Terraform + Vault Provider (Advanced)

**Thời gian:** 90 phút

## Chuẩn bị

Vault dev đang chạy + secret đã seed:

```bash
bash vault/scripts/seed-secrets.sh
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'
```

## Apply

```bash
AUTO_APPROVE=yes bash scripts/03-run-terraform.sh 05-vault-provider --auto
cat terraform/05-vault-provider/output/.env.generated
```

**Không** commit file `.env.generated`.

## Bài tập

1. Đổi password trong Vault → `terraform apply` lại → file cập nhật
2. Revoke token read-only → apply fail — hiểu dependency auth
3. Thêm output `sensitive = true` cho password hint

## Verify

```bash
bash scripts/04-verify-lab.sh 11
```

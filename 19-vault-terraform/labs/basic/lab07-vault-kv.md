# Lab 07 — Vault Dev & KV v2 (Basic)

**Thời gian:** 45 phút

## Chuẩn bị

Terminal 1:
```bash
bash 19-vault-terraform/scripts/02-setup-vault-dev.sh
```

Terminal 2:
```bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'
vault status
```

## Bài tập

```bash
# Ghi secret
vault kv put secret/myapp/db username=admin password=lab123 host=db.internal

# Doc
vault kv get secret/myapp/db
vault kv get -field=password secret/myapp/db

# Version
vault kv put secret/myapp/db password=lab456
vault kv get -version=1 secret/myapp/db
vault kv metadata get secret/myapp/db
```

## Verify

```bash
bash 19-vault-terraform/scripts/04-verify-lab.sh 07
```

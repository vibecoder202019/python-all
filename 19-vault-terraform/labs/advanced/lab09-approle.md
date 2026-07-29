# Lab 09 — AppRole Auth (Advanced)

**Thời gian:** 60 phút

```bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'
bash 19-vault-terraform/vault/scripts/setup-approle.sh
```

Login bằng Role ID + Secret ID, dùng token nhận được đọc `secret/myapp/db`.

Viết script bash 10 dòng: login AppRole → export VAULT_TOKEN → `vault kv get`.

## Production note

Secret ID nên deliver qua CI secret manager — không commit vào Git.

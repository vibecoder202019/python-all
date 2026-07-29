# Lab 08 — Vault Policies & Tokens (Intermediate)

**Thời gian:** 60 phút

## Bài tập

```bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

# Nap policy
vault policy write readonly-kv vault/policies/readonly-kv.hcl
vault policy read readonly-kv

# Token chi read
TOKEN=$(vault token create -policy=readonly-kv -format=json | jq -r .auth.client_token)
VAULT_TOKEN=$TOKEN vault kv get secret/myapp/db      # OK
VAULT_TOKEN=$TOKEN vault kv put secret/myapp/db x=1  # denied
```

Viết policy `deny-delete` — read được nhưng không delete metadata.

## Verify

```bash
bash 19-vault-terraform/scripts/04-verify-lab.sh 08
```

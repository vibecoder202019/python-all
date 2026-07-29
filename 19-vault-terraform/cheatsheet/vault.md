# Cheatsheet Vault

export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'   # CHI dev

vault status
vault secrets list
vault auth list
vault policy list

# KV v2
vault secrets enable -path=secret kv-v2
vault kv put secret/myapp/db user=admin pass=secret
vault kv get secret/myapp/db
vault kv get -field=pass secret/myapp/db
vault kv list secret/
vault kv metadata get secret/myapp/db

# Policy
vault policy write NAME policy.hcl
vault policy read NAME
vault token create -policy=NAME -ttl=1h

# AppRole
vault auth enable approle
vault write auth/approle/role/APP token_policies="POL"
vault read auth/approle/role/APP/role-id
vault write -f auth/approle/role/APP/secret-id
vault write auth/approle/login role_id=... secret_id=...

# Dev server
vault server -dev -dev-root-token-id=root

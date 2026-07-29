path "auth/approle/login" {
  capabilities = ["create", "read"]
}

path "secret/data/myapp/*" {
  capabilities = ["read"]
}

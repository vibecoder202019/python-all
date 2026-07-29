# Cheatsheet Vault + Terraform

export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='...'

# Provider
provider "vault" {
  address = var.vault_address
}

# Doc secret KV v2
data "vault_kv_secret_v2" "db" {
  mount = "secret"
  name  = "myapp/db"
}
# data.vault_kv_secret_v2.db.data["password"]

# Tao secret bang Terraform
resource "vault_kv_secret_v2" "x" {
  mount     = "secret"
  name      = "path"
  data_json = jsonencode({ k = "v" })
}

# Output nhay cam
output "pass" {
  value     = data.vault_kv_secret_v2.db.data["password"]
  sensitive = true
}

# Workflow lab
vault kv put secret/myapp/db username=a password=b
cd terraform/05-vault-provider && terraform apply

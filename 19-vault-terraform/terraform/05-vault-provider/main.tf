terraform {
  required_version = ">= 1.6"
  required_providers {
    vault = {
      source  = "hashicorp/vault"
      version = "~> 4.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

variable "vault_address" {
  default = "http://127.0.0.1:8200"
}

provider "vault" {
  address = var.vault_address
  # token: export VAULT_TOKEN=...
}

data "vault_kv_secret_v2" "db" {
  mount = "secret"
  name  = "myapp/db"
}

resource "local_file" "app_env" {
  filename = "${path.module}/output/.env.generated"
  content  = <<-EOT
    DB_USER=${data.vault_kv_secret_v2.db.data["username"]}
    DB_PASS=${data.vault_kv_secret_v2.db.data["password"]}
    DB_HOST=${lookup(data.vault_kv_secret_v2.db.data, "host", "localhost")}
  EOT

  file_permission = "0600"
}

output "env_file" {
  value = local_file.app_env.filename
}

output "db_user" {
  value     = data.vault_kv_secret_v2.db.data["username"]
  sensitive = false
}

output "db_password_hint" {
  value     = "(hidden — xem file .env.generated)"
  sensitive = true
}

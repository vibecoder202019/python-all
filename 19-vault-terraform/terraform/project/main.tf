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

variable "environment" {
  default = "dev"
}

provider "vault" {
  address = var.vault_address
}

data "vault_kv_secret_v2" "app" {
  mount = "secret"
  name  = "myapp/db"
}

module "config" {
  source      = "../04-modules/modules/config-file"
  environment = var.environment
  app_name    = "capstone"
}

resource "local_file" "deployment_manifest" {
  filename = "${path.module}/output/deployment-${var.environment}.yaml"
  content  = <<-YAML
    apiVersion: v1
    kind: Secret
    metadata:
      name: app-db
      namespace: default
    type: Opaque
    stringData:
      username: ${data.vault_kv_secret_v2.app.data["username"]}
      password: ${data.vault_kv_secret_v2.app.data["password"]}
    ---
    # Config tu module Terraform
    # Path: ${module.config.path}
  YAML
}

output "manifest_path" {
  value = local_file.deployment_manifest.filename
}

output "config_module_path" {
  value = module.config.path
}

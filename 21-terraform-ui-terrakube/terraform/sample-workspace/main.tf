terraform {
  required_version = ">= 1.6"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

variable "environment" {
  type        = string
  description = "Moi truong: dev, staging, prod"
  default     = "dev"
}

variable "app_name" {
  type        = string
  description = "Ten ung dung"
  default     = "terrakube-lab"
}

provider "local" {}

resource "local_file" "app_config" {
  filename = "${path.module}/output/${var.app_name}-${var.environment}.json"
  content = jsonencode({
    app         = var.app_name
    environment = var.environment
    managed_by  = "terrakube-ui-module-21"
    timestamp   = timestamp()
  })
}

output "config_file" {
  description = "Duong dan file config da tao"
  value       = local_file.app_config.filename
}

output "environment" {
  value = var.environment
}

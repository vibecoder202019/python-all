terraform {
  required_version = ">= 1.6"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

provider "local" {}

variable "environment" {
  description = "Moi truong: dev, staging, prod"
  type        = string
  default     = "dev"
}

variable "app_name" {
  description = "Ten ung dung"
  type        = string
  default     = "demo-app"
}

resource "local_file" "config" {
  filename = "${path.module}/output/${var.app_name}-${var.environment}.json"
  content = jsonencode({
    app         = var.app_name
    environment = var.environment
    created_by  = "terraform-module-19"
  })
}

output "config_path" {
  value = local_file.config.filename
}

output "environment" {
  value = var.environment
}

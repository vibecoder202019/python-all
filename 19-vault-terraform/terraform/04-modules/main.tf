terraform {
  required_version = ">= 1.6"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }

  backend "local" {
    path = "../../state/04-modules.tfstate"
  }
}

provider "local" {}

variable "environment" {
  default = "dev"
}

module "dev_config" {
  source      = "./modules/config-file"
  environment = var.environment
  app_name    = "api"
}

module "web_config" {
  source      = "./modules/config-file"
  environment = var.environment
  app_name    = "web"
}

output "config_paths" {
  value = [
    module.dev_config.path,
    module.web_config.path,
  ]
}

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

resource "local_file" "hello" {
  filename = "${path.module}/output/hello.txt"
  content  = "Xin chao tu Terraform! Module 19 - ${timestamp()}"
}

output "file_path" {
  value       = local_file.hello.filename
  description = "Duong dan file da tao"
}

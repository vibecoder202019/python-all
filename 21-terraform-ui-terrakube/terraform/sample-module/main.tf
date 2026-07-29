variable "environment" {
  type = string
}

variable "app_name" {
  type = string
}

resource "local_file" "config" {
  filename = "${path.module}/../../sample-workspace/output/${var.app_name}-${var.environment}-from-module.json"
  content = jsonencode({
    source      = "terrakube-private-module"
    app         = var.app_name
    environment = var.environment
  })
}

output "path" {
  value = local_file.config.filename
}

variable "environment" {
  type = string
}

variable "app_name" {
  type = string
}

resource "local_file" "config" {
  filename = "${path.module}/../../output/${var.app_name}-${var.environment}.json"
  content = jsonencode({
    app         = var.app_name
    environment = var.environment
    module      = "config-file"
  })
}

output "path" {
  value = local_file.config.filename
}

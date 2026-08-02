output "namespace" {
  value = kubernetes_namespace.apps.metadata[0].name
}

output "awx_deploy_template_id" {
  value = var.awx_deploy_template_id
}

output "bridge_deploy_example" {
  value = <<-EOT
    curl -s -X POST http://127.0.0.1:8090/api/v1/deploy \
      -H 'Content-Type: application/json' \
      -H 'X-API-Key: '"$BRIDGE_API_KEY" \
      -d '{"app_name":"demo-api","namespace":"${kubernetes_namespace.apps.metadata[0].name}","image":"nginx:1.27-alpine","replicas":2}'
  EOT
}

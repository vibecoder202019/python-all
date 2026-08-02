terraform {
  required_version = ">= 1.5.0"
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.29"
    }
  }
}

# Lab local: dùng kubeconfig hiện tại (kind / Docker Desktop / k3s).
# Production: đổi sang EKS provider + remote state.
provider "kubernetes" {
  config_path    = var.kubeconfig_path
  config_context = var.kube_context != "" ? var.kube_context : null
}

resource "kubernetes_namespace" "apps" {
  metadata {
    name = var.namespace
    labels = {
      "app.kubernetes.io/managed-by" = "terraform"
      "platform.mlops/module"        = "28"
      environment                    = var.environment
    }
  }
}

resource "kubernetes_resource_quota" "apps" {
  count = var.enable_quota ? 1 : 0

  metadata {
    name      = "platform-apps-quota"
    namespace = kubernetes_namespace.apps.metadata[0].name
  }

  spec {
    hard = {
      pods             = var.quota_pods
      "requests.cpu"    = var.quota_cpu
      "requests.memory" = var.quota_memory
    }
  }
}

resource "kubernetes_config_map" "platform_meta" {
  metadata {
    name      = "platform-meta"
    namespace = kubernetes_namespace.apps.metadata[0].name
  }

  data = {
    environment         = var.environment
    awx_job_template_id = tostring(var.awx_deploy_template_id)
    bridge_hint         = "POST /api/v1/deploy với namespace=${var.namespace}"
  }
}

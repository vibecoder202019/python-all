variable "namespace" {
  type        = string
  default     = "platform-apps"
  description = "Namespace Terraform tạo sẵn cho AWX/Ansible deploy vào"
}

variable "environment" {
  type    = string
  default = "labs"
}

variable "kubeconfig_path" {
  type    = string
  default = "~/.kube/config"
}

variable "kube_context" {
  type        = string
  default     = ""
  description = "Để trống = context hiện tại. Ví dụ: kind-lab-desktop"
}

variable "enable_quota" {
  type    = bool
  default = true
}

variable "quota_pods" {
  type    = string
  default = "20"
}

variable "quota_cpu" {
  type    = string
  default = "4"
}

variable "quota_memory" {
  type    = string
  default = "8Gi"
}

variable "awx_deploy_template_id" {
  type        = number
  default     = 7
  description = "Job template ID mặc định (Deploy microservice)"
}

terraform {
  required_version = ">= 1.6"
  required_providers {
    awx = {
      source  = "iwonderanddev/awx"
      version = "~> 24.0"
    }
  }
}

variable "awx_host" {
  description = "URL AWX server (port-forward hoac ingress)"
  type        = string
}

variable "awx_token" {
  description = "OAuth token AWX — KHONG commit file tfvars"
  type        = string
  sensitive   = true
}

variable "awx_insecure" {
  description = "Bo qua SSL verify (lab HTTP)"
  type        = bool
  default     = true
}

variable "organization_name" {
  default = "Lab-Module15"
}

variable "project_name" {
  default = "python-demo-playbooks"
}

variable "scm_url" {
  description = "Git repo co playbook (fork python-all)"
  type        = string
}

variable "scm_branch" {
  default = "main"
}

variable "playbook_path" {
  description = "Thu muc playbook trong repo"
  default     = "15-ansible-awx-minio-k8s/ansible-playbook/python-demo"
}

variable "job_template_name" {
  default = "python-script-demo-tf"
}

variable "playbook_file" {
  default = "playbook-script.yml"
}

provider "awx" {
  hostname    = var.awx_host
  oauth_token = var.awx_token
  insecure    = var.awx_insecure
}

resource "awx_organization" "lab" {
  name        = var.organization_name
  description = "Module 15 — Terraform AWX client lab"
}

resource "awx_project" "python_demo" {
  name             = var.project_name
  organization_id  = awx_organization.lab.id
  scm_type         = "git"
  scm_url          = var.scm_url
  scm_branch       = var.scm_branch
  scm_clean        = true
  scm_update_on_launch = true
}

resource "awx_inventory" "lab" {
  name            = "lab-localhost"
  organization_id = awx_organization.lab.id
  description     = "Inventory lab Module 15"
}

resource "awx_host" "localhost" {
  name         = "localhost"
  inventory_id = awx_inventory.lab.id
  variables    = jsonencode({ ansible_connection = "local" })
}

resource "awx_job_template" "python_script" {
  name         = var.job_template_name
  description  = "Chay playbook-script.yml — tao boi Terraform"
  job_type     = "run"
  organization_id = awx_organization.lab.id
  project_id   = awx_project.python_demo.id
  inventory_id = awx_inventory.lab.id
  playbook     = "${var.playbook_path}/${var.playbook_file}"
  extra_vars   = jsonencode({ demo_mode = true })
}

output "organization_id" {
  value = awx_organization.lab.id
}

output "project_id" {
  value = awx_project.python_demo.id
}

output "job_template_id" {
  value = awx_job_template.python_script.id
}

output "job_template_name" {
  value = awx_job_template.python_script.name
}

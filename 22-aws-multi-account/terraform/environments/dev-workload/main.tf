terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

variable "aws_region" {
  default = "ap-southeast-1"
}

variable "management_account_id" {
  type        = string
  description = "Management account ID (trust principal)"
}

variable "dev_account_id" {
  type        = string
  description = "Dev member account ID — provider assume_role target"
}

variable "dev_assume_role_name" {
  default     = "OrganizationAccountAccessRole"
  description = "Role trong dev account de terraform assume (lab: OrganizationAccountAccessRole)"
}

variable "external_id" {
  default = "lab-module-22-dev"
}

# Credentials goc: management account (aws configure profile)
provider "aws" {
  alias  = "management"
  region = var.aws_region
}

provider "aws" {
  alias  = "dev"
  region = var.aws_region

  assume_role {
    role_arn     = "arn:aws:iam::${var.dev_account_id}:role/${var.dev_assume_role_name}"
    session_name = "terraform-module-22-dev"
  }
}

module "devops_role" {
  source = "../../modules/cross-account-role"
  providers = {
    aws = aws.dev
  }

  role_name             = "DevOpsCrossAccountRole"
  management_account_id = var.management_account_id
  external_id           = var.external_id
  policy_json           = file("${path.module}/../../../policies/devops-scoped.json")
}

resource "aws_s3_bucket" "dev_lab" {
  provider = aws.dev
  bucket   = "module22-dev-${var.dev_account_id}-lab"
}

output "devops_role_arn" {
  value = module.devops_role.role_arn
}

output "dev_bucket" {
  value = aws_s3_bucket.dev_lab.bucket
}

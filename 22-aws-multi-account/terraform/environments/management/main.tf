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

variable "environment" {
  default = "lab"
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Project   = "module-22-multi-account"
      ManagedBy = "terraform"
    }
  }
}

data "aws_organizations_organization" "current" {}

resource "aws_organizations_organizational_unit" "workloads" {
  name      = "Workloads-Lab"
  parent_id = data.aws_organizations_organization.current.roots[0].id
}

resource "aws_organizations_organizational_unit" "sandbox" {
  name      = "Sandbox-Lab"
  parent_id = data.aws_organizations_organization.current.roots[0].id
}

module "scp_deny_leave_org" {
  source = "../../modules/scp"

  policy_name = "DenyLeaveOrganization-Lab"
  policy_file = "${path.module}/../../../policies/scp-deny-leave-org.json"
  target_id   = data.aws_organizations_organization.current.roots[0].id
}

module "scp_deny_regions_sandbox" {
  source = "../../modules/scp"

  policy_name = "DenyOutsideSingapore-Sandbox"
  policy_file = "${path.module}/../../../policies/scp-deny-regions.json"
  target_id   = aws_organizations_organizational_unit.sandbox.id
}

output "organization_id" {
  value = data.aws_organizations_organization.current.id
}

output "workloads_ou_id" {
  value = aws_organizations_organizational_unit.workloads.id
}

output "sandbox_ou_id" {
  value = aws_organizations_organizational_unit.sandbox.id
}

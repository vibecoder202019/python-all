# Terraform — AWS Organizations

Mirror cấu hình Console bằng Terraform.

---

## Provider setup (management account)

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "module-22-multi-account"
      ManagedBy   = "terraform"
      Environment = var.environment
    }
  }
}
```

Credentials: profile management admin hoặc env vars — **không commit keys**.

---

## Data source — Organization đã tồn tại

Sau khi bật Organizations trên Console (lab 01):

```hcl
data "aws_organizations_organization" "current" {}

output "org_id" {
  value = data.aws_organizations_organization.current.id
}

output "org_accounts" {
  value = data.aws_organizations_organization.current.accounts
}
```

---

## Tạo OU

```hcl
resource "aws_organizations_organizational_unit" "workloads" {
  name      = "Workloads"
  parent_id = data.aws_organizations_organization.current.roots[0].id
}
```

Module: [terraform/modules/organizational-unit](../terraform/modules/organizational-unit/)

---

## Tạo account member (cẩn thận!)

```hcl
resource "aws_organizations_account" "dev" {
  name  = "dev-workload"
  email = var.dev_account_email  # email CHUA dung AWS

  lifecycle {
    prevent_destroy = true  # tranh destroy nham account
  }
}
```

⚠️ Tạo account mất ~5 phút. Lab khuyến nghị tạo **Console trước**, Terraform **import** hoặc chỉ quản lý OU/SCP.

---

## SCP

```hcl
resource "aws_organizations_policy" "deny_regions" {
  name    = "DenyOutsideSingapore"
  type    = "SERVICE_CONTROL_POLICY"
  content = file("${path.module}/../../policies/scp-deny-regions.json")
}

resource "aws_organizations_policy_attachment" "sandbox" {
  policy_id = aws_organizations_policy.deny_regions.id
  target_id = aws_organizations_organizational_unit.sandbox.id
}
```

Module: [terraform/modules/scp](../terraform/modules/scp/)

---

## Environment layout

```
terraform/environments/management/  # OU, SCP, org data
terraform/environments/dev-role/    # role trong dev (provider assume_role)
```

---

## Lab

→ [Lab 08 — Terraform org](../labs/advanced/lab08-terraform-org.md)

**Tiếp:** [07-terraform-iam-roles.md](07-terraform-iam-roles.md)

# Terraform — IAM Cross-Account & assume_role

## Module cross-account role

Deploy trong **member account** (Dev) — trust management account.

File: [terraform/modules/cross-account-role/main.tf](../terraform/modules/cross-account-role/main.tf)

```hcl
module "devops_role" {
  source = "../../modules/cross-account-role"

  role_name              = "DevOpsCrossAccountRole"
  management_account_id  = var.management_account_id
  external_id            = "lab-module-22-dev"
  policy_json            = file("${path.module}/../../policies/devops-scoped.json")
}
```

---

## Provider assume_role (chạy Terraform từ laptop)

Deploy resource **trong Dev** mà credentials gốc là Management:

```hcl
provider "aws" {
  alias  = "dev"
  region = var.aws_region

  assume_role {
    role_arn     = "arn:aws:iam::${var.dev_account_id}:role/OrganizationAccountAccessRole"
    session_name = "terraform-module-22"
  }
}

resource "aws_s3_bucket" "dev_app" {
  provider = aws.dev
  bucket   = "app-dev-${var.dev_account_id}-lab"
}
```

Environment: [terraform/environments/dev-workload](../terraform/environments/dev-workload/)

---

## Multi-provider pattern

```hcl
provider "aws" {
  alias  = "management"
  region = "ap-southeast-1"
}

provider "aws" {
  alias  = "dev"
  region = "ap-southeast-1"
  assume_role {
    role_arn = var.dev_role_arn
  }
}
```

---

## S3 bucket policy (Terraform)

```hcl
resource "aws_s3_bucket_policy" "audit" {
  provider = aws.management
  bucket   = aws_s3_bucket.audit_logs.id
  policy   = templatefile("${path.module}/bucket-policy.tpl", {
    dev_account_id = var.dev_account_id
    dev_role_name  = var.devops_role_name
  })
}
```

---

## Import role đã tạo Console

```bash
terraform import module.devops_role.aws_iam_role.this DevOpsCrossAccountRole
```

So sánh `terraform plan` — drift = 0 nếu khớp Console.

---

## Lab

→ [Lab 09](../labs/advanced/lab09-terraform-iam.md), [Lab 10](../labs/advanced/lab10-capstone.md)

**Tiếp:** [08-best-practices.md](08-best-practices.md)

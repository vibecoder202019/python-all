# Terraform nâng cao

## Modules — Tái sử dụng code

Module = thư mục chứa `.tf` riêng, gọi từ project cha:

```hcl
# terraform/04-modules/main.tf
module "app_config" {
  source      = "./modules/config-file"
  environment = var.environment
  app_name    = "demo-api"
}
```

```hcl
# modules/config-file/main.tf
variable "environment" { type = string }
variable "app_name"    { type = string }

resource "local_file" "config" {
  filename = "${path.module}/../../output/${var.app_name}-${var.environment}.json"
  content  = jsonencode({
    app         = var.app_name
    environment = var.environment
  })
}
```

**Lợi ích:** DRY — một module dùng cho dev/staging/prod với biến khác nhau.

---

## Remote State

Local state không phù hợp team. **Remote backend** lưu state tập trung (S3, GCS, Terraform Cloud, hoặc **local path** cho lab).

```hcl
terraform {
  backend "local" {
    path = "../state/04-modules.tfstate"
  }
}
```

Production thường dùng:

```hcl
# Ví dụ AWS S3 (Module 13 — cần AWS creds)
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "ap-southeast-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

**State locking:** Tránh 2 người `apply` đồng thời — DynamoDB hoặc native lock backend.

---

## Workspace

Tách state theo môi trường trên **cùng code**:

```bash
terraform workspace new dev
terraform workspace new prod
terraform workspace select dev
terraform apply -var="environment=dev"
```

Mỗi workspace = file state riêng (`terraform.tfstate.d/`).

---

## count vs for_each

```hcl
# count — index số
variable "users" { default = ["alice", "bob"] }
resource "local_file" "user" {
  count    = length(var.users)
  filename = "${path.module}/output/user-${count.index}.txt"
  content  = var.users[count.index]
}

# for_each — map/set (khuyến nghị khi key ổn định)
resource "local_file" "user_map" {
  for_each = toset(var.users)
  filename = "${path.module}/output/${each.key}.txt"
  content  = each.key
}
```

---

## Lifecycle

```hcl
resource "local_file" "important" {
  filename = "${path.module}/output/important.txt"
  content  = "data"

  lifecycle {
    prevent_destroy = true   # Không cho terraform destroy xóa
    ignore_changes  = [content]  # Bỏ qua thay đổi content khi apply
  }
}
```

---

## Data sources

Đọc resource có sẵn (không quản lý lifecycle):

```hcl
data "local_file" "existing" {
  filename = "${path.module}/output/hello.txt"
}

output "existing_content" {
  value = data.local_file.existing.content
}
```

---

## Provisioners (hạn chế dùng)

Chạy script trên máy local hoặc remote sau khi tạo resource — **chỉ khi không có cách khác**:

```hcl
resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "echo 'Resource created'"
  }
}
```

Best practice: dùng **cloud-init**, **Ansible**, hoặc **CI/CD** thay local-exec.

---

## Lab module

| Thư mục | Chủ đề |
|---------|--------|
| `terraform/03-local-resources/` | count, for_each |
| `terraform/04-modules/` | module con |
| `terraform/04-remote-state/` | backend local path |

---

## Best practices

1. **Luôn** `terraform plan` trước `apply`
2. **Không** commit `.tfstate`, `.terraform/`
3. Dùng **`.tfvars`** cho giá trị nhạy cảm (gitignore) — hoặc Vault
4. Pin provider version: `version = "~> 2.4"`
5. Format: `terraform fmt -recursive`

**Tiếp theo:** [04-vault-co-ban.md](04-vault-co-ban.md)

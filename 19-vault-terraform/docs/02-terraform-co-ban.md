# Terraform cơ bản

## Terraform là gì?

**Terraform** = công cụ **Infrastructure as Code (IaC)** của HashiCorp. Bạn mô tả hạ tầng bằng file **HCL** (HashiCorp Configuration Language), Terraform so sánh với thực tế và tạo/sửa/xóa resource.

**Ví von:** Terraform như **công thức nấu ăn** — ghi rõ nguyên liệu (resource), lần sau làm lại y hệt, chia sẻ được với team.

---

## Workflow cơ bản

```
┌─────────┐    ┌──────┐    ┌───────┐    ┌────────┐
│  .tf    │───▶│ init │───▶│ plan  │───▶│ apply  │
│  files  │    └──────┘    └───────┘    └────────┘
└─────────┘         │           │            │
                    ▼           ▼            ▼
              Download      Preview      Create/
              providers     changes      update
                            (diff)       resources
```

| Lệnh | Mục đích |
|------|----------|
| `terraform init` | Tải provider, khởi tạo backend |
| `terraform fmt` | Format file `.tf` chuẩn |
| `terraform validate` | Kiểm tra syntax |
| `terraform plan` | Xem thay đổi **trước** khi apply |
| `terraform apply` | Áp dụng thay đổi |
| `terraform destroy` | Xóa toàn bộ resource trong state |

---

## Cấu trúc file `.tf`

```hcl
# main.tf — resource chính
terraform {
  required_version = ">= 1.6"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

provider "local" {}

resource "local_file" "hello" {
  filename = "${path.module}/output/hello.txt"
  content  = "Xin chao tu Terraform!"
}
```

| Block | Ý nghĩa |
|-------|---------|
| `terraform {}` | Phiên bản Terraform + providers cần dùng |
| `provider "" {}` | Cấu hình plugin (AWS region, Vault addr...) |
| `resource "TYPE" "NAME" {}` | Một resource cụ thể |
| `data "" "" {}` | Đọc dữ liệu có sẵn (không tạo mới) |
| `variable "" {}` | Input |
| `output "" {}` | Output sau apply |

---

## Variables & Outputs

```hcl
# variables.tf
variable "environment" {
  description = "Ten moi truong: dev, staging, prod"
  type        = string
  default     = "dev"
}

# main.tf — dùng biến
resource "local_file" "env" {
  filename = "${path.module}/output/${var.environment}.txt"
  content  = "Env: ${var.environment}"
}

# outputs.tf
output "file_path" {
  description = "Duong dan file da tao"
  value       = local_file.env.filename
}
```

Truyền biến khi chạy:

```bash
terraform apply -var="environment=staging"
# hoặc
export TF_VAR_environment=staging
terraform apply
```

---

## State file (`.tfstate`)

Terraform lưu **ánh xạ** giữa resource trong code và resource thật.

- File: `terraform.tfstate` (local backend)
- **Không commit** state có secret lên Git public
- Mất state = Terraform "quên" resource đã tạo

Lab module dùng local state trong thư mục `.terraform/` và `terraform.tfstate` — `.gitignore` đã loại trừ.

---

## Ví dụ trong module

| Thư mục | Nội dung |
|---------|----------|
| `terraform/01-hello/` | File local đầu tiên |
| `terraform/02-variables/` | variables + outputs |
| `terraform/03-local-resources/` | count, for_each |

Chạy:

```bash
bash scripts/03-run-terraform.sh 01-hello
bash scripts/03-run-terraform.sh 02-variables
```

---

## Giải thích chi tiết lệnh (lab 01)

```bash
cd terraform/01-hello
terraform init      # Tải provider hashicorp/local
terraform plan      # + local_file.hello sẽ được tạo
terraform apply     # Gõ yes — tạo file output/hello.txt
terraform show      # Xem state hiện tại
cat output/hello.txt
terraform destroy   # Xóa resource, dọn lab
```

---

## FAQ

**Q: Provider là gì?**  
Plugin kết nối Terraform với API (AWS, Azure, Vault, local file...).

**Q: `path.module` là gì?**  
Đường dẫn thư mục chứa module hiện tại — dùng cho path file tương đối.

**Q: Plan báo "No changes"?**  
Code khớp state — không cần apply.

**Tiếp theo:** [03-terraform-nang-cao.md](03-terraform-nang-cao.md)

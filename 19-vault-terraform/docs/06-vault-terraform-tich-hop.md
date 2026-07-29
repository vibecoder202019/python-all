# Tích hợp Vault + Terraform

## Vấn đề cần giải

```hcl
# ❌ KHÔNG làm thế này
variable "db_password" {
  default = "super-secret-123"  # Lộ trong Git history
}
```

```hcl
# ✅ Lấy secret từ Vault
data "vault_kv_secret_v2" "db" {
  mount = "secret"
  name  = "myapp/db"
}

resource "local_file" "app_env" {
  content = "DB_USER=${data.vault_kv_secret_v2.db.data["username"]}\nDB_PASS=${data.vault_kv_secret_v2.db.data["password"]}"
  filename = "${path.module}/output/.env.generated"
}
```

---

## Cấu hình Vault Provider

```hcl
terraform {
  required_providers {
    vault = {
      source  = "hashicorp/vault"
      version = "~> 4.0"
    }
  }
}

provider "vault" {
  address = var.vault_address
  # token lấy từ env VAULT_TOKEN — không hardcode
}
```

Biến môi trường trước khi apply:

```bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'   # lab only — production: AppRole token

cd terraform/05-vault-provider
terraform init && terraform apply
```

---

## Luồng lab Module 19

```
1. vault kv put secret/myapp/db username=admin password=...
2. Terraform data source đọc secret
3. Terraform tạo file config / mock resource dùng creds
4. Không có password trong .tf files
```

Thư mục: `terraform/05-vault-provider/`

---

## Terraform backend credentials trong Vault

Production pattern:

1. Lưu AWS keys cho state backend trong Vault path `secret/terraform/aws`
2. CI job: AppRole login → export creds → `terraform init/apply`
3. State bucket encrypted (S3 SSE)

```bash
vault kv put secret/terraform/aws \
  access_key=AKIA... \
  secret_key=...
```

Script tham khảo: `vault/scripts/inject-tf-creds.sh.example`

---

## Vault Provider — Resource vs Data

| Loại | Ví dụ | Dùng khi |
|------|-------|----------|
| **data** | `vault_kv_secret_v2` | **Đọc** secret có sẵn |
| **resource** | `vault_kv_secret_v2` | **Tạo/quản lý** secret bằng Terraform |
| **resource** | `vault_policy` | Quản lý policy as code |

Quản lý secret bằng Terraform (GitOps):

```hcl
resource "vault_kv_secret_v2" "app" {
  mount = "secret"
  name  = "myapp/config"
  data_json = jsonencode({
    api_key = var.api_key  # từ TF_VAR hoặc CI secret
  })
}
```

**Trade-off:** Secret trong state file — cần remote state encrypted + access control.

---

## Project capstone

`terraform/project/` — stack đầy đủ:

- Module config file từ Vault
- Variables per environment
- Output không in password ra console (`sensitive = true`)

```bash
bash scripts/03-run-terraform.sh project
```

Lab: [lab12-capstone.md](../labs/advanced/lab12-capstone.md)

---

## Best practices tích hợp

1. **CI:** AppRole → short-lived token → terraform apply
2. **Mark sensitive:** `sensitive = true` trên output chứa secret
3. **State encryption:** S3 + KMS hoặc Terraform Cloud
4. **Separate roles:** Terraform plan (read) vs apply (write) policies khác nhau
5. **Rotation:** Dynamic secrets > static KV khi có thể

---

## Liên kết

- [Terraform Vault Provider docs](https://registry.terraform.io/providers/hashicorp/vault/latest/docs)
- Module 13 — apply cùng pattern lên AWS
- Cheatsheet: [cheatsheet/vault-terraform.md](../cheatsheet/vault-terraform.md)

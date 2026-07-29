# Cài đặt HashiCorp Vault & Terraform

Hướng dẫn cài đặt chi tiết trên **macOS**, **Linux** và **Windows (WSL)** — kèm giải thích từng bước.

---

## 1. Cài Terraform

### macOS (Homebrew — khuyến nghị)

```bash
# Cài Terraform qua Homebrew
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

# Kiểm tra phiên bản
terraform version
# Output ví dụ: Terraform v1.9.x
```

| Lệnh | Giải thích |
|------|------------|
| `brew tap hashicorp/tap` | Thêm repo chính thức HashiCorp vào Homebrew |
| `brew install hashicorp/tap/terraform` | Cài binary `terraform` vào PATH |
| `terraform version` | Xác nhận cài thành công |

### Linux (apt — Ubuntu/Debian)

```bash
# Thêm GPG key và repo HashiCorp
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

# Cài Terraform
sudo apt update && sudo apt install terraform

terraform version
```

### Linux / macOS (tfenv — quản lý nhiều phiên bản)

```bash
# Cài tfenv (macOS)
brew install tfenv

# Cài Terraform 1.9.x và dùng
tfenv install 1.9.8
tfenv use 1.9.8
terraform version
```

### Windows

1. Tải ZIP: https://developer.hashicorp.com/terraform/install
2. Giải nén, thêm thư mục vào **PATH**
3. Hoặc dùng **WSL2** + lệnh Linux ở trên (khuyến nghị cho DevOps)

---

## 2. Cài Vault

### macOS

```bash
brew tap hashicorp/tap
brew install hashicorp/tap/vault
vault version
```

### Linux (apt)

```bash
# Dùng cùng repo HashiCorp như Terraform (bước trên)
sudo apt update && sudo apt install vault
vault version
```

### Docker (Vault server — giống production hơn dev mode)

```bash
# Chạy Vault trong container (lab module)
cd 19-vault-terraform/vault
docker compose up -d

# Kiểm tra
docker compose ps
export VAULT_ADDR='http://127.0.0.1:8200'
vault status
```

File `vault/docker-compose.yaml` trong module — Vault lắng nghe port **8200**.

---

## 3. Công cụ bổ trợ

```bash
# jq — parse JSON (Vault API, terraform output -json)
brew install jq          # macOS
sudo apt install jq      # Ubuntu

# direnv — tự load .envrc (tùy chọn)
brew install direnv
```

---

## 4. Script tự động (module)

```bash
# Chỉ kiểm tra
bash 19-vault-terraform/scripts/01-install-tools.sh --check

# Cài qua Homebrew (macOS)
bash 19-vault-terraform/scripts/01-install-tools.sh --install
```

---

## 5. Khởi động Vault cho lab

### Dev mode (nhanh nhất — học cơ bản)

```bash
bash 19-vault-terraform/scripts/02-setup-vault-dev.sh
```

Script sẽ:
1. Export `VAULT_ADDR=http://127.0.0.1:8200`
2. Chạy `vault server -dev` (root token in ra màn hình)
3. Enable KV v2 engine `secret/`

**Lưu ý:** Dev mode **không** dùng production — data mất khi tắt process.

### Production-like (Docker Compose)

```bash
cd 19-vault-terraform/vault
docker compose up -d
# Init/unseal: xem README trong vault/
```

---

## 6. Biến môi trường quan trọng

| Biến | Giá trị lab | Ý nghĩa |
|------|-------------|---------|
| `VAULT_ADDR` | `http://127.0.0.1:8200` | URL Vault server |
| `VAULT_TOKEN` | root token (dev) hoặc token app | Xác thực CLI/API |
| `TF_VAR_*` | tùy project | Inject biến vào Terraform không cần `-var` |

Thêm vào `~/.zshrc` hoặc file `.envrc` trong thư mục lab:

```bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'   # CHỈ dev mode — đổi token thật khi học policy
```

---

## 7. Kiểm tra cài đặt hoàn chỉnh

```bash
terraform version
vault version
jq --version

# Vault đang chạy?
export VAULT_ADDR='http://127.0.0.1:8200'
vault status

# Terraform chạy được?
bash 19-vault-terraform/scripts/03-run-terraform.sh 01-hello
```

Nếu tất cả OK → chuyển sang [02-terraform-co-ban.md](02-terraform-co-ban.md).

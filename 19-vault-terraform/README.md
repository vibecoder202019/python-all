# Module 19: Tự học HashiCorp Vault + Terraform — Cơ bản đến Nâng cao

Lộ trình **tự học** **Terraform** (Infrastructure as Code) và **HashiCorp Vault** (quản lý secrets) — lý thuyết chi tiết, cài đặt từng bước, lab thực hành local (không bắt buộc AWS).

> **Liên quan:** Module 13 (AWS + boto3), Module 15–18 (K8s/DevOps). Module này dùng provider `local`/`random`/`null` để học offline; có ví dụ AWS tùy chọn.

---

## Mục tiêu

| Công cụ | Bạn sẽ học được |
|---------|-----------------|
| **Terraform** | HCL, state, plan/apply, variables, modules, remote state, Vault provider |
| **Vault** | Dev/prod mode, KV v2, policies, AppRole, dynamic secrets, audit |
| **Tích hợp** | Terraform đọc secret từ Vault; Vault lưu Terraform state credentials |

---

## Vault vs Terraform — Khác nhau thế nào?

| | **Terraform** | **Vault** |
|---|---------------|-----------|
| **Mục đích** | **Tạo/sửa/xóa** hạ tầng (IaC) | **Lưu trữ & cấp phát** secrets an toàn |
| **Output chính** | Resource trên cloud/K8s/local | Token, password, cert động |
| **State** | `.tfstate` (quan trọng!) | Không có state file kiểu Terraform |
| **Ví dụ** | Tạo EC2, S3, namespace K8s | Lưu DB password, API key, PKI |

**Kết hợp:** Terraform **không** hardcode password — lấy từ Vault qua provider `hashicorp/vault`.

---

## Yêu cầu môi trường

| Công cụ | Phiên bản | Mục đích |
|---------|-----------|----------|
| **Terraform** | ≥ 1.6 | IaC |
| **Vault** | ≥ 1.15 | Secrets |
| **Docker** | (tùy chọn) | Vault production-like local |
| **jq** | (khuyến nghị) | Parse JSON CLI |

```bash
# Cài đặt + kiểm tra (macOS/Linux)
bash 19-vault-terraform/scripts/01-install-tools.sh --check

# Cài nếu thiếu (Homebrew trên macOS)
bash 19-vault-terraform/scripts/01-install-tools.sh --install
```

Chi tiết cài đặt: [docs/01-cai-dat.md](docs/01-cai-dat.md)

---

## Lộ trình học (6–8 tuần)

```
Tuần 1–2:  Cài đặt + Terraform cơ bản (docs 01–02, lab 01–03)
Tuần 3:    Terraform nâng cao — modules, remote state (docs 03, lab 04–06)
Tuần 4:    Vault cơ bản — KV, policy, token (docs 04, lab 07–08)
Tuần 5:    Vault nâng cao — AppRole, dynamic DB (docs 05, lab 09–10)
Tuần 6–7:  Tích hợp Vault + Terraform (docs 06, lab 11–12)
Tuần 8:    Dự án tổng hợp + mock interview
```

---

## Cấu trúc module

```
19-vault-terraform/
├── README.md
├── docs/                     # Lý thuyết chi tiết
│   ├── 00-lo-trinh.md
│   ├── 01-cai-dat.md
│   ├── 02-terraform-co-ban.md
│   ├── 03-terraform-nang-cao.md
│   ├── 04-vault-co-ban.md
│   ├── 05-vault-nang-cao.md
│   └── 06-vault-terraform-tich-hop.md
├── terraform/                # Ví dụ Terraform (01 → 05 + project)
├── vault/                    # Policy, docker-compose, config mẫu
├── labs/                     # 12 lab hands-on
├── scripts/                  # Cài đặt, chạy lab, verify
├── cheatsheet/               # Lệnh hay dùng
└── exercises/                # Bài tập + đáp án
```

---

## Chạy nhanh (15 phút)

```bash
cd learn-python-ai   # hoặc python-all

# 1. Kiểm tra / cài Terraform + Vault
bash 19-vault-terraform/scripts/01-install-tools.sh --check

# 2. Khởi động Vault dev mode (terminal 1)
bash 19-vault-terraform/scripts/02-setup-vault-dev.sh

# 3. Chạy Terraform hello world (terminal 2)
bash 19-vault-terraform/scripts/03-run-terraform.sh 01-hello

# 4. Lab đầu tiên
cat 19-vault-terraform/labs/basic/lab01-terraform-init.md
```

---

## Lab thực hành (12 lab)

| # | Lab | Level | Thời gian |
|---|-----|-------|-----------|
| 01 | [Terraform init & plan](labs/basic/lab01-terraform-init.md) | Basic | 30 phút |
| 02 | [Variables & outputs](labs/basic/lab02-variables-outputs.md) | Basic | 30 phút |
| 03 | [Local files & count](labs/basic/lab03-local-resources.md) | Basic | 45 phút |
| 04 | [Modules](labs/intermediate/lab04-modules.md) | Intermediate | 45 phút |
| 05 | [Remote state local](labs/intermediate/lab05-remote-state.md) | Intermediate | 60 phút |
| 06 | [Workspace & lifecycle](labs/intermediate/lab06-workspaces.md) | Intermediate | 45 phút |
| 07 | [Vault dev & KV v2](labs/basic/lab07-vault-kv.md) | Basic | 45 phút |
| 08 | [Policies & tokens](labs/intermediate/lab08-vault-policies.md) | Intermediate | 60 phút |
| 09 | [AppRole auth](labs/advanced/lab09-approle.md) | Advanced | 60 phút |
| 10 | [Dynamic secrets (mock)](labs/advanced/lab10-dynamic-secrets.md) | Advanced | 60 phút |
| 11 | [Terraform + Vault provider](labs/advanced/lab11-terraform-vault.md) | Advanced | 90 phút |
| 12 | [Project tổng hợp](labs/advanced/lab12-capstone.md) | Advanced | 120 phút |

---

## Tài liệu đọc theo thứ tự

1. [Lộ trình](docs/00-lo-trinh.md)
2. [Cài đặt Vault & Terraform](docs/01-cai-dat.md)
3. [Terraform cơ bản](docs/02-terraform-co-ban.md)
4. [Terraform nâng cao](docs/03-terraform-nang-cao.md)
5. [Vault cơ bản](docs/04-vault-co-ban.md)
6. [Vault nâng cao](docs/05-vault-nang-cao.md)
7. [Tích hợp Vault + Terraform](docs/06-vault-terraform-tich-hop.md)

---

## Liên kết module liên quan

- [Module 13 — AWS Infra](../13-python-aws-infra/README.md) — apply Terraform lên AWS thật
- [Module 15 — AWX + MinIO + K8s](../15-ansible-awx-minio-k8s/README.md)
- [Module 18 — CKA/CKS](../18-cka-cks-kubernetes/README.md)

## Tài liệu chính thức

- [Terraform Docs](https://developer.hashicorp.com/terraform/docs)
- [Vault Docs](https://developer.hashicorp.com/vault/docs)
- [Terraform Vault Provider](https://registry.terraform.io/providers/hashicorp/vault/latest/docs)

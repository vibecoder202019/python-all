# Module 22: AWS Multi-Account — Console → Terraform

Hướng dẫn **quản lý multi-account AWS**: Organizations, OU, phân quyền, **IAM Role cross-account**, truy cập resource — **step-by-step trên Console**, sau đó **chuyển sang Terraform**.

> **Tiên quyết:** [Module 13 — AWS + boto3](../13-python-aws-infra/README.md), [Module 19 — Terraform](../19-vault-terraform/README.md).

---

## Mục tiêu

| Giai đoạn | Bạn học được |
|-----------|--------------|
| **Console** | Tạo Organization, OU, account member, IAM Identity Center, role assume |
| **Phân quyền** | SCP, trust policy, permission boundary, least privilege |
| **Resource** | Cross-account S3, EC2 assume role, centralized logging account |
| **Terraform** | `aws_organizations_*`, `aws_iam_role`, provider `assume_role`, module tái sử dụng |

---

## Kiến trúc lab (mô hình chuẩn)

```
                    ┌─────────────────────────┐
                    │  Management Account     │
                    │  (Organizations root)   │
                    │  + IAM Identity Center  │
                    └───────────┬─────────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
   ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
   │ OU: Security│      │ OU: Workload│      │ OU: Sandbox │
   │ Account Log │      │ Dev / Prod  │      │ Lab         │
   └─────────────┘      └─────────────┘      └─────────────┘
```

| Account | Mục đích lab |
|---------|--------------|
| **Management** | Organizations, billing, SSO, SCP |
| **Dev** | Developer assume role, deploy EC2/S3 |
| **Audit/Log** (tùy chọn) | Central S3 logs |

---

## ⚠️ Chi phí & cảnh báo

- Tạo **account member** trong Organizations **miễn phí**, nhưng resource (EC2, S3…) **có phí**
- Module khuyến nghị **2 account** tối thiểu (management + 1 workload)
- Terraform `aws_organizations_account` **tạo account thật** — dùng `--apply` cẩn thận
- Lab EC2/S3: dùng `--apply` có kiểm soát + `destroy` sau khi học

---

## Yêu cầu

| Công cụ | Mục đích |
|---------|----------|
| Tài khoản AWS | Quyền **root hoặc admin** lần đầu enable Organizations |
| AWS CLI v2 | `aws sts get-caller-identity` |
| Terraform ≥ 1.6 | IaC phase |
| 2+ AWS accounts (hoặc tạo trong lab) | Cross-account role |

```bash
bash 22-aws-multi-account/scripts/01-check-prerequisites.sh
```

---

## Lộ trình (3–4 tuần)

```
Tuần 1:  Kiến trúc + Console Organizations (docs 01–02, lab 01–02)
Tuần 2:  IAM Role cross-account + SSO (docs 03–05, lab 03–05)
Tuần 3:  SCP + resource policies (doc 04, lab 06)
Tuần 4:  Terraform toàn bộ (docs 06–07, lab 07–10)
```

---

## Chạy nhanh

```bash
# Kiểm tra credentials
bash 22-aws-multi-account/scripts/01-check-prerequisites.sh

# Xem lab Console bước 1
bash 22-aws-multi-account/scripts/02-run-lab.sh 01

# Terraform (sau khi có account IDs)
cd 22-aws-multi-account/terraform/environments/dev
cp terraform.tfvars.example terraform.tfvars   # điền account IDs
terraform init && terraform plan
```

---

## Cấu trúc module

```
22-aws-multi-account/
├── README.md
├── docs/                 # Console + Terraform chi tiết
├── console/              # Checklist từng bước Console
├── terraform/
│   ├── modules/          # cross-account-role, scp, ou
│   └── environments/     # management, dev-workload
├── policies/             # JSON IAM/SCP mẫu
├── labs/                 # 10 lab
├── scripts/
├── cheatsheet/
└── exercises/
```

---

## Lab (10 lab)

| # | Lab | Console / TF |
|---|-----|--------------|
| 01 | [Enable Organizations](labs/basic/lab01-enable-organizations.md) | Console |
| 02 | [Tạo OU & Account member](labs/basic/lab02-ou-accounts.md) | Console |
| 03 | [IAM Identity Center (SSO)](labs/basic/lab03-identity-center.md) | Console |
| 04 | [Cross-account role DevOps](labs/intermediate/lab04-cross-account-role.md) | Console |
| 05 | [Assume role CLI](labs/intermediate/lab05-assume-role-cli.md) | Console + CLI |
| 06 | [SCP giới hạn region](labs/intermediate/lab06-scp.md) | Console |
| 07 | [S3 cross-account](labs/intermediate/lab07-s3-cross-account.md) | Console |
| 08 | [Terraform OU + SCP](labs/advanced/lab08-terraform-org.md) | Terraform |
| 09 | [Terraform cross-account roles](labs/advanced/lab09-terraform-iam.md) | Terraform |
| 10 | [Capstone landing zone mini](labs/advanced/lab10-capstone.md) | Both |

---

## Tài liệu

1. [Lộ trình](docs/00-lo-trinh.md)
2. [Kiến trúc multi-account](docs/01-kien-truc-multi-account.md)
3. [Console — Organizations](docs/02-console-organizations.md)
4. [Console — IAM Roles cross-account](docs/03-console-iam-cross-account.md)
5. [Console — SCP & phân quyền](docs/04-console-scp-permissions.md)
6. [Console — Truy cập resource](docs/05-console-resource-access.md)
7. [Terraform — Organizations](docs/06-terraform-organizations.md)
8. [Terraform — IAM & provider assume_role](docs/07-terraform-iam-roles.md)
9. [Best practices](docs/08-best-practices.md)

---

## Liên kết

- [Module 13 — boto3](../13-python-aws-infra/README.md)
- [Module 19 — Terraform](../19-vault-terraform/README.md)
- [AWS Organizations Docs](https://docs.aws.amazon.com/organizations/)

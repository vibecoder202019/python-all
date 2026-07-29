# Lộ trình Module 22

## Phase 1 — Console (Tuần 1–2)

| Lab | Nội dung |
|-----|----------|
| 01 | Bật AWS Organizations |
| 02 | OU + account Dev |
| 03 | IAM Identity Center — user/group |
| 04 | Role `OrganizationAccountAccessRole` + custom DevOps role |
| 05 | `aws sts assume-role` |
| 06 | SCP deny region / service |
| 07 | S3 bucket policy cross-account |

**Checkpoint:** Từ management account assume role vào Dev account, list S3.

---

## Phase 2 — Terraform (Tuần 3–4)

| Lab | Nội dung |
|-----|----------|
| 08 | Import/data source Organization, OU, SCP |
| 09 | Module `cross-account-role` deploy multi-provider |
| 10 | Capstone: tfvars 3 account IDs, plan/apply role + S3 policy |

**Checkpoint:** `terraform plan` khớp cấu hình đã làm Console.

---

## Thứ tự đọc docs

Console trước → Terraform mirror:

```
02-console-organizations  →  06-terraform-organizations
03-console-iam            →  07-terraform-iam-roles
04-console-scp            →  terraform/modules/scp
05-console-resource       →  terraform/modules/s3-cross-account
```

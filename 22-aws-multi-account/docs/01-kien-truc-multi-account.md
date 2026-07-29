# Kiến trúc AWS Multi-Account

## Tại sao nhiều account?

| 1 account duy nhất | Multi-account |
|--------------------|---------------|
| Blast radius lớn | Lỗi prod không ảnh hưởng billing |
| Khó phân quyền | Dev/Prod/Security tách biệt |
| Compliance khó | Audit account riêng |

**Ví von:** Một account = một căn hộ; Organization = tòa nhà — mỗi phòng (account) có chìa riêng (IAM role).

---

## Thành phần chính

| Thành phần | Vai trò |
|------------|---------|
| **Management account** | Root Organizations, billing tổng, không chạy workload prod |
| **Member account** | Account con trong org |
| **OU** (Organizational Unit) | Nhóm account (Security, Workloads, Sandbox) |
| **SCP** | Guardrail — giới hạn tối đa quyền (không grant thêm) |
| **IAM Identity Center** | SSO — user đăng nhập 1 lần, vào nhiều account |
| **Cross-account role** | Account A assume role Account B |

---

## Luồng truy cập (developer)

```
User ──► IAM Identity Center (SSO) ──► Permission Set ──► Role in Dev Account ──► EC2/S3
```

Hoặc CLI:

```
User credentials (management) ──► sts:AssumeRole ──► DevAccountRole ──► API calls
```

---

## Mô hình lab module

| Account alias | Account ID (điền của bạn) |
|---------------|---------------------------|
| management | `111111111111` |
| dev-workload | `222222222222` |
| audit (optional) | `333333333333` |

Lưu IDs vào `terraform/environments/*/terraform.tfvars` — **không commit file tfvars thật**.

---

## Terraform vs Console

| Việc | Console (lần đầu) | Terraform (duy trì) |
|------|-------------------|---------------------|
| Enable Organizations | ✅ Dễ | ⚠️ One-time, import state |
| Tạo account mới | ✅ Wizard | `aws_organizations_account` (chậm ~5 phút) |
| OU, SCP | ✅ | ✅ Lặp lại được |
| IAM role trust | ✅ Visual | ✅ Code review được |
| SSO users | ✅ Identity Center UI | `aws_ssoadmin_*` (phức tạp hơn) |

**Chiến lược module:** Học **Console** hiểu bản chất → **Terraform** automate phần lặp.

---

## Tiếp theo

→ [02-console-organizations.md](02-console-organizations.md)

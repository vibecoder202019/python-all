# Console — AWS Organizations (Step by Step)

Hướng dẫn chi tiết trên **AWS Management Console**. Đăng nhập bằng **root hoặc admin** account sẽ trở thành **management account**.

---

## Bước 1 — Kiểm tra account hiện tại

1. Mở https://console.aws.amazon.com/
2. Góc phải trên → click **Account name** → copy **Account ID**
3. Terminal:

```bash
aws sts get-caller-identity
```

Ghi **Account**, **Arn** — đây là management candidate.

---

## Bước 2 — Mở AWS Organizations

1. Ô tìm kiếm Console → gõ **Organizations**
2. Chọn **AWS Organizations**
3. Nếu chưa bật → **Create an organization**
4. Chọn **Enable all features** (khuyến nghị — full Organizations)

| Tùy chọn | Ý nghĩa |
|----------|---------|
| **All features** | SCP, consolidated billing, full API |
| Consolidated billing only | Chỉ gom bill (legacy) |

5. **Create organization** → Confirm

---

## Bước 3 — Xem cây Organization

1. Menu trái → **AWS accounts**
2. Thấy **Root** chứa management account
3. **Invite account** hoặc **Add an AWS account** (tạo mới)

---

## Bước 4 — Tạo Organizational Unit (OU)

1. Chọn **Root** → **Actions** → **Create new OU**
2. Name: `Workloads`
3. Repeat: tạo OU `Security`, `Sandbox`

Cấu trúc lab:

```
Root
├── Security
├── Workloads
│   └── (sẽ thêm Dev account)
└── Sandbox
```

---

## Bước 5 — Tạo account member (Dev)

1. **AWS accounts** → **Add an AWS account** → **Create an account**
2. Điền:
   - **AWS account name:** `dev-workload`
   - **Email:** email **duy nhất** chưa dùng AWS (vd: `aws-dev-workload+lab@yourdomain.com`)
   - **IAM role name:** `OrganizationAccountAccessRole` (mặc định — **giữ nguyên**)
3. **Create account**
4. Đợi ~5 phút — status **ACTIVE**
5. Kéo account vào OU **Workloads**

> Email nhận invite — lưu password root member account an toàn (break-glass only).

---

## Bước 6 — Consolidated billing (xem)

1. **Billing** → **Consolidated billing** (hoặc Billing console từ management)
2. Xác nhận member account xuất hiện dưới management

---

## Bước 7 — Ghi chép thông tin cho Terraform

| Field | Value |
|-------|-------|
| Management Account ID | |
| Dev Account ID | |
| Organization ID | `o-xxxxxxxxxx` (Organizations → Settings) |
| Dev Role ARN | `arn:aws:iam::DEV_ID:role/OrganizationAccountAccessRole` |

---

## Verify

```bash
aws organizations describe-organization
aws organizations list-accounts
```

---

## Lab

→ [Lab 01](../labs/basic/lab01-enable-organizations.md), [Lab 02](../labs/basic/lab02-ou-accounts.md)

**Tiếp:** [03-console-iam-cross-account.md](03-console-iam-cross-account.md)

# Console — IAM Cross-Account Roles

## Role mặc định: OrganizationAccountAccessRole

Khi tạo account qua Organizations, AWS tạo role:

```
arn:aws:iam::MEMBER_ACCOUNT_ID:role/OrganizationAccountAccessRole
```

**Trust policy:** cho phép **management account root** assume (full admin — chỉ break-glass).

Lab: tạo role **least privilege** cho DevOps hàng ngày.

---

## Bước 1 — Đăng nhập account Dev (member)

1. Switch role từ management:
   - Console góc phải → account dropdown → **Switch role**
   - **Account:** Dev Account ID
   - **Role:** `OrganizationAccountAccessRole`
   - **Display name:** `DevAdmin`
2. Hoặc dùng SSO (lab 03)

---

## Bước 2 — Tạo role DevOps (trong Dev account)

1. **IAM** → **Roles** → **Create role**
2. **Trusted entity type:** AWS account
3. **Another AWS account** → nhập **Management Account ID**
4. ☑ **Require external ID** (optional lab — chống confused deputy)
   - External ID: `lab-module-22-dev`
5. Next → Attach policy: **PowerUserAccess** (lab) hoặc custom policy scoped
6. Role name: `DevOpsCrossAccountRole`
7. **Create role**

---

## Bước 3 — Trust policy (giải thích)

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "AWS": "arn:aws:iam::MANAGEMENT_ID:root" },
    "Action": "sts:AssumeRole",
    "Condition": {
      "StringEquals": { "sts:ExternalId": "lab-module-22-dev" }
    }
  }]
}
```

| Field | Ý nghĩa |
|-------|---------|
| `Principal.AWS` | Ai được assume |
| `sts:AssumeRole` | Hành động assume |
| `ExternalId` | Shared secret chống abuse |

File mẫu: [policies/trust-devops-role.json](../policies/trust-devops-role.json)

---

## Bước 4 — Permission policy (scoped)

Attach policy chỉ S3 + EC2 read (lab):

1. Role `DevOpsCrossAccountRole` → **Add permissions** → **Create inline policy**
2. JSON → paste [policies/devops-scoped.json](../policies/devops-scoped.json)
3. Review → Create

---

## Bước 5 — IAM Identity Center (khuyến nghị thay root)

Thay vì user IAM lâu dài:

1. Console → **IAM Identity Center**
2. **Enable** (một lần trên management)
3. **Users** → Create user `dev.engineer`
4. **Groups** → `DevOps` → assign user
5. **AWS accounts** → chọn Dev account → **Assign users/groups**
6. **Permission set:** `PowerUserAccess` hoặc custom → **Session duration** 8h

User login: https://your-subdomain.awsapps.com/start

---

## Bước 6 — Assume role qua CLI

Từ management credentials (user có quyền `sts:AssumeRole`):

```bash
aws sts assume-role \
  --role-arn arn:aws:iam::DEV_ACCOUNT_ID:role/DevOpsCrossAccountRole \
  --role-session-name lab-session \
  --external-id lab-module-22-dev
```

Export `AccessKeyId`, `SecretAccessKey`, `SessionToken` → gọi API Dev account.

Script: [scripts/03-assume-role-demo.sh](../scripts/03-assume-role-demo.sh)

---

## Lab

→ [Lab 03](../labs/basic/lab03-identity-center.md), [Lab 04](../labs/intermediate/lab04-cross-account-role.md), [Lab 05](../labs/intermediate/lab05-assume-role-cli.md)

**Tiếp:** [04-console-scp-permissions.md](04-console-scp-permissions.md)

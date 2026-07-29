# Console — Truy cập Resource Cross-Account

## Pattern 1 — S3 bucket (Audit account)

**Mục tiêu:** Dev account ghi log vào bucket **Audit account**.

### Audit account — tạo bucket

1. Login Audit (hoặc management lab)
2. **S3** → **Create bucket** → `org-audit-logs-MGMT_ID-ap-southeast-1`
3. Block public access: ON

### Bucket policy (cho phép Dev role)

1. Bucket → **Permissions** → **Bucket policy**
2. Paste [policies/s3-cross-account-bucket.json](../policies/s3-cross-account-bucket.json)
3. Thay `DEV_ACCOUNT_ID`, `DEV_ROLE_NAME`

### Dev account — ghi object

```bash
# Sau assume role DevOps
aws s3 cp test.log s3://org-audit-logs-.../dev/test.log
```

---

## Pattern 2 — EC2 / resource trong Dev

Developer assume `DevOpsCrossAccountRole` → có quyền EC2 trong Dev — không cần resource policy.

---

## Pattern 3 — Central VPC (overview)

Hub account share subnet qua **RAM** (Resource Access Manager) — nâng cao, ngoài scope lab cơ bản.

---

## Pattern 4 — CloudWatch Logs central

Log subscription filter → Kinesis → account Audit — xem AWS doc **Cross-account cross-Region**.

Lab module: tập trung **S3 cross-account** (lab 07).

---

## Kiểm tra quyền hiệu lực

```bash
# IAM policy simulator (Console)
IAM → Policies → Simulate

# CLI
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::DEV_ID:role/DevOpsCrossAccountRole \
  --action-names s3:PutObject \
  --resource-arns arn:aws:s3:::org-audit-logs-*/dev/*
```

---

## Lab

→ [Lab 07 — S3 cross-account](../labs/intermediate/lab07-s3-cross-account.md)

**Tiếp:** [06-terraform-organizations.md](06-terraform-organizations.md)

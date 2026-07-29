# Console — SCP & Phân quyền

## SCP là gì?

**Service Control Policy (SCP)** = guardrail trên **OU/account** — giới hạn **tối đa** quyền. SCP **không grant** quyền (IAM mới grant).

```
Effective permissions = IAM policy ∩ SCP (cả hai phải allow)
```

---

## Bước 1 — Mở SCP

1. **AWS Organizations** → **Policies** → tab **Service control policies**
2. **Enable service control policies** (nếu chưa)
3. **Create policy**

---

## Bước 2 — SCP ví dụ: Chỉ region Singapore

1. **Create policy** → Name: `DenyOutsideSingapore`
2. JSON:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "DenyOtherRegions",
    "Effect": "Deny",
    "Action": "*",
    "Resource": "*",
    "Condition": {
      "StringNotEquals": {
        "aws:RequestedRegion": ["ap-southeast-1"]
      }
    }
  }]
}
```

File: [policies/scp-deny-regions.json](../policies/scp-deny-regions.json)

3. **Create policy**

---

## Bước 3 — Attach SCP vào OU

1. **Policies** → chọn `DenyOutsideSingapore`
2. **Attach** → chọn OU **Sandbox** (không attach Root trước khi test!)
3. Confirm

⚠️ **Không attach Deny policy vào Root** cho đến khi hiểu rõ — có thể khóa chính management.

---

## Bước 4 — SCP: Cấm leave organization

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Action": "organizations:LeaveOrganization",
    "Resource": "*"
  }]
}
```

File: [policies/scp-deny-leave-org.json](../policies/scp-deny-leave-org.json)

Attach vào **Root** — best practice production.

---

## Bước 5 — Permission Boundary (IAM)

Trong member account — giới hạn user/role **dù admin attach policy lớn**:

1. **IAM** → **Policies** → **Create policy** → boundary max permissions
2. User → **Set permissions boundary**

Khác SCP: boundary gắn **IAM entity**, SCP gắn **account/OU**.

---

## Bước 6 — Test SCP

1. Assume role vào Sandbox account
2. Thử tạo EC2 region `us-east-1` → **AccessDenied**
3. Tạo EC2 `ap-southeast-1` → OK (nếu IAM allow)

---

## Lab

→ [Lab 06 — SCP](../labs/intermediate/lab06-scp.md)

**Tiếp:** [05-console-resource-access.md](05-console-resource-access.md)

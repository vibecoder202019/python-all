# Prompt AI cho Vault & Terraform

## Quy tắc an toàn bắt buộc

| ❌ Không paste | ✅ Thay bằng |
|---------------|-------------|
| `VAULT_TOKEN=hvs.xxx` | `VAULT_TOKEN=[REDACTED]` |
| AWS secret key | `AKIA...[REDACTED]` |
| terraform.tfstate thật | Mô tả structure, redact values |

Prompt:
```markdown
Constraints: Mọi secret trong ví dụ dùng placeholder. Không invent token format thật.
```

---

## Vault — review policy

```markdown
## Role
Vault security reviewer.

## Context
Policy HCL đính kèm (path secret/data/myapp/* read, list).

## Task
1. Liệt kê path có thể bị over-privilege
2. Đề xuất policy least-privilege cho app chỉ đọc key `db` 
3. AppRole vs K8s auth — chọn 1 cho workload trong K8s, giải thích 3 câu

Output: policy HCL mới + bullet trade-off
```

Template: [prompts/vault/review-policy.md](../prompts/vault/review-policy.md)

---

## Vault — viết policy

```markdown
Task: Policy cho CI pipeline Terraform:
- Read secret/data/terraform/aws (chỉ read)
- Deny delete mọi path
- Deny auth/token/create với policy admin

Output: HCL file + lệnh vault policy write
```

---

## Terraform — explain plan

```markdown
## Context
Terraform plan output đính kèm (3 add, 1 change, 0 destroy).

## Task
Giải thích từng thay đổi bằng tiếng Việt — impact production.
Cảnh báo thay đổi destructive nếu có.
Không chạy apply — chỉ review.

Output: table | Resource | Action | Risk | Notes |
```

Template: [prompts/vault/terraform-plan-review.md](../prompts/vault/terraform-plan-review.md)

---

## Terraform — viết module

```markdown
Task: Module Terraform tạo local_file config JSON từ variables:
- environment (string)
- app_name (string)
Output path: output/${app_name}-${environment}.json

Constraints: provider local only, pin version ~> 2.4, có outputs.
Không backend S3 — lab local.
```

Module 19 examples là ground truth để so sánh AI output.

---

## Tích hợp Vault provider

```markdown
Context: Vault KV v2 path secret/myapp/db keys username, password.
Task: Terraform data source đọc secret → tạo local_file .env.generated permission 0600.
Không output password ra console — sensitive = true.

Output: main.tf only + env vars cần export
```

---

## Lab

→ [Lab 08 — Vault & Terraform](../labs/intermediate/lab08-vault-terraform.md)

**Tiếp:** [06-prompt-monitoring-logging.md](06-prompt-monitoring-logging.md)

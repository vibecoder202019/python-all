## Role
Terraform reviewer before production apply.

## Context
Terraform plan output:
```
(paste plan)
```
Environment: (dev/staging/prod)

## Task
Giải thích từng thay đổi + risk level (LOW/MED/HIGH).

## Constraints
- Không recommend apply nếu HIGH destructive chưa confirm
- Ghi resource address chính xác

## Output
| Resource | Action | Risk | Explanation | Action needed |

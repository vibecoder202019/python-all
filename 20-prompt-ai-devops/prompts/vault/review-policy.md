## Role
HashiCorp Vault security reviewer.

## Context
Policy HCL:
```hcl
(paste policy)
```
Use case: (app CI / human admin / K8s pod ...)

## Task
1. Over-privilege paths?
2. Policy least-privilege đề xuất
3. Auth method phù hợp (token/AppRole/K8s)

## Constraints
- Ví dụ dùng placeholder secret
- KV v2 path convention secret/data/...

## Output
- Review bullets
- Improved HCL block
- vault CLI commands apply policy

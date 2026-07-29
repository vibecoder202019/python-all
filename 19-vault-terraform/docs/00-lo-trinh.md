# Lộ trình tự học Vault + Terraform

## Giai đoạn 0 — Cài đặt (2–3 ngày)

**Mục tiêu:** Cài Terraform + Vault, chạy được `terraform version` và `vault version`.

```bash
bash scripts/01-install-tools.sh --check
bash scripts/02-setup-vault-dev.sh   # terminal 1
bash scripts/03-run-terraform.sh 01-hello  # terminal 2
```

**Đọc:** [01-cai-dat.md](01-cai-dat.md)

---

## Giai đoạn 1 — Terraform Core (2 tuần)

| Tuần | Docs | Labs | Kỹ năng |
|------|------|------|---------|
| 1 | 02 Cơ bản | 01–03 | init, plan, apply, variables |
| 2 | 03 Nâng cao | 04–06 | modules, state, workspace |

**Checkpoint:** Viết module Terraform tái sử dụng + remote state backend local.

---

## Giai đoạn 2 — Vault Core (2 tuần)

| Tuần | Docs | Labs | Kỹ năng |
|------|------|------|---------|
| 3 | 04 Cơ bản | 07–08 | KV v2, policy, token |
| 4 | 05 Nâng cao | 09–10 | AppRole, dynamic secrets concept |

**Checkpoint:** Tạo policy least-privilege + AppRole cho app giả lập.

---

## Giai đoạn 3 — Tích hợp (2 tuần)

| Tuần | Docs | Labs |
|------|------|------|
| 5–6 | 06 Tích hợp | 11–12 |

**Checkpoint:** Terraform project đọc secret từ Vault, không có password trong Git.

---

## Mock interview — Câu hỏi hay gặp

1. **Terraform state là gì?** File JSON lưu mapping resource thật ↔ config; không commit plain state có secret.
2. **plan vs apply?** plan = dry-run diff; apply = thực thi thay đổi.
3. **Vault dev mode khác prod?** Dev: in-memory, root token cố định — **chỉ lab**, không production.
4. **KV v1 vs v2?** v2 có versioning, metadata path `secret/data/` vs `secret/`.
5. **Tại sao dùng Vault thay .env?** Audit trail, rotation, dynamic creds, policy RBAC.

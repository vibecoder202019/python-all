# Lộ trình Module 21 — Terrakube

## Tuần 1 — Deploy & làm quen UI

| Ngày | Việc | Lab |
|------|------|-----|
| 1–2 | Đọc doc 01, cài mkcert, deploy Compose | 01 |
| 3 | Tour UI, đổi password admin | 02 |
| 4–5 | Tạo Org, Project | 03 |

**Checkpoint:** Truy cập https://terrakube.platform.local, đăng nhập OK.

---

## Tuần 2 — Workspace & Terraform run

| Ngày | Việc | Lab |
|------|------|-----|
| 1–2 | Workspace + chạy plan/apply sample local | 04 |
| 3 | Xem state file trên UI | 05 |
| 4–5 | Kết nối GitHub (fork python-all) | 06 |
| 6 | RBAC user read-only | 07 |

**Checkpoint:** 1 run Apply thành công, state hiển thị trên UI.

---

## Tuần 3 — Nâng cao

| Ngày | Việc | Lab |
|------|------|-----|
| 1–2 | Module registry concept | 08 |
| 3–4 | Helm trên minikube | 09 |
| 5 | Capstone end-to-end | 10 |

---

## So với Module 19

| Module 19 | Module 21 |
|-----------|-----------|
| `terraform` CLI local | Terraform qua **UI + remote backend** |
| State file local | State trên Terrakube |
| Học HCL | Học **vận hành platform** |

Học **19 trước 21** — hiểu plan/apply/state trước khi lên UI.

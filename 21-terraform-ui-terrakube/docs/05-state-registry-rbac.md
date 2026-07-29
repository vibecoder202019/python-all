# State, Module Registry & RBAC

## Remote State trên UI

Terrakube lưu **state** thay vì file local trên laptop.

1. Workspace → tab **States**
2. Xem version state, diff giữa runs
3. **Không** commit `.tfstate` lên Git

So sánh Module 19:

| Local CLI | Terrakube |
|-----------|-----------|
| `terraform.tfstate` file | State trong DB/backend platform |
| `terraform show` | UI States viewer |

Lab 05: sau Apply, mở States — tìm resource `local_file`.

---

## Module Registry (private)

Publish module nội bộ — reuse giống private Ansible roles.

1. Menu **Registry** → **Modules**
2. **Publish module** — connect Git repo module
3. Consumer workspace:

```hcl
module "config" {
  source  = "app.terraform.io/lab-org/config/local"  # format tùy Terrakube registry hostname
  # Hoặc registry URL lab: terrakube-registry.platform.local — xem UI registry docs
  environment = "dev"
}
```

Lab 08: publish module từ `terraform/sample-module/` (trong module 21).

---

## RBAC

### Teams

1. **Organization** → **Teams** → Create `developers`, `operators`
2. Gán quyền workspace:
   - **developers**: plan only
   - **operators**: plan + apply

### Users

1. **Settings** → **Users** → Invite (email lab)
2. Add user vào team

### So với AWX

| AWX | Terrakube |
|-----|-----------|
| Execute role on Job Template | Apply permission on Workspace |
| Audit job output | Audit run log |

Lab 07: tạo user read-only — verify không Apply được.

---

## Policy (OPA) — overview

Terrakube hỗ trợ **Sentinel/OPA** policy (tùy version) — chặn apply nếu vi phạm (ví dụ: không cho `0.0.0.0/0` security group).

Xem docs: https://docs.terrakube.io/ — mục Policy.

---

## Lab

- [Lab 05 — State](../labs/intermediate/lab05-state-ui.md)
- [Lab 07 — RBAC](../labs/intermediate/lab07-rbac.md)
- [Lab 08 — Registry](../labs/advanced/lab08-module-registry.md)

**Tiếp:** [06-helm-minikube.md](06-helm-minikube.md)

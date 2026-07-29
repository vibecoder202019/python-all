# Giới thiệu Terrakube & TACOS

## TACOS là gì?

**TACOS** = *Terraform Automation and Collaboration Software* — phần mềm tự động hóa và cộng tác cho Terraform, tương tự:

| Ansible world | Terraform world |
|---------------|-----------------|
| AWX / Ansible Semaphore | **Terrakube**, Terrapod |
| Playbook | `.tf` + workspace |
| Inventory | Variables + cloud creds |

HashiCorp có **Terraform Cloud/Enterprise** (TFC/TFE) — trả phí / SaaS. **Terrakube** là alternative **open source, self-host**.

---

## Kiến trúc Terrakube (đơn giản)

```
┌─────────────┐     HTTPS      ┌──────────────────┐
│  Browser    │ ─────────────▶ │  Terrakube UI    │
│  (Engineer) │                │  (Angular)       │
└─────────────┘                └────────┬─────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    ▼                   ▼                   ▼
              ┌──────────┐       ┌──────────┐       ┌──────────┐
              │ API      │       │ Registry │       │ Dex SSO  │
              │ Server   │       │ modules  │       │ (OAuth)  │
              └────┬─────┘       └──────────┘       └──────────┘
                   │
                   ▼
              ┌──────────┐       PostgreSQL / Redis / Executor (Docker/K8s Job)
              │ Executor │ ───▶ terraform plan|apply
              │ Agent    │
              └──────────┘
```

---

## Khái niệm trên UI

| Khái niệm | Giải thích | AWX tương đương |
|-----------|------------|-----------------|
| **Organization** | Tenant / team top-level | Organization AWX |
| **Project** | Nhóm workspace liên quan | Project |
| **Workspace** | 1 stack Terraform (1 state) | Job Template + inventory |
| **Run / Job** | 1 lần plan hoặc apply | Job run |
| **Module Registry** | Private Terraform modules | Execution Environment (khác nhưng cùng ý reuse) |
| **Team / RBAC** | Ai được plan/apply | Role AWX |

---

## Terrakube vs Atlantis vs AWX+Terraform

| | Terrakube | Atlantis | AWX chạy `terraform` |
|---|-----------|----------|------------------------|
| UI dashboard | ✅ Đầy đủ | ❌ Chủ yếu PR | ✅ Job UI |
| Remote state | ✅ | ❌ (tự lo) | ❌ |
| Registry | ✅ | ❌ | ❌ |
| PR workflow | ✅ (VCS) | ✅ Core | ⚠️ Tùy setup |
| Self-host OSS | ✅ | ✅ | ✅ |

**Module này chọn Terrakube** vì gần AWX nhất cho Terraform.

---

## OpenTofu

Terrakube hỗ trợ **Terraform** và **OpenTofu** — chọn execution mode trong workspace settings.

---

## Lab tiếp theo

→ [02-cai-dat-docker-compose.md](02-cai-dat-docker-compose.md)

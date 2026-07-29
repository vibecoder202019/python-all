# Workspace & Run trên Terrakube UI

## Luồng công việc chuẩn

```
Organization → Project → Workspace → Configure → Plan → Apply
```

Giống AWX: **Organization** → **Project** → **Job Template** → **Run Job**.

---

## Tạo Organization (lab)

1. Đăng nhập https://terrakube.platform.local
2. Menu **Organizations** → **Create**
3. Name: `lab-org`, Description: `Module 21 lab`

---

## Tạo Project

1. Trong `lab-org` → **Projects** → **Create**
2. Name: `demo-infra`
3. Optional: gắn team sau (lab 07)

---

## Tạo Workspace

1. Project `demo-infra` → **Workspaces** → **Create**
2. Gợi ý lab:

| Field | Giá trị lab |
|-------|-------------|
| Name | `local-files-demo` |
| Terraform version | Latest stable (UI chọn) |
| Execution mode | Remote (Terrakube executor) |
| Source | VCS hoặc CLI — xem lab 04 |

### Working directory (VCS)

Nếu repo là `python-all`, set:

```
21-terraform-ui-terrakube/terraform/sample-workspace
```

---

## Variables (Workspace)

Tab **Variables** — tương tự `-var` / `TF_VAR_`:

| Key | Value | Sensitive |
|-----|-------|-----------|
| `environment` | `dev` | No |
| `app_name` | `terrakube-lab` | No |

**Terraform env** (nếu cần):

| Key | Value |
|-----|-------|
| `TF_LOG` | `INFO` (debug tạm thời) |

---

## Chạy Plan

1. Workspace → **Actions** → **Plan** (hoặc **Queue plan**)
2. Xem log streaming — tìm `Plan: X to add`
3. **Không apply** nếu plan có destroy unexpected

---

## Chạy Apply

1. Sau plan thành công → **Confirm & Apply**
2. Một số org bật **approval policy** — admin approve
3. Verify output trong log + **States** tab

---

## Sample Terraform (local provider)

Code lab không cần AWS — xem:

```
21-terraform-ui-terrakube/terraform/sample-workspace/main.tf
```

Tạo file JSON dưới `output/` trên executor — state lưu Terrakube.

---

## CLI (tùy chọn)

Cài [terrakube-cli](https://github.com/terrakube-io/terrakube-cli) để trigger job từ terminal:

```bash
# Khái niệm — cấu hình theo docs Terrakube CLI
export TERRAKUBE_API=https://terrakube-api.platform.local
# terrakube workspace list
```

Lab 04 tập trung **UI** — CLI làm bài mở rộng.

---

## Lab

- [Lab 04 — Workspace + Run](../labs/intermediate/lab04-workspace-run.md)
- [Lab 05 — State UI](../labs/intermediate/lab05-state-ui.md)

**Tiếp:** [04-vcs-github.md](04-vcs-github.md)

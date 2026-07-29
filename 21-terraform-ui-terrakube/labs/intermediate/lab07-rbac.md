# Lab 07 — RBAC Team & Quyền

**60 phút**

## Tạo Team

1. Organization `lab-org` → **Teams**
2. Team `developers` — quyền **Plan only** trên workspace lab
3. Team `operators` — **Plan + Apply**

## User lab (nếu UI hỗ trợ multi-user local)

1. Invite user email thứ 2 (hoặc mô phỏng bằng 2 browser profile)
2. Gán vào team `developers`

## Verify

- User developers: Plan OK, Apply **bị chặn**
- User operators / admin: Apply OK

## So sánh AWX

| AWX | Terrakube |
|-----|-----------|
| Role: Execute on Job Template | Permission on Workspace |

Doc: [docs/05-state-registry-rbac.md](../../docs/05-state-registry-rbac.md)

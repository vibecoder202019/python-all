# Đáp án gợi ý Module 21

## 1. Domains
- terrakube.platform.local
- terrakube-api.platform.local
- terrakube-registry.platform.local
- terrakube-dex.platform.local

## 2. Organization vs Workspace
- Organization = tenant/team cấp cao (nhiều project)
- Workspace = 1 stack Terraform, 1 remote state, plan/apply riêng

## 4. Sample workspace path
`21-terraform-ui-terrakube/terraform/sample-workspace`

## Capstone
Luồng: Git → VCS webhook/manual → Terrakube executor → terraform apply → state lưu platform.

Khác CLI local: state tập trung, RBAC, audit run log trên UI.

Khác AWX: AWX chạy playbook stateless; Terrakube quản lý tfstate và plan artifact.

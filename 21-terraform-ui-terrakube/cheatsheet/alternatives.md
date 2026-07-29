# Terraform UI open source — alternatives

| Tool | UI | State | Self-host OSS | Ghi chú |
|------|----|-------|---------------|---------|
| **Terrakube** | Full | Yes | Apache 2.0 | Module 21 — gần AWX nhất |
| **Terrapod** | Full | Yes | Open source | So sánh Terrakube |
| **Atlantis** | PR only | No | Apache 2.0 | Nhẹ, GitHub/GitLab |
| **Terrateam** | Run log UI | External | MPL 2.0 | GitOps PR |
| **AWX + terraform** | Job UI | No | AWX OSS | Chỉ orchestrate shell |

# Khi chọn
- Can dashboard + registry → Terrakube
- Chi PR workflow → Atlantis
- Da co AWX → Job template terraform (Module 15)

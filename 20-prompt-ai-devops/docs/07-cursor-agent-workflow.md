# Cursor & Agent Workflow

## Cursor vs Chat thường

| | **Chat** | **Agent** |
|---|----------|-----------|
| Sửa file | Gợi ý, bạn copy | Tự edit nhiều file |
| Chạy lệnh | Hạn chế | Terminal, test, build |
| Phù hợp | Hỏi nhanh, review | Feature, refactor, debug multi-file |

---

## @ context — luôn dùng

```
@file handlers.py — code liên quan
@folder 16-k8s-security/manifests — YAML mẫu
@docs 04-prompt-kubernetes.md — theo chuẩn module
```

Prompt mẫu:
```markdown
@file deployment.yaml
Pod không Ready — readiness probe fail.
Describe output: (paste)
Sửa tối thiểu trong file này. Giải thích 2 câu trước diff.
```

---

## Agent prompt hiệu quả

```markdown
## Goal
Thêm endpoint GET /health trả {"status":"ok"} cho Go Task API Module 17.

## Constraints
- Sửa @file project/internal/handlers/handlers.go
- Thêm test trong handlers_test.go
- Không đổi API hiện có
- Chạy go test ./... trước khi xong

## Done when
- Test pass
- curl localhost:8080/health trả 200
```

---

## Rules / .cursorrules

Tạo rule repo-level (Module skill create-rule):

```markdown
# DevOps prompts
- Mọi kubectl có -n namespace
- YAML K8s: không :latest
- Python: type hints mới
- Không commit secret
```

Agent đọc rule mỗi session — giảm lặp lại constraint.

---

## Review diff từ Agent

Checklist trước Accept:
- [ ] Diff scope đúng yêu cầu — không file lạ?
- [ ] Secret/token không lọt?
- [ ] Test đã chạy?
- [ ] Breaking change?

Prompt review:
```markdown
Review staged diff như senior engineer. Chỉ liệt kê vấn đề BLOCKER.
```

---

## Multi-step agent task

```
Step 1 (Agent): "Đọc module 19 terraform/05-vault-provider, liệt kê dependency Vault"
Step 2 (Agent): "Thêm output sensitive cho password — minimal diff"
Step 3 (You): verify terraform plan tay
```

---

## Lab

→ [Lab 11 — Cursor Agent](../labs/advanced/lab11-cursor-agent.md)

**Tiếp:** [08-an-toan-va-chat-luong.md](08-an-toan-va-chat-luong.md)

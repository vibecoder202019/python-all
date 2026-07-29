# Prompt AI cơ bản

## Prompt là gì?

**Prompt** = hướng dẫn bạn gửi cho mô hình ngôn ngữ (LLM). Chất lượng output phụ thuộc **rõ ràng** bạn muốn gì, **context** đủ, và **format** mong đợi.

**Ví von:** Prompt tệ như nói "sửa máy" — thợ không biết máy gì, lỗi gì. Prompt tốt như work order có model, mã lỗi, phần cần sửa.

---

## Framework R-C-T-O

```markdown
## Role
Bạn là senior DevOps engineer chuyên Kubernetes và Python.

## Context
- Cluster: minikube, namespace `cka-lab`
- Pod `web-pod` CrashLoopBackOff
- Image: nginx:1.25
- Đã chạy: kubectl describe pod web-pod -n cka-lab (output đính kèm)

## Task
Liệt kê 3 nguyên nhân có thể, theo thứ tự xác suất.
Với mỗi nguyên nhân: 1 lệnh kubectl verify.

## Output
- Markdown bullet
- Lệnh copy-paste được
- Không đề xuất thay đổi chưa verify
```

| Thành phần | Câu hỏi tự kiểm |
|------------|-----------------|
| **Role** | AI cần level junior hay staff? Domain gì? |
| **Context** | OS, version, namespace, log, file path? |
| **Task** | Một việc — debug **hoặc** viết YAML, không cả hai cùng lúc |
| **Output** | Bullet / code only / table / tiếng Việt? |

Template: [prompts/templates/rcto-base.md](../prompts/templates/rcto-base.md)

---

## Prompt tệ vs prompt tốt

### ❌ Tệ
```
Fix my kubernetes pod
```

### ✅ Tốt
```
Pod web-7f9c8 CrashLoopBackOff trong namespace production.
Events: FailedMount — secret "db-creds" not found.
Đề xuất fix tối thiểu (YAML Secret hoặc sửa volumeMount).
Output: 1 manifest YAML + 2 lệnh kubectl verify.
```

---

## Nguyên tắc vàng

1. **Cụ thể > chung chung** — tên resource, version, error message
2. **Một task mỗi prompt** — tách "debug" và "viết doc"
3. **Giới hạn output** — "chỉ diff", "tối đa 20 dòng"
4. **Nói rõ giả định** — "giả sử không có quyền cluster-admin"
5. **Yêu cầu giải thích** — "explain why before code"

---

## Output format thường dùng

```markdown
## Output format
1. Root cause (1 câu)
2. Fix (code block)
3. Verify (lệnh shell)
4. Prevention (1 bullet)
```

Cho Python:
```
Output: unified diff only, no prose
```

Cho K8s:
```
Output: valid YAML, apiVersion + kind đầy đủ, không comment dài
```

---

## Công cụ

| Công cụ | Khi dùng |
|---------|----------|
| **Cursor Chat** | Hỏi nhanh, @file context |
| **Cursor Agent** | Sửa nhiều file, chạy lệnh |
| **ChatGPT / Claude** | Brainstorm, review kiến trúc |

---

## Lab

→ [Lab 01 — Framework R-C-T-O](../labs/basic/lab01-framework-rcto.md)

**Tiếp:** [02-prompt-nang-cao.md](02-prompt-nang-cao.md)

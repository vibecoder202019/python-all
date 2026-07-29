# An toàn & Chất lượng output AI

## Rủi ro khi tin AI mù quáng

| Rủi ro | Ví dụ |
|--------|-------|
| **Hallucination** | API K8s field không tồn tại |
| **Secret leak** | Paste token vào chat cloud |
| **Unsafe command** | `rm -rf /`, curl pipe bash |
| **Over-permission** | ClusterRole bind admin |
| **Stale knowledge** | Deprecated API version |

---

## Checklist trước khi chạy lệnh AI

- [ ] Đã đọc từng dòng shell/YAML?
- [ ] Production hay lab?
- [ ] Có backup / dry-run?
- [ ] Secret redacted trong prompt?
- [ ] Có cách rollback?

```bash
kubectl apply --dry-run=client -f -
terraform plan
python -m pytest
```

---

## Redaction template

Trước khi paste log/config:

```python
import re
text = re.sub(r'(password|token|secret)=[^\s&]+', r'\1=[REDACTED]', text, flags=re.I)
```

Hoặc thủ công: thay giá trị bằng `xxx`, giữ **structure**.

---

## Rubric tự chấm prompt (1–5)

| Tiêu chí | 1 | 5 |
|----------|---|---|
| Role rõ | Không | Có level + domain |
| Context | Thiếu version/NS | Đủ verify |
| Task | Mơ hồ | Một việc cụ thể |
| Output format | Không | Có template |
| Safety | Paste secret | Redacted |

Lab 12 capstone — chấm ≥ 20/25 trước khi coi là pass.

---

## Khi AI sai — prompt sửa

```markdown
Câu trả lời trước sai vì: (giải thích cụ thể)
Data bổ sung: (log/metric mới)
Chỉ sửa phần X. Giữ nguyên Y.
```

---

## Compliance & data

- Không đưa **PII**, **production secret**, **customer data** vào public LLM
- Dùng enterprise / local model nếu công ty yêu cầu
- Cursor privacy settings — đọc policy công ty

---

## Lab capstone

→ [Lab 12 — Incident response](../labs/advanced/lab12-capstone.md)

## Cheatsheet

→ [cheatsheet/prompt-framework.md](../cheatsheet/prompt-framework.md)

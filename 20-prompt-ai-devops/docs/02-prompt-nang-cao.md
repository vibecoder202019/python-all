# Prompt AI nâng cao

## Chain-of-Thought (CoT)

Yêu cầu AI **suy luận từng bước** trước kết luận — giảm hallucination khi troubleshoot.

```markdown
## Task
Phân tích log Pod OOMKilled.

## Instructions
Trước khi đưa fix, làm theo bước:
1. Trích metric/limit từ YAML đính kèm
2. So sánh request vs limit vs actual usage
3. Kết luận root cause
4. Đề xuất fix với trade-off (cost vs stability)
```

---

## Few-shot (ví dụ mẫu)

Cho AI 1–2 ví dụ input → output mong muốn:

```markdown
## Examples

Input: Pod ImagePullBackOff, image `ngnix:latest` (typo)
Output:
- Cause: typo image name / tag không tồn tại
- Fix: sửa thành nginx:latest
- Verify: kubectl describe pod ... | grep -i pull

Input: Pod 0/1 Ready, readiness probe HTTP 404
Output:
- Cause: probe path sai hoặc app chưa listen
- Fix: sửa path hoặc initialDelaySeconds
- Verify: kubectl exec ... -- curl localhost:8080/health
```

Ví dụ module: [examples/k8s-few-shot.md](../examples/k8s-few-shot.md)

---

## Decomposition (chia nhỏ)

Task lớn → chuỗi prompt:

```
Prompt 1: "Review NetworkPolicy — liệt kê gap bảo mật, không viết YAML"
Prompt 2: "Viết YAML deny-all + allow frontend→backend:8080"
Prompt 3: "Viết 3 lệnh kubectl test connectivity từ pod test"
```

---

## Iterative refine

Khi output gần đúng:

```markdown
Output trước thiếu:
- namespace trong mọi lệnh kubectl
- resource limits cho container

Giữ nguyên phần đúng. Chỉ bổ sung 2 mục trên.
Format: YAML full file, không snippet rời.
```

Lab: [lab03-iterative-refine.md](../labs/basic/lab03-iterative-refine.md)

---

## Negative constraints

Nói rõ **không làm gì**:

```markdown
Constraints:
- KHÔNG dùng `:latest` tag
- KHÔNG mở port 22 ra Internet
- KHÔNG hardcode password — dùng secretKeyRef
- KHÔNG thêm Helm nếu chưa yêu cầu
```

---

## Self-critique

```markdown
Sau khi trả lời, thêm section "Review":
- Assumption nào có thể sai?
- Cần thêm data gì để chắc chắn 100%?
- Risk nếu apply blind?
```

---

## Temperature & model (khái niệm)

- **Code / YAML / PromQL:** cần chính xác → prompt chi tiết, ít creative
- **Brainstorm runbook:** có thể mở rộng hơn

Trong Cursor: chọn model reasoning cho debug phức tạp.

**Tiếp:** [03-prompt-python-code.md](03-prompt-python-code.md)

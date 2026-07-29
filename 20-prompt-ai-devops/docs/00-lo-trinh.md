# Lộ trình Prompt AI cho DevOps Engineer

## Giai đoạn 1 — Nền tảng (Tuần 1)

**Đọc:** docs 01, 02  
**Lab:** 01, 02, 03

Học framework **R-C-T-O**:
- **R**ole — AI đóng vai gì
- **C**ontext — môi trường, stack, ràng buộc
- **T**ask — việc cụ thể, 1 task/lần
- **O**utput — format mong muốn

**Checkpoint:** Viết 3 prompt cho cùng 1 task — so sánh chất lượng output.

---

## Giai đoạn 2 — Code Python (Tuần 2)

**Đọc:** doc 03  
**Lab:** 04, 05

Kỹ năng:
- Paste traceback + file liên quan
- Yêu cầu giải thích **trước** khi sửa
- Output: diff nhỏ, có test

**Checkpoint:** Debug script Python Module 12 bằng prompt — không copy nguyên code AI mù quáng.

---

## Giai đoạn 3 — Kubernetes (Tuần 3)

**Đọc:** doc 04  
**Lab:** 06, 07

Kỹ năng:
- `kubectl describe`, `logs`, events trong prompt
- Namespace, tên resource chính xác
- YAML minimal, không thêm field thừa

**Checkpoint:** Troubleshoot broken pod Module 18 lab 09 chỉ với prompt + verify tay.

---

## Giai đoạn 4 — Vault & Terraform (Tuần 4)

**Đọc:** doc 05  
**Lab:** 08

Kỹ năng:
- Không paste token/password
- Review policy least-privilege
- Terraform plan interpretation

---

## Giai đoạn 5 — Observability (Tuần 5)

**Đọc:** doc 06  
**Lab:** 09, 10

Kỹ năng:
- PromQL từ metric mô tả bằng lời
- Alert rule với threshold + runbook link
- Log grep pattern + RCA timeline

---

## Giai đoạn 6 — Production workflow (Tuần 6)

**Đọc:** doc 07, 08  
**Lab:** 11, 12

**Capstone:** Giả lập incident — dùng AI hỗ trợ nhưng **bạn** quyết định apply.

---

## Thói quen hàng ngày

1. **Prompt ngắn, context đủ** — không novel, không thiếu namespace
2. **Verify mọi YAML/shell** trước khi chạy production
3. **Redact secret** — `[REDACTED]`, fake values trong lab
4. **Iterate** — "output sai X, sửa chỉ phần Y"
5. **Học từ diff** — đọc vì sao AI sửa, không chỉ apply

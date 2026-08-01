# Hướng dẫn chạy Manual — Module 20: Prompt AI DevOps

> Copy từng lệnh và chạy **tuần tự**. Module này **lab-driven** — không deploy infrastructure.

## Điều kiện

- Python 3
- Cursor hoặc IDE có AI (khuyến nghị)

---

## Phần A — Setup (tương ứng `scripts/01-setup.sh`)

```bash
cd learn-python-ai/20-prompt-ai-devops
mkdir -p notes
python3 --version
```

---

## Phần B — Lab 01 (tương ứng `scripts/02-run-lab.sh 01`)

```bash
cd learn-python-ai/20-prompt-ai-devops
cat labs/basic/lab01-framework-rcto.md
```

Làm theo lab: copy prompt template → paste vào AI → lưu kết quả vào `notes/`.

---

## Phần C — Đọc template prompt

```bash
cat prompts/python/debug-error.md
cat prompts/kubernetes/troubleshoot-pod.md
cat prompts/vault/terraform-plan-review.md
cat prompts/monitoring/promql-query.md
cat cheatsheet/prompt-framework.md
```

---

## Phần D — Lab tiếp theo (thay số 01→12)

```bash
cat labs/basic/lab02-before-after.md
cat labs/intermediate/lab06-k8s-troubleshoot.md
cat labs/advanced/lab10-logging-rca.md
```

Hoặc dùng script để mở lab:

```bash
bash scripts/02-run-lab.sh 03
bash scripts/02-run-lab.sh 08
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-setup.sh` | A |
| `02-run-lab.sh <NN>` | B, D |

## Gỡ / dọn dẹp

Không cần — chỉ file notes local.

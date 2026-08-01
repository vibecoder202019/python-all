# Hướng dẫn chạy Manual — Module 20: Prompt AI DevOps

> Lệnh trích từ `01-setup.sh`, `02-run-lab.sh`.

## Phần A — Cài đặt (`scripts/01-setup.sh`)

```bash
mkdir -p learn-python-ai/20-prompt-ai-devops/notes
python3 --version
```

**Kiểm tra:**

```bash
test -d learn-python-ai/20-prompt-ai-devops/notes && echo "notes OK"
python3 --version | grep -E "3\.(1[0-9]|[2-9][0-9])"
```

---

## Phần B — Lab 01 (`scripts/02-run-lab.sh 01`)

```bash
find learn-python-ai/20-prompt-ai-devops/labs -name "lab01-*.md"
cat learn-python-ai/20-prompt-ai-devops/labs/basic/lab01-framework-rcto.md
```

Làm theo lab → lưu output vào `notes/`.

---

## Phần C — Đọc template

```bash
cat learn-python-ai/20-prompt-ai-devops/prompts/python/debug-error.md
cat learn-python-ai/20-prompt-ai-devops/prompts/kubernetes/troubleshoot-pod.md
cat learn-python-ai/20-prompt-ai-devops/cheatsheet/prompt-framework.md
```

---

## Phần D — Lab khác

```bash
bash learn-python-ai/20-prompt-ai-devops/scripts/02-run-lab.sh 03
bash learn-python-ai/20-prompt-ai-devops/scripts/02-run-lab.sh 08
```

Hoặc:

```bash
cat learn-python-ai/20-prompt-ai-devops/labs/intermediate/lab06-k8s-troubleshoot.md
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-setup.sh` | A |
| `02-run-lab.sh` | B, D |

# Prompt AI cho Python & Code

## Context cần có khi debug

| Thông tin | Ví dụ |
|-----------|-------|
| Python version | 3.11 |
| Traceback đầy đủ | copy nguyên stack |
| File + function | `handlers.py`, line 42 |
| Input gây lỗi | JSON payload mẫu |
| Đã thử gì | "đã pip install X" |

Template: [prompts/python/debug-error.md](../prompts/python/debug-error.md)

---

## Prompt debug traceback

```markdown
## Role
Senior Python developer, ưu tiên fix tối thiểu.

## Context
Python 3.11, FastAPI app Module 09.
Traceback:
```
File "app/main.py", line 18, in predict
    result = model.predict(X)
ValueError: Feature names mismatch
```
Feature columns expected: ['age','income'] — input có 'Age' (capital A).

## Task
1. Giải thích root cause (2 câu)
2. Sửa tối thiểu — 1 file nếu có thể
3. Thêm 1 test pytest cover case này

## Output
- unified diff
- lệnh chạy test
```

---

## Refactor an toàn

```markdown
Refactor function `parse_log_line` trong @file utils/log_parser.py:
- Giữ public API không đổi
- Thêm type hints
- Tách regex ra constant
- Không đổi behavior — test hiện tại phải pass

Output: diff only. Liệt kê test cần chạy.
```

---

## Viết test

```markdown
Viết pytest cho @file store/memory.py:
- test create task
- test duplicate id raises
- test list empty

Mock: không dùng database thật.
Coverage: happy path + 1 edge case mỗi function.
```

Template: [prompts/python/write-tests.md](../prompts/python/write-tests.md)

---

## boto3 / AWS (Module 13)

```markdown
Context: boto3 list S3 buckets, region ap-southeast-1.
Task: script Python list buckets + size > 1GB (approximate).
Constraints: dùng paginator, handle ClientError, không hardcode key.
Output: single file + argparse --profile optional
```

---

## Code review prompt

```markdown
Review PR diff đính kèm như security-focused reviewer:
- SQL injection, command injection
- Secret in code
- Error handling leak stack trace

Output: table | Severity | File:Line | Issue | Fix suggestion |
Chỉ HIGH/MEDIUM.
```

---

## Anti-patterns

| ❌ | ✅ |
|----|-----|
| "viết app quản lý task" | "FastAPI CRUD Task, in-memory store, 3 endpoint, Pydantic v2" |
| Paste cả repo 500 file | @file cụ thể hoặc snippet 50 dòng |
| "fix bug" | traceback + expected vs actual |
| Apply code không đọc | Chạy test + đọc diff |

---

## Lab

- [Lab 04 — Debug Python](../labs/basic/lab04-python-debug.md)
- [Lab 05 — Viết test](../labs/intermediate/lab05-python-tests.md)

**Tiếp:** [04-prompt-kubernetes.md](04-prompt-kubernetes.md)

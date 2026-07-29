# Lab 11 — Cursor Agent workflow (Advanced)

**90 phút**

## Task

Dùng Cursor Agent với prompt:

```markdown
## Goal
Thêm function validate_port(value: str) -> int vào
@file examples/sample-buggy/db_url.py
Default port 5432 nếu value rỗng. Raise ValueError message rõ nếu invalid.

## Constraints
- Minimal diff
- Thêm test file examples/sample-buggy/test_db_url.py
- Chạy python + pytest trước khi xong

## Done when
db_url.py chạy không lỗi với port=""
```

## Review

- Accept diff chỉ sau checklist doc 07
- Ghi 2 điều Agent làm tốt / 1 điều cần sửa tay

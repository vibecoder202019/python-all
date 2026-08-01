# Hướng dẫn chạy Manual — Module 01: Python cơ bản

> Copy từng lệnh và chạy **tuần tự**. Module không có `scripts/` — phần **Cài đặt/Kiểm tra** theo README gốc repo.

## Quy ước

| Nhãn | Ý nghĩa |
|------|---------|
| **Cài đặt** | Chuẩn bị Python/venv |
| **Kiểm tra** | Xác nhận môi trường OK |
| **Chạy lab** | Từng file `examples/` |

---

## Phần 0 — Kiểm tra môi trường

```bash
python3 --version
which python3
```

**Kỳ vọng:** Python ≥ 3.10.

---

## Phần A — Cài đặt (tương đương setup repo gốc)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

**Kiểm tra sau cài đặt:**

```bash
python -c "import sys; print(sys.version)"
pip --version
```

---

## Phần B — Chạy ví dụ (tuần tự)

```bash
cd learn-python-ai/01-python-co-ban
```

```bash
python examples/01_bien_va_kieu_du_lieu.py
```

**Kiểm tra:** In ra kiểu `int`, `float`, `str`, `bool`.

```bash
python examples/02_dieu_kien_va_vong_lap.py
```

**Kiểm tra:** In kết quả `if/for/while`.

```bash
python examples/03_ham_va_lambda.py
```

```bash
python examples/04_list_comprehension.py
```

---

## Phần C — Bài tập (tùy chọn)

```bash
cat exercises/bai_tap.md
cat exercises/solutions/solutions.py
```

---

## Bản đồ manual

| Bước | File | Automation |
|------|------|------------|
| A | venv + pip | `README.md` — Cài đặt môi trường |
| B1–B4 | `examples/01` → `04` | Không có script |

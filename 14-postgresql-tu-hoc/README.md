# Module 14: Tự học PostgreSQL

Học **PostgreSQL** từ cơ bản đến nâng cao — SQL, Functions, Triggers, Views, Index, và kết nối từ Python.

## Mục tiêu

- Hiểu relational database và PostgreSQL
- Viết SQL: SELECT, JOIN, INSERT, UPDATE, DELETE
- Tạo **Functions** (PL/pgSQL) và **Triggers**
- Views, Index, Transactions
- Kết nối PostgreSQL từ Python (`psycopg2`)
- Hoàn thành database **Thư viện sách** qua 6 bước tuần tự

## Lý thuyết nền tảng — PostgreSQL là gì?

**PostgreSQL** (Postgres) là hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) mã nguồn mở, mạnh mẽ và phổ biến nhất cho developer.

```
Excel (1 file)          →  PostgreSQL (server, nhiều user, concurrent)
SQLite (file nhỏ)       →  PostgreSQL (production, scale lớn)
MySQL                   →  PostgreSQL (chuẩn SQL hơn, JSON, extensions)
```

### Tại sao học PostgreSQL?

| Lý do | Giải thích |
|-------|------------|
| Phổ biến | Dùng bởi Instagram, Spotify, Apple, FastAPI projects |
| Miễn phí | Open source, không license fee |
| Mạnh | ACID, JSON, full-text search, extensions (PostGIS...) |
| Kết hợp Python | FastAPI + SQLAlchemy + PostgreSQL = stack phổ biến |

### Khái niệm cốt lõi

| Khái niệm | Ví von | SQL |
|-----------|--------|-----|
| **Database** | Thư viện | `CREATE DATABASE lib` |
| **Table** | Kệ sách | `CREATE TABLE books (...)` |
| **Row** | 1 cuốn sách | `INSERT INTO books ...` |
| **Column** | Thuộc tính (title, author) | `title VARCHAR(200)` |
| **Primary Key** | Mã số duy nhất | `id SERIAL PRIMARY KEY` |
| **Foreign Key** | Liên kết bảng khác | `author_id REFERENCES authors(id)` |
| **Index** | Mục lục — tìm nhanh | `CREATE INDEX idx_title ON books(title)` |

### ACID — đảm bảo dữ liệu tin cậy

- **A**tomicity — giao dịch hoặc thành công hết, hoặc rollback hết
- **C**onsistency — luôn tuân thủ rules (constraints)
- **I**solation — nhiều user không ảnh hưởng lẫn nhau
- **D**urability — commit xong không mất dù server crash

---

## Yêu cầu

- Docker Desktop (khuyến nghị) hoặc PostgreSQL cài local
- Python 3.10+ (cho script kết nối)
- psql hoặc DBeaver/pgAdmin (optional — xem data trực quan)

---

## Chạy nhanh

```bash
bash scripts/setup.sh                    # Khởi động PostgreSQL (Docker)
bash scripts/run_all_examples.sh         # Ví dụ 01→06 tuần tự
bash scripts/run_project.sh              # Dự án Thư viện 6 bước
bash scripts/psql_shell.sh               # Mở psql shell tương tác
bash scripts/teardown.sh                 # Dừng và xóa container
```

**Kết nối mặc định:**
```
Host:     localhost
Port:     5433          # tránh conflict port 5432 local
Database: learn_db
User:     learn_user
Password: learn_pass
```

---

## Lộ trình trong module

Mỗi file trong `examples/` có **2 phần ở đầu file**:
- **YÊU CẦU ĐỀ BÀI** — bài này làm gì, từng bước
- **KẾT QUẢ MONG ĐỢI** — bảng đối chiếu khi chạy xong

Khi chạy script, các dòng `yeu_cau` / `ket_qua` / `buoc` cũng in ra terminal.

| # | File | Yêu cầu (tóm tắt) | Kết quả mong đợi | Level |
|---|------|-------------------|------------------|-------|
| 00 | `examples/00_reset_demo.sql` | Xóa và tạo lại schema `demo` | Schema trống, không lỗi | Setup |
| 01 | `examples/01_sql_co_ban.sql` | CRUD, WHERE, UPDATE 10%, thống kê | 5 sách, 3 sách <100k, 2 sách NNÁ tăng giá | Cơ bản |
| 02 | `examples/02_joins_aggregation.sql` | INNER/LEFT JOIN, HAVING, subquery | 5 sách+tác giả; NNÁ/Murakami=2 sách | Cơ bản |
| 03 | `examples/03_functions_plpgsql.sql` | 4 function PL/pgSQL + gọi thử | NNÁ=2 sách; phân loại giá; tổng kho | Trung bình |
| 04 | `examples/04_triggers.sql` | updated_at, audit_log, validate giá | UPDATE ok; audit_log có dòng UPDATE | Trung bình |
| 05 | `examples/05_views_indexes.sql` | View, materialized view, index, EXPLAIN | 3 tác giả trong view; 2 members | Nâng cao |
| 06 | `examples/06_python_psycopg2.py` | psycopg2: JOIN, function, transaction | Top 5 sách; 2 sách NNÁ; commit +1000 | Nâng cao |
| 🎯 | `project/` | Database **Thư viện sách** (6 step) | Mượn/trả, trigger, báo cáo | Dự án |

---

## 1. SQL cơ bản

```sql
-- Tạo bảng
CREATE TABLE authors (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

CREATE TABLE books (
    id        SERIAL PRIMARY KEY,
    title     VARCHAR(200) NOT NULL,
    author_id INTEGER REFERENCES authors(id),
    price     NUMERIC(10, 2) CHECK (price >= 0),
    published DATE
);

-- Thêm dữ liệu
INSERT INTO authors (name, country) VALUES ('Nguyễn Nhật Ánh', 'Việt Nam');

-- Truy vấn
SELECT b.title, a.name AS author, b.price
FROM books b
JOIN authors a ON b.author_id = a.id
WHERE b.price < 100000
ORDER BY b.title;
```

---

## 2. Functions (PL/pgSQL)

```sql
CREATE OR REPLACE FUNCTION book_count_by_author(author_name VARCHAR)
RETURNS INTEGER
LANGUAGE plpgsql
AS $$
DECLARE
    total INTEGER;
BEGIN
    SELECT COUNT(*) INTO total
    FROM books b
    JOIN authors a ON b.author_id = a.id
    WHERE a.name = author_name;
    RETURN total;
END;
$$;

-- Gọi function
SELECT book_count_by_author('Nguyễn Nhật Ánh');
```

**PL/pgSQL** = ngôn ngữ procedural của PostgreSQL — biến, IF, LOOP, giống Python trong SQL.

---

## 3. Triggers

```sql
-- Function trigger chạy khi có sự kiện
CREATE OR REPLACE FUNCTION update_modified_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

-- Gắn trigger vào bảng
CREATE TRIGGER trg_books_updated
    BEFORE UPDATE ON books
    FOR EACH ROW
    EXECUTE FUNCTION update_modified_at();
```

| Loại | Khi nào chạy |
|------|--------------|
| `BEFORE INSERT/UPDATE` | Trước khi ghi — validate, transform data |
| `AFTER INSERT/UPDATE/DELETE` | Sau khi ghi — audit log, sync bảng khác |

---

## 4. Views & Index

```sql
-- View — query lưu sẵn, dùng như bảng
CREATE VIEW v_book_summary AS
SELECT a.name AS author, COUNT(b.id) AS book_count, AVG(b.price) AS avg_price
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
GROUP BY a.name;

-- Index — tăng tốc tìm kiếm
CREATE INDEX idx_books_title ON books(title);
CREATE INDEX idx_books_author_id ON books(author_id);
```

---

## Dự án tuần tự: Database Thư viện Sách

```
project/
├── step01_schema.sql       # Tạo bảng: authors, books, members, loans
├── step02_seed_data.sql    # Dữ liệu mẫu
├── step03_functions.sql    # Functions: tính phí, đếm sách
├── step04_triggers.sql     # Triggers: audit log, auto updated_at
├── step05_views.sql        # Views: báo cáo, sách quá hạn
└── step06_final.sql        # Index, constraints, query tổng hợp
```

---

## Giải thích chi tiết (Tự học)

### Script `scripts/setup.sh`

```bash
docker compose up -d          # Khởi động PostgreSQL container nền
docker compose ps             # Kiểm tra container running
python scripts/run_sql.py examples/01_sql_co_ban.sql  # Chạy file SQL
```

- Docker chạy Postgres **cô lập** — không ảnh hưởng PostgreSQL hệ thống (nếu có)
- Port `5433` tránh xung đột với Postgres local port `5432`

### Script `scripts/run_sql.py`

```python
conn = psycopg2.connect(**DB_CONFIG)
cur.execute(sql_content)      # Thực thi toàn bộ file SQL
conn.commit()                 # Lưu thay đổi
```

- `psycopg2` — driver PostgreSQL cho Python
- **`commit()`** bắt buộc sau INSERT/UPDATE/DELETE — không commit = mất data

### File `01_sql_co_ban.sql` — đọc từng lệnh

```sql
SERIAL PRIMARY KEY
```
- `SERIAL` = integer tự tăng (1, 2, 3...)
- `PRIMARY KEY` = duy nhất, không null — định danh mỗi row

```sql
REFERENCES authors(id)
```
- **Foreign key** — `author_id` phải tồn tại trong `authors.id`
- Ngăn xóa author còn sách (hoặc cascade tùy config)

```sql
WHERE price BETWEEN 50000 AND 200000
```
- Lọc hàng — chỉ trả row thỏa điều kiện

### File `03_functions_plpgsql.sql`

```sql
DECLARE total INTEGER;     -- Khai báo biến local
BEGIN ... END;             -- Block thực thi
SELECT COUNT(*) INTO total  -- Gán kết quả query vào biến
RETURN total;              -- Trả về caller
```

**Function vs Trigger function:**
- Function thường: gọi bằng `SELECT my_func()`
- Trigger function: PostgreSQL gọi tự động khi INSERT/UPDATE/DELETE

### File `04_triggers.sql`

```sql
NEW.column    -- Giá trị MỚI (INSERT/UPDATE)
OLD.column    -- Giá trị CŨ (UPDATE/DELETE)
RETURN NEW;   -- BEFORE trigger: cho phép ghi (hoặc sửa NEW)
RETURN NULL;  -- BEFORE trigger: hủy operation
```

**Audit trigger pattern:**
```sql
INSERT INTO audit_log (table_name, action, old_data, new_data, changed_at)
VALUES (TG_TABLE_NAME, TG_OP, row_to_json(OLD), row_to_json(NEW), NOW());
```

---

## Câu hỏi thường gặp (FAQ)

**Q: PostgreSQL vs MySQL?**  
A: Postgres chuẩn SQL hơn, JSON/Array tốt hơn, phù hợp app phức tạp. MySQL phổ biến hosting shared.

**Q: Quên `COMMIT` thì sao?**  
A: Trong psql mặc định autocommit ON. Trong Python psycopg2 — **phải** `conn.commit()` hoặc dùng `with conn:` context.

**Q: Function vs Stored Procedure?**  
A: Postgres chủ yếu dùng **Functions** (có thể return value). Procedure (`CALL`) có từ PG 11+ nhưng ít dùng hơn.

**Q: Trigger chậm không?**  
A: Trigger trên bảng lớn có thể chậm — chỉ dùng khi cần (audit, validate). Logic phức tạp nên đặt application layer.

**Q: Làm sao xem query chậm?**  
A: `EXPLAIN ANALYZE SELECT ...` — xem execution plan và thời gian.

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module liên quan

- Trước: [Module 04 — File I/O](../04-xu-ly-file-va-module/README.md), [Module 09 — FastAPI](../09-fastapi/README.md)
- Sau: Kết hợp FastAPI + PostgreSQL + SQLAlchemy cho full-stack app

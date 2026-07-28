-- ═══════════════════════════════════════════════════════════════════════════
-- VÍ DỤ 1: SQL CƠ BẢN (CRUD + SELECT + AGGREGATE)
-- Chạy: python scripts/run_sql.py examples/00_reset_demo.sql examples/01_sql_co_ban.sql
-- ═══════════════════════════════════════════════════════════════════════════
--
-- YÊU CẦU ĐỀ BÀI:
--   1. Tạo bảng `authors` (tác giả) và `books` (sách), liên kết FOREIGN KEY.
--   2. INSERT 3 tác giả và 5 cuốn sách mẫu.
--   3. SELECT toàn bộ sách (id, title, price).
--   4. Lọc sách có giá < 100.000 VND, sắp xếp theo giá tăng dần.
--   5. UPDATE tăng giá 10% cho tất cả sách của author_id = 1 (Nguyễn Nhật Ánh).
--   6. Thống kê: tổng số sách, giá trung bình, min, max.
--
-- KẾT QUẢ MONG ĐỢI (khi chạy xong, đối chiếu output):
--   ┌─────────────────────────────┬──────────────────────────────────────┐
--   │ Phần in ra                  │ Kết quả                              │
--   ├─────────────────────────────┼──────────────────────────────────────┤
--   │ Tất cả sách                 │ 5 dòng                               │
--   │ Sách dưới 100k              │ 3 dòng (Alchemist, 2 sách NNÁ gốc)   │
--   │ Sau tăng giá 10% (author=1) │ 2 dòng: ~93.500 và ~101.200 VND      │
--   │ Thống kê                    │ total_books=5, avg_price ~96.000+    │
--   └─────────────────────────────┴──────────────────────────────────────┘
--
-- ═══════════════════════════════════════════════════════════════════════════

SET search_path TO demo;

SELECT '=== VÍ DỤ 1: SQL CƠ BẢN ===' AS info;
SELECT 'Yêu cầu: Tạo bảng → INSERT → SELECT → WHERE → UPDATE 10% → COUNT/AVG/MIN/MAX' AS yeu_cau;
SELECT 'Kết quả mong đợi: 5 sách | 3 sách <100k | 2 sách NNÁ tăng giá | thống kê 5 cuốn' AS ket_qua;

-- ── Bước 1: Tạo bảng ──
CREATE TABLE authors (
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

CREATE TABLE books (
    id         SERIAL PRIMARY KEY,
    title      VARCHAR(200) NOT NULL,
    author_id  INTEGER NOT NULL REFERENCES authors(id),
    price      NUMERIC(10, 2) CHECK (price >= 0),
    published  DATE,
    available  BOOLEAN DEFAULT TRUE
);

-- ── Bước 2: INSERT dữ liệu ──
INSERT INTO authors (name, country) VALUES
    ('Nguyễn Nhật Ánh', 'Việt Nam'),
    ('Haruki Murakami', 'Nhật Bản'),
    ('Paulo Coelho', 'Brazil');

INSERT INTO books (title, author_id, price, published) VALUES
    ('Cho tôi xin một vé đi tuổi thơ', 1, 85000, '2008-01-01'),
    ('Mắt biếc', 1, 92000, '2010-01-01'),
    ('Kafka bên bờ biển', 2, 120000, '2002-01-01'),
    ('Nhà ga cuối đêm', 2, 98000, '2015-01-01'),
    ('Alchemist', 3, 75000, '1988-01-01');

-- ── Bước 3: SELECT cơ bản ──
SELECT '▶ Kết quả: Tất cả sách (mong đợi 5 dòng)' AS buoc;
SELECT id, title, price FROM books;

-- ── Bước 4: WHERE — lọc giá ──
SELECT '▶ Kết quả: Sách dưới 100k (mong đợi 3 dòng)' AS buoc;
SELECT title, price FROM books WHERE price < 100000 ORDER BY price;

-- ── Bước 5: UPDATE tăng giá ──
UPDATE books SET price = price * 1.1 WHERE author_id = 1;
SELECT '▶ Kết quả: Sau tăng giá 10% author_id=1 (mong đợi 93500 và 101200)' AS buoc;
SELECT title, price FROM books WHERE author_id = 1;

-- ── Bước 6: Aggregate ──
SELECT '▶ Kết quả: Thống kê (mong đợi total_books=5)' AS buoc;
SELECT COUNT(*) AS total_books, ROUND(AVG(price), 0) AS avg_price,
       MIN(price) AS min_price, MAX(price) AS max_price
FROM books;

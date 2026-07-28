-- ═══════════════════════════════════════════════════════════════════════════
-- VÍ DỤ 5: VIEWS, MATERIALIZED VIEW VÀ INDEX
-- Chạy: sau ví dụ 01–04 (cần authors, books)
--       python scripts/run_sql.py examples/05_views_indexes.sql
-- ═══════════════════════════════════════════════════════════════════════════
--
-- YÊU CẦU ĐỀ BÀI:
--   1. View `v_author_summary`: thống kê sách/giá theo tác giả.
--   2. Materialized View `mv_expensive_books`: sách giá >= 90.000, REFRESH.
--   3. Tạo index trên books(title, author_id, price).
--   4. EXPLAIN ANALYZE: tìm sách theo title (xem query dùng index).
--   5. Bảng members với UNIQUE email — demo constraint + index tự động.
--
-- KẾT QUẢ MONG ĐỢI:
--   ┌─────────────────────────────┬──────────────────────────────────────┐
--   │ Phần in ra                  │ Kết quả                              │
--   ├─────────────────────────────┼──────────────────────────────────────┤
--   │ v_author_summary            │ 3 tác giả, book_count và avg_price   │
--   │ mv_expensive_books          │ 3-4 sách giá >= 90000                │
--   │ EXPLAIN ANALYZE             │ Index Scan hoặc Seq Scan (tùy data)  │
--   │ members                     │ 2 dòng: minh@..., lan@...            │
--   └─────────────────────────────┴──────────────────────────────────────┘
--
-- ═══════════════════════════════════════════════════════════════════════════

SET search_path TO demo;

SELECT '=== VÍ DỤ 5: VIEWS VÀ INDEX ===' AS info;
SELECT 'Yêu cầu: View tóm tắt | Materialized View | Index | EXPLAIN | UNIQUE email' AS yeu_cau;
SELECT 'Kết quả mong đợi: 3 tác giả trong view | 3-4 sách đắt | 2 members' AS ket_qua;

CREATE OR REPLACE VIEW v_author_summary AS
SELECT
    a.id,
    a.name AS author,
    a.country,
    COUNT(b.id) AS book_count,
    ROUND(AVG(b.price), 0) AS avg_price,
    SUM(b.price) AS total_value
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
GROUP BY a.id, a.name, a.country;

SELECT '▶ Kết quả: v_author_summary — 3 tác giả, số sách và giá TB' AS buoc;
SELECT * FROM v_author_summary ORDER BY book_count DESC;

CREATE MATERIALIZED VIEW IF NOT EXISTS mv_expensive_books AS
SELECT b.id, b.title, a.name AS author, b.price
FROM books b
JOIN authors a ON b.author_id = a.id
WHERE b.price >= 90000
WITH NO DATA;

REFRESH MATERIALIZED VIEW mv_expensive_books;

SELECT '▶ Kết quả: mv_expensive_books — sách giá >= 90000 (thường 3-4 dòng)' AS buoc;
SELECT * FROM mv_expensive_books;

CREATE INDEX IF NOT EXISTS idx_books_title ON books(title);
CREATE INDEX IF NOT EXISTS idx_books_author_id ON books(author_id);
CREATE INDEX IF NOT EXISTS idx_books_price ON books(price);

SELECT '▶ Kết quả: EXPLAIN ANALYZE tìm title=Mắt biếc (xem Index Scan / Seq Scan)' AS buoc;
EXPLAIN ANALYZE SELECT * FROM books WHERE title = 'Mắt biếc';

CREATE TABLE IF NOT EXISTS members (
    id    SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    name  VARCHAR(100) NOT NULL
);

INSERT INTO members (email, name) VALUES
    ('minh@example.com', 'Minh'),
    ('lan@example.com', 'Lan')
ON CONFLICT (email) DO NOTHING;

SELECT '▶ Kết quả: members — 2 dòng' AS buoc;
SELECT * FROM members;

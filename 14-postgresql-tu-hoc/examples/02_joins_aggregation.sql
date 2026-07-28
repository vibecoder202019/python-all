-- ═══════════════════════════════════════════════════════════════════════════
-- VÍ DỤ 2: JOIN VÀ AGGREGATION
-- Chạy: sau ví dụ 01 (cần bảng authors, books đã có dữ liệu)
--       python scripts/run_sql.py examples/02_joins_aggregation.sql
-- ═══════════════════════════════════════════════════════════════════════════
--
-- YÊU CẦU ĐỀ BÀI:
--   1. Tạo bảng `categories` và `book_categories` (quan hệ n-n sách ↔ thể loại).
--   2. INNER JOIN: liệt kê sách kèm tên tác giả.
--   3. LEFT JOIN: đếm số sách mỗi tác giả (kể cả tác giả 0 sách).
--   4. JOIN 3 bảng: sách theo thể loại.
--   5. GROUP BY + HAVING: tác giả có ≥ 2 cuốn sách.
--   6. Subquery: sách có giá cao hơn giá trung bình toàn kho.
--
-- KẾT QUẢ MONG ĐỢI:
--   ┌─────────────────────────────┬──────────────────────────────────────┐
--   │ Phần in ra                  │ Kết quả                              │
--   ├─────────────────────────────┼──────────────────────────────────────┤
--   │ INNER JOIN                  │ 5 dòng, mỗi sách có tên tác giả      │
--   │ LEFT JOIN book_count        │ NNÁ=2, Murakami=2, Coelho=1           │
--   │ Sách theo thể loại          │ 5 dòng (Thiếu nhi, Tiểu thuyết, ...) │
--   │ Tác giả >= 2 sách           │ 2 dòng: NNÁ và Murakami              │
--   │ Sách > giá TB               │ 2-3 dòng (Kafka, Nhà ga, Mắt biếc...)│
--   └─────────────────────────────┴──────────────────────────────────────┘
--
-- ═══════════════════════════════════════════════════════════════════════════

SET search_path TO demo;

SELECT '=== VÍ DỤ 2: JOIN VÀ AGGREGATION ===' AS info;
SELECT 'Yêu cầu: INNER JOIN | LEFT JOIN | JOIN 3 bảng | GROUP BY+HAVING | Subquery' AS yeu_cau;
SELECT 'Kết quả mong đợi: 5 sách+tác giả | NNÁ/Murakami=2 sách | 2 tác giả >=2 sách' AS ket_qua;

CREATE TABLE IF NOT EXISTS categories (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS book_categories (
    book_id     INTEGER REFERENCES books(id),
    category_id INTEGER REFERENCES categories(id),
    PRIMARY KEY (book_id, category_id)
);

INSERT INTO categories (name) VALUES ('Tiểu thuyết'), ('Thiếu nhi'), ('Triết học')
ON CONFLICT DO NOTHING;

INSERT INTO book_categories (book_id, category_id) VALUES
    (1, 2), (2, 2), (3, 1), (4, 1), (5, 3)
ON CONFLICT DO NOTHING;

-- ── INNER JOIN ──
SELECT '▶ Kết quả: INNER JOIN — 5 sách kèm tác giả' AS buoc;
SELECT b.title, a.name AS author, b.price
FROM books b
INNER JOIN authors a ON b.author_id = a.id
ORDER BY b.title;

-- ── LEFT JOIN ──
SELECT '▶ Kết quả: LEFT JOIN — số sách/tác giả (NNÁ=2, Murakami=2, Coelho=1)' AS buoc;
SELECT a.name, COUNT(b.id) AS book_count
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
GROUP BY a.name
ORDER BY book_count DESC;

-- ── JOIN nhiều bảng ──
SELECT '▶ Kết quả: Sách theo thể loại — 5 dòng' AS buoc;
SELECT b.title, c.name AS category
FROM books b
JOIN book_categories bc ON b.id = bc.book_id
JOIN categories c ON bc.category_id = c.id
ORDER BY c.name, b.title;

-- ── GROUP BY + HAVING ──
SELECT '▶ Kết quả: Tác giả >= 2 sách — 2 dòng (NNÁ, Murakami)' AS buoc;
SELECT a.name, COUNT(b.id) AS books, ROUND(AVG(b.price)) AS avg_price
FROM authors a
JOIN books b ON a.id = b.author_id
GROUP BY a.name
HAVING COUNT(b.id) >= 2;

-- ── Subquery ──
SELECT '▶ Kết quả: Sách đắt hơn giá TB — thường 2-3 dòng' AS buoc;
SELECT title, price FROM books
WHERE price > (SELECT AVG(price) FROM books);

-- ═══════════════════════════════════════════════════════════════════════════
-- VÍ DỤ 3: FUNCTIONS PL/pgSQL
-- Chạy: sau ví dụ 01–02 (cần bảng authors, books)
--       python scripts/run_sql.py examples/03_functions_plpgsql.sql
-- ═══════════════════════════════════════════════════════════════════════════
--
-- YÊU CẦU ĐỀ BÀI:
--   1. fn_book_count(name)     — đếm số sách của 1 tác giả (RETURNS INTEGER).
--   2. fn_price_category(price)— phân loại giá: Rẻ / Trung bình / Cao.
--   3. fn_books_by_author(name)— trả về TABLE các sách của tác giả.
--   4. fn_inventory_value()    — tổng giá trị sách còn available (LANGUAGE sql).
--   Gọi từng function và in kết quả để kiểm tra.
--
-- KẾT QUẢ MONG ĐỢI:
--   ┌─────────────────────────────┬──────────────────────────────────────┐
--   │ Function / Query            │ Kết quả                              │
--   ├─────────────────────────────┼──────────────────────────────────────┤
--   │ fn_book_count               │ NNÁ=2, Murakami=2, Coelho=1           │
--   │ fn_price_category           │ Mỗi sách có nhãn Rẻ/TB/Cao           │
--   │ fn_books_by_author('NNÁ')   │ 2 dòng: Vé tuổi thơ, Mắt biếc        │
--   │ fn_inventory_value()        │ 1 số = SUM(price) sách available     │
--   └─────────────────────────────┴──────────────────────────────────────┘
--
-- ═══════════════════════════════════════════════════════════════════════════

SET search_path TO demo;

SELECT '=== VÍ DỤ 3: FUNCTIONS PL/pgSQL ===' AS info;
SELECT 'Yêu cầu: 4 function (đếm sách, phân loại giá, TABLE, tổng kho) + gọi thử' AS yeu_cau;
SELECT 'Kết quả mong đợi: NNÁ=2 sách | phân loại giá | 2 sách NNÁ | tổng kho > 0' AS ket_qua;

-- ── Function 1: Đếm sách theo tác giả ──
CREATE OR REPLACE FUNCTION fn_book_count(p_author_name VARCHAR)
RETURNS INTEGER
LANGUAGE plpgsql
AS $$
DECLARE
    v_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM books b
    JOIN authors a ON b.author_id = a.id
    WHERE a.name = p_author_name;
    RETURN v_count;
END;
$$;

SELECT '▶ Kết quả: fn_book_count — NNÁ=2, Murakami=2, Coelho=1' AS buoc;
SELECT name, fn_book_count(name) AS books FROM authors;

-- ── Function 2: Phân loại giá ──
CREATE OR REPLACE FUNCTION fn_price_category(p_price NUMERIC)
RETURNS VARCHAR
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_price < 80000 THEN
        RETURN 'Rẻ';
    ELSIF p_price < 110000 THEN
        RETURN 'Trung bình';
    ELSE
        RETURN 'Cao';
    END IF;
END;
$$;

SELECT '▶ Kết quả: fn_price_category — mỗi sách có nhãn Rẻ/TB/Cao' AS buoc;
SELECT title, price, fn_price_category(price) AS category FROM books;

-- ── Function 3: Trả về TABLE ──
CREATE OR REPLACE FUNCTION fn_books_by_author(p_author_name VARCHAR)
RETURNS TABLE(title VARCHAR, price NUMERIC, published DATE)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT b.title, b.price, b.published
    FROM books b
    JOIN authors a ON b.author_id = a.id
    WHERE a.name = p_author_name
    ORDER BY b.published;
END;
$$;

SELECT '▶ Kết quả: fn_books_by_author(NNÁ) — 2 dòng sách' AS buoc;
SELECT * FROM fn_books_by_author('Nguyễn Nhật Ánh');

-- ── Function 4: Tổng giá trị kho ──
CREATE OR REPLACE FUNCTION fn_inventory_value()
RETURNS NUMERIC
LANGUAGE sql
STABLE
AS $$
    SELECT COALESCE(SUM(price), 0) FROM books WHERE available = TRUE;
$$;

SELECT '▶ Kết quả: fn_inventory_value — 1 số (tổng price sách available)' AS buoc;
SELECT fn_inventory_value() AS total_value;

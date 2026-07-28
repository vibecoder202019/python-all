-- Dự án Library — Bước 5: Index và tối ưu query
SET search_path TO library;

-- Index cho các cột thường query
CREATE INDEX IF NOT EXISTS idx_loans_member_id ON loans(member_id);
CREATE INDEX IF NOT EXISTS idx_loans_book_id ON loans(book_id);
CREATE INDEX IF NOT EXISTS idx_loans_status ON loans(status);
CREATE INDEX IF NOT EXISTS idx_books_author_id ON books(author_id);
CREATE INDEX IF NOT EXISTS idx_books_title ON books(title);
CREATE INDEX IF NOT EXISTS idx_members_email ON members(email);

-- Composite index: query loans theo member + status
CREATE INDEX IF NOT EXISTS idx_loans_member_status ON loans(member_id, status);

-- Partial index: chỉ index loans đang active (nhỏ hơn, nhanh hơn)
CREATE INDEX IF NOT EXISTS idx_loans_active ON loans(book_id)
    WHERE status = 'active';

-- EXPLAIN ANALYZE
SELECT '=== EXPLAIN: active loans by member ===' AS info;
EXPLAIN ANALYZE
SELECT * FROM loans WHERE member_id = 1 AND status = 'active';

SELECT '=== EXPLAIN: search book by title ===' AS info;
EXPLAIN ANALYZE
SELECT * FROM books WHERE title LIKE 'Harry%';

-- Thống kê index
SELECT '=== Indexes on library schema ===' AS info;
SELECT indexname, tablename, indexdef
FROM pg_indexes
WHERE schemaname = 'library'
ORDER BY tablename, indexname;

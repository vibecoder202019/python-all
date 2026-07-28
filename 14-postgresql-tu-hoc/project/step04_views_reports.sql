-- Dự án Library — Bước 4: Views báo cáo
SET search_path TO library;

-- View: Sách đang được mượn
CREATE OR REPLACE VIEW v_active_loans AS
SELECT
    l.id AS loan_id,
    b.title AS book,
    a.name AS author,
    m.name AS member,
    m.email,
    l.loan_date,
    l.due_date,
    l.due_date - CURRENT_DATE AS days_remaining,
    l.status
FROM loans l
JOIN books b ON l.book_id = b.id
JOIN authors a ON b.author_id = a.id
JOIN members m ON l.member_id = m.id
WHERE l.status IN ('active', 'overdue');

-- View: Thống kê thành viên
CREATE OR REPLACE VIEW v_member_stats AS
SELECT
    m.id,
    m.name,
    m.email,
    COUNT(l.id) FILTER (WHERE l.status = 'active') AS active_loans,
    COUNT(l.id) FILTER (WHERE l.status = 'returned') AS returned_loans,
    COUNT(l.id) FILTER (WHERE l.status = 'overdue') AS overdue_loans
FROM members m
LEFT JOIN loans l ON m.id = l.member_id
GROUP BY m.id, m.name, m.email;

-- View: Tồn kho sách
CREATE OR REPLACE VIEW v_book_inventory AS
SELECT
    b.id,
    b.title,
    a.name AS author,
    b.copies AS total_copies,
    COUNT(l.id) FILTER (WHERE l.status = 'active') AS on_loan,
    b.copies - COUNT(l.id) FILTER (WHERE l.status = 'active') AS available
FROM books b
JOIN authors a ON b.author_id = a.id
LEFT JOIN loans l ON b.id = l.book_id
GROUP BY b.id, b.title, a.name, b.copies;

-- Function: Báo cáo tổng hợp
CREATE OR REPLACE FUNCTION fn_library_report()
RETURNS TABLE(
    metric VARCHAR,
    value BIGINT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 'total_books'::VARCHAR, COUNT(*)::BIGINT FROM books
    UNION ALL
    SELECT 'total_members', COUNT(*)::BIGINT FROM members WHERE active
    UNION ALL
    SELECT 'active_loans', COUNT(*)::BIGINT FROM loans WHERE status = 'active'
    UNION ALL
    SELECT 'overdue_loans', COUNT(*)::BIGINT FROM loans WHERE status = 'overdue';
END;
$$;

SELECT '=== Active loans ===' AS info;
SELECT * FROM v_active_loans;

SELECT '=== Member stats ===' AS info;
SELECT * FROM v_member_stats;

SELECT '=== Book inventory ===' AS info;
SELECT * FROM v_book_inventory;

SELECT '=== Library report ===' AS info;
SELECT * FROM fn_library_report();

-- Dự án Library — Bước 6: Hoàn thiện — stored procedure tổng hợp
SET search_path TO library;

-- Procedure: xử lý trả sách hàng loạt (overdue → returned nếu trả)
CREATE OR REPLACE FUNCTION fn_process_overdue()
RETURNS INTEGER  -- số loan được đánh dấu overdue
LANGUAGE plpgsql
AS $$
DECLARE
    v_count INTEGER;
BEGIN
    UPDATE loans
    SET status = 'overdue'
    WHERE status = 'active' AND due_date < CURRENT_DATE;

    GET DIAGNOSTICS v_count = ROW_COUNT;
    RETURN v_count;
END;
$$;

-- Procedure: thống kê top sách được mượn nhiều
CREATE OR REPLACE FUNCTION fn_top_borrowed(p_limit INTEGER DEFAULT 5)
RETURNS TABLE(title VARCHAR, borrow_count BIGINT)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT b.title, COUNT(l.id) AS borrow_count
    FROM books b
    LEFT JOIN loans l ON b.id = l.book_id
    GROUP BY b.id, b.title
    ORDER BY borrow_count DESC
    LIMIT p_limit;
END;
$$;

-- Grant read-only cho role demo (best practice)
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'library_reader') THEN
        CREATE ROLE library_reader;
    END IF;
END $$;

GRANT USAGE ON SCHEMA library TO library_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA library TO library_reader;

-- Final demo
SELECT '=== Top borrowed books ===' AS info;
SELECT * FROM fn_top_borrowed(5);

SELECT '=== Final library report ===' AS info;
SELECT * FROM fn_library_report();

SELECT '=== Active loans (final) ===' AS info;
SELECT loan_id, book, member, days_remaining, status FROM v_active_loans;

SELECT '=== Project complete! ===' AS info;

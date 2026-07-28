-- Dự án Library — Bước 2: Functions mượn/trả sách
SET search_path TO library;

-- Kiểm tra sách còn bản sao không
CREATE OR REPLACE FUNCTION fn_book_available(p_book_id INTEGER)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
    v_copies INTEGER;
    v_on_loan INTEGER;
BEGIN
    SELECT copies INTO v_copies FROM books WHERE id = p_book_id;
    IF v_copies IS NULL THEN
        RAISE EXCEPTION 'Sách id=% không tồn tại', p_book_id;
    END IF;

    SELECT COUNT(*) INTO v_on_loan
    FROM loans WHERE book_id = p_book_id AND status = 'active';

    RETURN (v_copies - v_on_loan) > 0;
END;
$$;

-- Mượn sách
CREATE OR REPLACE FUNCTION fn_borrow_book(
    p_book_id INTEGER,
    p_member_id INTEGER,
    p_days INTEGER DEFAULT 14
)
RETURNS INTEGER  -- trả về loan_id
LANGUAGE plpgsql
AS $$
DECLARE
    v_loan_id INTEGER;
    v_member_active BOOLEAN;
BEGIN
    SELECT active INTO v_member_active FROM members WHERE id = p_member_id;
    IF NOT v_member_active THEN
        RAISE EXCEPTION 'Thành viên id=% không còn hoạt động', p_member_id;
    END IF;

    IF NOT fn_book_available(p_book_id) THEN
        RAISE EXCEPTION 'Sách id=% hết bản sao', p_book_id;
    END IF;

    INSERT INTO loans (book_id, member_id, due_date)
    VALUES (p_book_id, p_member_id, CURRENT_DATE + p_days)
    RETURNING id INTO v_loan_id;

    RETURN v_loan_id;
END;
$$;

-- Trả sách
CREATE OR REPLACE FUNCTION fn_return_book(p_loan_id INTEGER)
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE loans
    SET status = 'returned', return_date = CURRENT_DATE
    WHERE id = p_loan_id AND status = 'active';

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Loan id=% không tồn tại hoặc đã trả', p_loan_id;
    END IF;
END;
$$;

-- Demo
SELECT '=== Mượn sách ===' AS info;
SELECT fn_borrow_book(1, 1) AS loan_id_1;
SELECT fn_borrow_book(4, 2) AS loan_id_2;

SELECT '=== Sách còn available? ===' AS info;
SELECT id, title, fn_book_available(id) AS available FROM books;

SELECT '=== Trả sách ===' AS info;
SELECT fn_return_book(1);
SELECT id, title, fn_book_available(id) AS available FROM books WHERE id = 1;

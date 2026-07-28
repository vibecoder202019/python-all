-- Giải bài 4–6 (functions)
SET search_path TO demo;

CREATE OR REPLACE FUNCTION fn_genre_count(p_genre_name VARCHAR)
RETURNS INTEGER LANGUAGE plpgsql AS $$
DECLARE v_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO v_count
    FROM book_genres bg
    JOIN genres g ON bg.genre_id = g.id
    WHERE g.name = p_genre_name;
    RETURN v_count;
END;
$$;

-- Chuyển sang library cho bài 5–6
SET search_path TO library;

CREATE OR REPLACE FUNCTION fn_member_can_borrow(p_member_id INTEGER)
RETURNS BOOLEAN LANGUAGE plpgsql AS $$
DECLARE
    v_active BOOLEAN;
    v_loans INTEGER;
BEGIN
    SELECT active INTO v_active FROM members WHERE id = p_member_id;
    IF NOT FOUND OR NOT v_active THEN RETURN FALSE; END IF;

    SELECT COUNT(*) INTO v_loans
    FROM loans WHERE member_id = p_member_id AND status = 'active';

    RETURN v_loans < 3;
END;
$$;

CREATE OR REPLACE FUNCTION fn_overdue_loans()
RETURNS TABLE(book_title VARCHAR, member_name VARCHAR, days_overdue INTEGER)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT b.title, m.name, (CURRENT_DATE - l.due_date)::INTEGER
    FROM loans l
    JOIN books b ON l.book_id = b.id
    JOIN members m ON l.member_id = m.id
    WHERE l.status IN ('active', 'overdue') AND l.due_date < CURRENT_DATE;
END;
$$;

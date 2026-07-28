-- Dự án Library — Bước 3: Triggers audit + validation
SET search_path TO library;

-- Bảng audit
CREATE TABLE IF NOT EXISTS audit_log (
    id         SERIAL PRIMARY KEY,
    table_name VARCHAR(50),
    action     VARCHAR(10),
    record_id  INTEGER,
    details    JSONB,
    changed_by VARCHAR(50) DEFAULT current_user,
    changed_at TIMESTAMP DEFAULT NOW()
);

-- Trigger: ghi log mọi thay đổi loans
CREATE OR REPLACE FUNCTION trg_loans_audit()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO audit_log (table_name, action, record_id, details)
        VALUES ('loans', 'INSERT', NEW.id, jsonb_build_object(
            'book_id', NEW.book_id, 'member_id', NEW.member_id, 'due_date', NEW.due_date
        ));
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO audit_log (table_name, action, record_id, details)
        VALUES ('loans', 'UPDATE', NEW.id, jsonb_build_object(
            'old_status', OLD.status, 'new_status', NEW.status
        ));
    END IF;
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_loans_audit ON loans;
CREATE TRIGGER trg_loans_audit
    AFTER INSERT OR UPDATE ON loans
    FOR EACH ROW
    EXECUTE FUNCTION trg_loans_audit();

-- Trigger: không cho mượn quá 3 sách cùng lúc
CREATE OR REPLACE FUNCTION trg_limit_borrow()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    v_active_loans INTEGER;
BEGIN
    SELECT COUNT(*) INTO v_active_loans
    FROM loans WHERE member_id = NEW.member_id AND status = 'active';

    IF v_active_loans >= 3 THEN
        RAISE EXCEPTION 'Thành viên id=% đã mượn tối đa 3 sách', NEW.member_id;
    END IF;
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_limit_borrow ON loans;
CREATE TRIGGER trg_limit_borrow
    BEFORE INSERT ON loans
    FOR EACH ROW
    EXECUTE FUNCTION trg_limit_borrow();

-- Trigger: tự đánh dấu overdue (khi update)
CREATE OR REPLACE FUNCTION trg_check_overdue()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.status = 'active' AND NEW.due_date < CURRENT_DATE THEN
        NEW.status = 'overdue';
    END IF;
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_check_overdue ON loans;
CREATE TRIGGER trg_check_overdue
    BEFORE UPDATE ON loans
    FOR EACH ROW
    EXECUTE FUNCTION trg_check_overdue();

-- Demo
SELECT '=== Mượn thêm (trigger audit) ===' AS info;
SELECT fn_borrow_book(5, 1) AS loan_id;

SELECT '=== Audit log ===' AS info;
SELECT id, action, record_id, details, changed_at FROM audit_log ORDER BY id;

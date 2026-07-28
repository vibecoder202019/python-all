-- Giải bài 7–9 (triggers & materialized view)
SET search_path TO library;

-- Bài 7
CREATE OR REPLACE FUNCTION trg_unique_member_email()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.email IS DISTINCT FROM OLD.email THEN
        IF EXISTS (SELECT 1 FROM members WHERE email = NEW.email AND id <> NEW.id) THEN
            RAISE EXCEPTION 'Email % đã được sử dụng', NEW.email;
        END IF;
    END IF;
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_member_email ON members;
CREATE TRIGGER trg_member_email
    BEFORE UPDATE OF email ON members
    FOR EACH ROW EXECUTE FUNCTION trg_unique_member_email();

-- Bài 8
CREATE OR REPLACE FUNCTION trg_books_audit()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO audit_log (table_name, action, record_id, details)
        VALUES ('books', 'INSERT', NEW.id, row_to_json(NEW)::jsonb);
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO audit_log (table_name, action, record_id, details)
        VALUES ('books', 'DELETE', OLD.id, row_to_json(OLD)::jsonb);
    END IF;
    RETURN COALESCE(NEW, OLD);
END;
$$;

DROP TRIGGER IF EXISTS trg_books_audit ON books;
CREATE TRIGGER trg_books_audit
    AFTER INSERT OR DELETE ON books
    FOR EACH ROW EXECUTE FUNCTION trg_books_audit();

-- Bài 9
CREATE MATERIALIZED VIEW IF NOT EXISTS mv_monthly_loans AS
SELECT date_trunc('month', loan_date)::DATE AS month,
       COUNT(*) AS loan_count
FROM loans
GROUP BY 1
ORDER BY 1;

REFRESH MATERIALIZED VIEW mv_monthly_loans;

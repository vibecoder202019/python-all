-- ═══════════════════════════════════════════════════════════════════════════
-- VÍ DỤ 4: TRIGGERS (TỰ ĐỘNG HÓA KHI INSERT/UPDATE/DELETE)
-- Chạy: sau ví dụ 01 (cần bảng books)
--       python scripts/run_sql.py examples/04_triggers.sql
-- ═══════════════════════════════════════════════════════════════════════════
--
-- YÊU CẦU ĐỀ BÀI:
--   1. Thêm cột `updated_at` vào books.
--   2. Tạo bảng `audit_log` ghi lịch sử thay đổi.
--   3. Trigger BEFORE UPDATE: tự gán updated_at = NOW().
--   4. Trigger AFTER INSERT/UPDATE/DELETE: ghi audit_log (old/new JSON).
--   5. Trigger BEFORE UPDATE price: cấm giảm giá quá 50%.
--   6. Demo: UPDATE 1 sách → kiểm tra audit_log có dòng UPDATE.
--
-- KẾT QUẢ MONG ĐỢI:
--   ┌─────────────────────────────┬──────────────────────────────────────┐
--   │ Hành động                   │ Kết quả                              │
--   ├─────────────────────────────┼──────────────────────────────────────┤
--   │ UPDATE books id=1           │ Thành công, price = 95000            │
--   │ audit_log                   │ ≥1 dòng action='UPDATE', record_id=1 │
--   │ (tùy chọn) giảm giá >50%    │ RAISE EXCEPTION — script dừng lỗi    │
--   └─────────────────────────────┴──────────────────────────────────────┘
--
-- ═══════════════════════════════════════════════════════════════════════════

SET search_path TO demo;

SELECT '=== VÍ DỤ 4: TRIGGERS ===' AS info;
SELECT 'Yêu cầu: updated_at tự động | audit_log | validate giảm giá max 50%' AS yeu_cau;
SELECT 'Kết quả mong đợi: UPDATE thành công | audit_log có dòng UPDATE id=1' AS ket_qua;

ALTER TABLE books ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP DEFAULT NOW();

CREATE TABLE IF NOT EXISTS audit_log (
    id         SERIAL PRIMARY KEY,
    table_name VARCHAR(50),
    action     VARCHAR(10),
    record_id  INTEGER,
    old_data   JSONB,
    new_data   JSONB,
    changed_at TIMESTAMP DEFAULT NOW()
);

CREATE OR REPLACE FUNCTION trg_set_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_books_updated ON books;
CREATE TRIGGER trg_books_updated
    BEFORE UPDATE ON books
    FOR EACH ROW
    EXECUTE FUNCTION trg_set_updated_at();

CREATE OR REPLACE FUNCTION trg_audit_changes()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO audit_log (table_name, action, record_id, new_data)
        VALUES (TG_TABLE_NAME, TG_OP, NEW.id, row_to_json(NEW));
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO audit_log (table_name, action, record_id, old_data, new_data)
        VALUES (TG_TABLE_NAME, TG_OP, NEW.id, row_to_json(OLD), row_to_json(NEW));
        RETURN NEW;
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO audit_log (table_name, action, record_id, old_data)
        VALUES (TG_TABLE_NAME, TG_OP, OLD.id, row_to_json(OLD));
        RETURN OLD;
    END IF;
    RETURN NULL;
END;
$$;

DROP TRIGGER IF EXISTS trg_books_audit ON books;
CREATE TRIGGER trg_books_audit
    AFTER INSERT OR UPDATE OR DELETE ON books
    FOR EACH ROW
    EXECUTE FUNCTION trg_audit_changes();

CREATE OR REPLACE FUNCTION trg_validate_price_drop()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.price < OLD.price * 0.5 THEN
        RAISE EXCEPTION 'Giá không được giảm quá 50%% (từ % xuống %)', OLD.price, NEW.price;
    END IF;
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_books_price_check ON books;
CREATE TRIGGER trg_books_price_check
    BEFORE UPDATE OF price ON books
    FOR EACH ROW
    EXECUTE FUNCTION trg_validate_price_drop();

-- ── Demo ──
SELECT '▶ Kết quả: UPDATE id=1 → price=95000, trigger ghi audit' AS buoc;
UPDATE books SET price = 95000 WHERE id = 1;

SELECT '▶ Kết quả: audit_log — mong đợi action=UPDATE, record_id=1' AS buoc;
SELECT id, table_name, action, record_id, changed_at FROM audit_log ORDER BY id DESC LIMIT 5;

-- Bỏ comment dòng dưới để test trigger validation (script sẽ báo lỗi — đúng yêu cầu):
-- UPDATE books SET price = 1000 WHERE id = 1;

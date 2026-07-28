-- ═══════════════════════════════════════════════════════════════════════════
-- VÍ DỤ 0: RESET SCHEMA DEMO
-- Chạy: python scripts/run_sql.py examples/00_reset_demo.sql
--       (run_all_examples.sh tự gọi file này trước ví dụ 01)
-- ═══════════════════════════════════════════════════════════════════════════
--
-- YÊU CẦU ĐỀ BÀI:
--   Xóa toàn bộ schema `demo` cũ (nếu có) và tạo lại schema trống,
--   để các ví dụ 01→05 chạy từ trạng thái sạch, không bị lỗi "đã tồn tại".
--
-- KẾT QUẢ MONG ĐỢI:
--   - Không in bảng dữ liệu (chỉ DDL thành công).
--   - Schema `demo` tồn tại, chưa có bảng — sẵn sàng cho ví dụ 01.
--
-- ═══════════════════════════════════════════════════════════════════════════

SELECT '=== VÍ DỤ 0: RESET SCHEMA DEMO ===' AS info;
SELECT 'Yêu cầu: DROP + CREATE schema demo (làm sạch trước khi học ví dụ 01→05)' AS yeu_cau;
SELECT 'Kết quả mong đợi: không có lỗi; schema demo trống, sẵn sàng tạo bảng' AS ket_qua;

DROP SCHEMA IF EXISTS demo CASCADE;
CREATE SCHEMA demo;
SET search_path TO demo;

SELECT '✓ Schema demo đã reset xong' AS ket_qua_thuc_te;

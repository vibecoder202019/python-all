"""
Module 14 — Giải bài 10: Mượn sách từ Python (fn_borrow_book)

Gọi stored function PostgreSQL library.fn_borrow_book qua psycopg2,
xử lý transaction commit/rollback khi thành công hoặc lỗi.

Chạy: python exercises/solutions/bai_10_borrow.py
      (cần chạy examples 01→03 và bài tập trước để có schema library)

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Kết nối PostgreSQL và gọi library.fn_borrow_book(book_id, member_id).
  2. Commit khi mượn thành công — in loan_id trả về.
  3. Rollback và in lỗi khi sách không tồn tại hoặc hết sách.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - borrow(1, 1): "✓ Mượn thành công, loan_id=..." (nếu sách còn).
  - borrow(999, 1): "✗ Không mượn được: ..." (sách id=999 không tồn tại).
═══════════════════════════════════════════════════════════════════════════
"""
import psycopg2

# ── Cấu hình DB — khớp docker-compose và run_sql.py ──
DB = dict(host="localhost", port=5433, dbname="learn_db",
          user="learn_user", password="learn_pass")


def borrow(book_id: int, member_id: int) -> None:
    """Gọi fn_borrow_book — commit nếu OK, rollback nếu lỗi PostgreSQL."""
    conn = psycopg2.connect(**DB)
    cur = conn.cursor()
    try:
        # Parameterized query (%s) — tránh SQL injection
        cur.execute("SELECT library.fn_borrow_book(%s, %s)", (book_id, member_id))
        loan_id = cur.fetchone()[0]
        conn.commit()
        print(f"✓ Mượn thành công, loan_id={loan_id}")
    except psycopg2.Error as e:
        conn.rollback()
        print(f"✗ Không mượn được: {e.pgerror or e}")
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    # Trường hợp 1: mượn sách hợp lệ — kết quả phụ thuộc state DB hiện tại
    borrow(1, 1)
    # Trường hợp 2: sách không tồn tại — function raise exception → rollback
    borrow(999, 1)

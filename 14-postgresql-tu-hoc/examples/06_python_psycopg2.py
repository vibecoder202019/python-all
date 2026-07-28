"""
Module 14 — Ví dụ 6: Kết nối PostgreSQL từ Python (psycopg2)

Chạy: python examples/06_python_psycopg2.py
      (cần chạy ví dụ 01→03 trước để có bảng demo và function fn_inventory_value)

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Kết nối PostgreSQL qua psycopg2 (host localhost:5433).
  2. SELECT JOIN — in top 5 sách đắt nhất (title, author, price).
  3. Gọi function PostgreSQL fn_inventory_value() từ Python.
  4. Parameterized query (%s) — lấy sách theo tên tác giả (chống SQL injection).
  5. Transaction: UPDATE tăng giá + commit; nếu lỗi thì rollback.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  ┌─────────────────────────────┬──────────────────────────────────────┐
  │ Phần in ra                  │ Kết quả                              │
  ├─────────────────────────────┼──────────────────────────────────────┤
  │ Top 5 sách đắt nhất         │ 5 dòng, Kafka thường đứng đầu       │
  │ Tổng giá trị kho            │ 1 số VND (SUM price sách available)  │
  │ Sách của 'Nguyễn Nhật Ánh'  │ 2 dòng: Vé tuổi thơ, Mắt biếc       │
  │ Transaction                 │ "✓ Transaction committed (+1000...)"  │
  │ Cuối script                 │ "✓ Done"                             │
  └─────────────────────────────┴──────────────────────────────────────┘
═══════════════════════════════════════════════════════════════════════════
"""
import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "dbname": "learn_db",
    "user": "learn_user",
    "password": "learn_pass",
}


def demo_query():
    print("=== VÍ DỤ 6: PYTHON + PSYCOPG2 ===")
    print("Yêu cầu: SELECT JOIN | gọi function | parameterized query | transaction")
    print("Kết quả mong đợi: 5 sách đắt | tổng kho | 2 sách NNÁ | commit +1000 VND\n")

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # ── Bước 1: SELECT JOIN top 5 ──
    print("▶ Kết quả: Top 5 sách đắt nhất (mong đợi 5 dòng)")
    cur.execute("""
        SET search_path TO demo;
        SELECT b.title, a.name AS author, b.price
        FROM books b
        JOIN authors a ON b.author_id = a.id
        ORDER BY b.price DESC
        LIMIT 5
    """)
    rows = cur.fetchall()
    for row in rows:
        print(f"  {row['title']:35s} {row['author']:20s} {row['price']:,.0f}")

    # ── Bước 2: Gọi PostgreSQL function ──
    print("\n▶ Kết quả: fn_inventory_value() — 1 số tổng giá trị kho")
    cur.execute("SELECT fn_inventory_value() AS total")
    total = cur.fetchone()["total"]
    print(f"  Tổng giá trị kho: {total:,.0f} VND")

    # ── Bước 3: Parameterized query ──
    author = "Nguyễn Nhật Ánh"
    print(f"\n▶ Kết quả: Sách của '{author}' (mong đợi 2 dòng)")
    cur.execute(
        "SELECT title, price FROM demo.books b "
        "JOIN demo.authors a ON b.author_id = a.id WHERE a.name = %s",
        (author,),
    )
    for row in cur.fetchall():
        print(f"  {row['title']} — {row['price']:,.0f}")

    # ── Bước 4: Transaction ──
    print("\n▶ Kết quả: Transaction UPDATE id=1 (+1000 VND)")
    try:
        cur.execute("UPDATE demo.books SET price = price + 1000 WHERE id = 1")
        conn.commit()
        print("  ✓ Transaction committed (+1000 VND book id=1)")
    except Exception as e:
        conn.rollback()
        print(f"  ✗ Rolled back: {e}")

    cur.close()
    conn.close()
    print("\n✓ Done — đối chiếu output với bảng 'Kết quả mong đợi' ở đầu file")


if __name__ == "__main__":
    demo_query()

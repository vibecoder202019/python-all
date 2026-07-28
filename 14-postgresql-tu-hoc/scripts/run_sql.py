"""
Module 14 — Script chạy file SQL against PostgreSQL

Dùng chung cho module 14: đọc file .sql, tách statement an toàn
(bỏ qua ; trong string và khối $$), thực thi qua psycopg2.

Chạy: python scripts/run_sql.py examples/01_sql_co_ban.sql

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Kết nối PostgreSQL localhost:5433 (learn_db / learn_user).
  2. Đọc file SQL, tách thành từng statement (hỗ trợ $$ blocks và string).
  3. Thực thi tuần tự; in kết quả SELECT (tối đa 15 dòng/statement).

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - Mỗi file: "▶ tên_file.sql" rồi in rows nếu có SELECT.
  - Cuối mỗi file: "✓ Executed: tên_file (N statements)".
  - Lỗi SQL: "✗ Error in ..." kèm pgerror.
═══════════════════════════════════════════════════════════════════════════
"""
import re
import sys
from pathlib import Path

try:
    import psycopg2
except ImportError:
    print("pip install psycopg2-binary")
    sys.exit(1)

# ── Cấu hình kết nối — khớp docker-compose.yml module 14 ──
DB_CONFIG = {
    "host": "localhost",
    "port": 5433,
    "dbname": "learn_db",
    "user": "learn_user",
    "password": "learn_pass",
}


def split_sql_statements(sql: str) -> list[str]:
    """Tách SQL thành từng statement (bỏ qua ; trong string và $$ blocks)."""
    statements: list[str] = []
    current: list[str] = []
    in_single = False   # Đang trong chuỗi '...'
    in_double = False   # Đang trong chuỗi "..."
    dollar_tag: str | None = None  # Tag khối $$ ... $$ (PL/pgSQL function)
    i = 0
    while i < len(sql):
        ch = sql[i]
        # Bắt đầu khối dollar-quoted ($$ hoặc $tag$)
        if dollar_tag is None and not in_single and not in_double and ch == "$":
            m = re.match(r"\$([A-Za-z0-9_]*)\$", sql[i:])
            if m:
                dollar_tag = m.group(0)
                current.append(dollar_tag)
                i += len(dollar_tag)
                continue
        # Kết thúc khối dollar-quoted
        if dollar_tag and sql.startswith(dollar_tag, i):
            current.append(dollar_tag)
            i += len(dollar_tag)
            dollar_tag = None
            continue
        if dollar_tag is None:
            if ch == "'" and not in_double:
                in_single = not in_single
            elif ch == '"' and not in_single:
                in_double = not in_double
            elif ch == ";" and not in_single and not in_double:
                # Dấu ; ngoài string = kết thúc statement
                stmt = "".join(current).strip()
                if stmt and not stmt.startswith("--"):
                    statements.append(stmt)
                current = []
                i += 1
                continue
        current.append(ch)
        i += 1
    # Statement cuối (không có ; ở cuối file)
    tail = "".join(current).strip()
    if tail and not tail.startswith("--"):
        statements.append(tail)
    return statements


def run_sql_file(filepath: Path, verbose: bool = True) -> None:
    """Đọc và thực thi một file SQL — autocommit từng statement."""
    sql = filepath.read_text(encoding="utf-8")
    statements = split_sql_statements(sql)
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True
    cur = conn.cursor()
    try:
        for stmt in statements:
            cur.execute(stmt)
            # In kết quả SELECT nếu cursor có description
            if verbose and cur.description:
                rows = cur.fetchall()
                cols = [d[0] for d in cur.description]
                for row in rows[:15]:
                    print(f"    {dict(zip(cols, row))}")
                if len(rows) > 15:
                    print(f"    ... ({len(rows)} rows total)")
        if verbose:
            print(f"  ✓ Executed: {filepath.name} ({len(statements)} statements)")
    except psycopg2.Error as e:
        print(f"  ✗ Error in {filepath.name}: {e.pgerror or e}")
        raise
    finally:
        cur.close()
        conn.close()


def run_sql_files(files: list[Path]) -> None:
    """Chạy lần lượt nhiều file SQL."""
    for f in files:
        print(f"\n▶ {f.name}")
        run_sql_file(f)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_sql.py <file.sql> [file2.sql ...]")
        sys.exit(1)
    run_sql_files([Path(p) for p in sys.argv[1:]])

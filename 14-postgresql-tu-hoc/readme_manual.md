# Hướng dẫn chạy Manual — Module 14: PostgreSQL

> Lệnh trích từ `setup.sh`, `run_all_examples.sh`, `run_project.sh`, `psql_shell.sh`, `teardown.sh`.

## Phần 0 — Kiểm tra

```bash
python3 --version
docker --version
docker compose version
```

---

## Phần A — Cài đặt (`scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install psycopg2-binary
cd 14-postgresql-tu-hoc
docker compose up -d
```

**Kiểm tra PostgreSQL sẵn sàng (lặp đến khi OK):**

```bash
cd learn-python-ai/14-postgresql-tu-hoc
docker compose exec -T postgres pg_isready -U learn_user -d learn_db
docker compose ps
```

**Kỳ vọng:** `accepting connections`; container `running`.

**Kiểm tra Python driver:**

```bash
source ../.venv/bin/activate
python -c "import psycopg2; print('psycopg2 OK')"
```

---

## Phần B — Ví dụ SQL (`scripts/run_all_examples.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/examples/00_reset_demo.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/examples/01_sql_co_ban.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/examples/02_joins_aggregation.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/examples/03_functions_plpgsql.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/examples/04_triggers.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/examples/05_views_indexes.sql
python 14-postgresql-tu-hoc/examples/06_python_psycopg2.py
```

---

## Phần C — Dự án thư viện (`scripts/run_project.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/project/00_reset_library.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/project/step01_schema.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/project/step02_borrow_functions.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/project/step03_triggers.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/project/step04_views_reports.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/project/step05_indexes.sql
python 14-postgresql-tu-hoc/scripts/run_sql.py 14-postgresql-tu-hoc/project/step06_final.sql
```

---

## Phần D — psql shell (`scripts/psql_shell.sh`)

```bash
cd learn-python-ai/14-postgresql-tu-hoc
docker compose exec postgres psql -U learn_user -d learn_db
```

Trong psql:

```sql
\dt
SELECT version();
\q
```

---

## Phần E — Teardown (`scripts/teardown.sh`)

```bash
cd learn-python-ai/14-postgresql-tu-hoc
docker compose down
```

Xóa volume:

```bash
docker compose down -v
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `run_all_examples.sh` | B |
| `run_project.sh` | C |
| `psql_shell.sh` | D |
| `teardown.sh` | E |

**Kết nối:** `localhost:5433` / `learn_db` / `learn_user` / `learn_pass`

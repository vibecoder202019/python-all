# Lab 10 — Dynamic Secrets (Mock) (Advanced)

**Thời gian:** 60 phút

## Mục tiêu

Hiểu **dynamic credentials** — Vault tạo user DB tạm thay vì password tĩnh.

## Mock lab (không cần Postgres)

1. Đọc [docs/05-vault-nang-cao.md](../../docs/05-vault-nang-cao.md) phần Database engine
2. Vẽ sơ đồ luồng: App → Vault → DB
3. So sánh KV static vs dynamic TTL 1h

## Tùy chọn (có Docker Postgres)

```bash
docker run -d --name pg-lab -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:15
# Follow HashiCorp tutorial: vault database secrets engine postgresql
```

## Câu hỏi ôn tập

- Dynamic secret hết TTL thì Vault làm gì?
- Tại sao an toàn hơn password trong `.env`?

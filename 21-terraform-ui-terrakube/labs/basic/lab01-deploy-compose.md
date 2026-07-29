# Lab 01 — Deploy Terrakube Docker Compose

**Thời gian:** 60 phút | **Level:** Basic

## Mục tiêu

Triển khai Terrakube local HTTPS, container chạy ổn định.

---

## Bước 1 — Prerequisites

```bash
bash 21-terraform-ui-terrakube/scripts/01-check-prerequisites.sh
```

Nếu thiếu mkcert (macOS):

```bash
brew install mkcert nss
mkcert -install
```

---

## Bước 2 — /etc/hosts

```bash
bash 21-terraform-ui-terrakube/scripts/02-prepare-hosts.sh --print
sudo sh -c 'cat 21-terraform-ui-terrakube/config/hosts-entries.txt >> /etc/hosts'
bash 21-terraform-ui-terrakube/scripts/02-prepare-hosts.sh --check
```

---

## Bước 3 — Deploy

```bash
bash 21-terraform-ui-terrakube/scripts/03-deploy-terrakube-compose.sh
bash 21-terraform-ui-terrakube/scripts/04-wait-healthy.sh
```

---

## Bước 4 — Kiểm tra container

```bash
docker ps --format "table {{.Names}}\t{{.Status}}" | grep -i terra || docker ps
```

Mở browser: **https://terrakube.platform.local**

---

## Bước 5 — Verify lab

```bash
bash 21-terraform-ui-terrakube/scripts/08-verify-lab.sh 01
```

---

## Troubleshooting

| Lỗi | Xử lý |
|-----|--------|
| Certificate | `mkcert -install`, restart browser |
| 502/504 | `cd 21-terraform-ui-terrakube/.cache/terrakube-upstream/docker-compose && docker compose logs -f` |
| Clone fail | Kiểm tra network, xóa `.cache` deploy lại |

---

## Dọn dẹp (cuối module)

```bash
bash 21-terraform-ui-terrakube/scripts/05-teardown-compose.sh
```

# Cài đặt Terrakube — Docker Compose (HTTPS local)

Hướng dẫn **từng bước** theo [docs chính thức Terrakube](https://docs.terrakube.io/getting-started/docker-compose). Module bọc bằng script tự động phần lớn bước.

---

## Bước 0 — Kiểm tra prerequisites

```bash
bash 21-terraform-ui-terrakube/scripts/01-check-prerequisites.sh
```

| Công cụ | Kiểm tra |
|---------|----------|
| `docker` | `docker info` |
| `docker compose` | `docker compose version` |
| `mkcert` | `mkcert -version` |
| `git` | clone repo Terrakube |

### Cài mkcert (macOS)

```bash
brew install mkcert nss
mkcert -install
```

| Lệnh | Giải thích |
|------|------------|
| `mkcert -install` | Tạo CA local, tin cậy trên macOS Keychain |

### Cài mkcert (Ubuntu)

```bash
sudo apt install libnss3-tools
curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64"
chmod +x mkcert-v*-linux-amd64
sudo mv mkcert-v*-linux-amd64 /usr/local/bin/mkcert
mkcert -install
```

---

## Bước 1 — Docker network

Terrakube Compose dùng network cố định + Traefik gateway `10.25.25.253`:

```bash
docker network create terrakube-network \
  -d bridge \
  --subnet 10.25.25.0/24 \
  --gateway 10.25.25.254
```

| Tham số | Ý nghĩa |
|---------|---------|
| `10.25.25.0/24` | Subnet riêng — tránh conflict với Docker default |
| Gateway `.254` | Gateway bridge |
| Traefik `.253` | IP virtual host routing (theo docs Terrakube) |

Script `03-deploy-terrakube-compose.sh` tạo network nếu chưa có.

---

## Bước 2 — /etc/hosts

Thêm **4 dòng** (cần quyền admin):

```
10.25.25.253 terrakube.platform.local
10.25.25.253 terrakube-api.platform.local
10.25.25.253 terrakube-registry.platform.local
10.25.25.253 terrakube-dex.platform.local
```

```bash
# In hướng dẫn + kiểm tra
bash 21-terraform-ui-terrakube/scripts/02-prepare-hosts.sh --print
bash 21-terraform-ui-terrakube/scripts/02-prepare-hosts.sh --check
```

**macOS/Linux thêm thủ công:**

```bash
sudo sh -c 'cat >> /etc/hosts << EOF
10.25.25.253 terrakube.platform.local
10.25.25.253 terrakube-api.platform.local
10.25.25.253 terrakube-registry.platform.local
10.25.25.253 terrakube-dex.platform.local
EOF'
```

---

## Bước 3 — Clone & chứng chỉ HTTPS

```bash
bash 21-terraform-ui-terrakube/scripts/03-deploy-terrakube-compose.sh
```

Script thực hiện:

1. Clone `https://github.com/terrakube-io/terrakube.git` → `.cache/terrakube-upstream/`
2. `cd docker-compose`
3. `mkcert -key-file key.pem -cert-file cert.pem platform.local "*.platform.local"`
4. Copy `rootCA.pem` từ mkcert
5. `docker compose up -d --force-recreate`

---

## Bước 4 — Kiểm tra container

```bash
bash 21-terraform-ui-terrakube/scripts/04-wait-healthy.sh
docker ps --filter "network=terrakube-network"
```

Đợi **1–2 phút** lần đầu (PostgreSQL migrate, API start).

---

## Bước 5 — Đăng nhập UI

| | |
|---|---|
| **URL** | https://terrakube.platform.local |
| **User** | `admin@example.com` |
| **Password** | `admin` |

⚠️ **Lab only** — đổi password ngay sau lab 02.

Nếu certificate warning: chạy lại `mkcert -install`, restart browser.

---

## Bước 6 — Dọn lab (teardown)

```bash
bash 21-terraform-ui-terrakube/scripts/05-teardown-compose.sh
```

Không xóa `/etc/hosts` — xóa tay nếu muốn.

---

## Troubleshooting

| Triệu chứng | Cách xử lý |
|-------------|------------|
| `connection refused` UI | `docker compose logs -f` trong `.cache/terrakube-upstream/docker-compose` |
| Certificate invalid | Regenerate mkcert trong thư mục compose |
| Host not found | Kiểm tra `/etc/hosts` + `--check` script |
| Port conflict | `docker ps`, stop stack cũ |
| RAM thiếu | Docker Desktop ≥ 4GB RAM cho container |

---

## Lab

→ [Lab 01 — Deploy Compose](../labs/basic/lab01-deploy-compose.md)

**Tiếp:** [03-workspace-va-run.md](03-workspace-va-run.md)

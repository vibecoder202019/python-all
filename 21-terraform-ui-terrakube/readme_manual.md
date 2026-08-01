# Hướng dẫn chạy Manual — Module 21: Terrakube (Terraform UI)

> Copy từng lệnh và chạy **tuần tự**. Luồng chính: Docker Compose + mkcert.

## Điều kiện

- Docker Desktop ≥ 4.x
- `mkcert`, `git`
- RAM ≥ 8 GB
- Module 19 (Terraform cơ bản)

---

## Phần A — Kiểm tra (tương ứng `scripts/01-check-prerequisites.sh`)

```bash
docker --version
docker compose version
mkcert -version
git --version
```

Cài mkcert (macOS):

```bash
brew install mkcert nss
mkcert -install
```

---

## Phần B — Hosts (tương ứng `scripts/02-prepare-hosts.sh`)

Xem entries cần thêm:

```bash
cat learn-python-ai/21-terraform-ui-terrakube/config/hosts-entries.txt
```

Thêm vào `/etc/hosts`:

```bash
sudo sh -c 'cat learn-python-ai/21-terraform-ui-terrakube/config/hosts-entries.txt >> /etc/hosts'
```

---

## Phần C — Deploy Compose (tương ứng `scripts/03-deploy-terrakube-compose.sh`)

```bash
docker network create terrakube-network -d bridge --subnet 10.25.25.0/24 --gateway 10.25.25.254
```

```bash
git clone --depth 1 https://github.com/terrakube-io/terrakube.git \
  learn-python-ai/21-terraform-ui-terrakube/.cache/terrakube-upstream
```

```bash
cd learn-python-ai/21-terraform-ui-terrakube/.cache/terrakube-upstream/docker-compose
mkcert -key-file key.pem -cert-file cert.pem platform.local "*.platform.local"
cp "$(mkcert -CAROOT)/rootCA.pem" rootCA.pem
docker compose up -d --force-recreate
```

---

## Phần D — Chờ healthy (tương ứng `scripts/04-wait-healthy.sh`)

```bash
curl -sk -o /dev/null -w "%{http_code}\n" https://terrakube.platform.local
```

Mở UI:

```bash
open https://terrakube.platform.local
```

Login: `admin@example.com` / `admin`

---

## Phần E — Lab (tương ứng `scripts/07-run-lab.sh`)

```bash
cd learn-python-ai/21-terraform-ui-terrakube
cat labs/basic/lab01-first-workspace.md
bash scripts/07-run-lab.sh 02
bash scripts/08-verify-lab.sh 01
```

Sample Terraform workspace:

```bash
cd learn-python-ai/21-terraform-ui-terrakube/terraform/sample-workspace
terraform init
terraform plan
```

---

## Phần F — Helm/minikube (tùy chọn, tương ứng `scripts/06-deploy-helm-minikube.sh`)

```bash
minikube start --cpus=4 --memory=8192
helm repo add terrakube-io https://terrakube-io.github.io/terrakube-helm-chart
helm repo update
kubectl create namespace terrakube
helm upgrade --install terrakube terrakube-io/terrakube \
  -n terrakube \
  -f learn-python-ai/21-terraform-ui-terrakube/helm/values-minikube.yaml \
  --wait --timeout 10m
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-check-prerequisites.sh` | A |
| `02-prepare-hosts.sh` | B |
| `03-deploy-terrakube-compose.sh` | C |
| `04-wait-healthy.sh` | D |
| `07-run-lab.sh` | E |
| `06-deploy-helm-minikube.sh` | F |
| `05-teardown-compose.sh` | Gỡ Compose |
| `09-teardown-helm.sh` | Gỡ Helm |

## Gỡ / dọn dẹp

```bash
cd learn-python-ai/21-terraform-ui-terrakube/.cache/terrakube-upstream/docker-compose
docker compose down -v
docker network rm terrakube-network
helm uninstall terrakube -n terrakube
kubectl delete namespace terrakube
```

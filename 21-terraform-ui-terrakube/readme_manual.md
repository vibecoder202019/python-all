# Hướng dẫn chạy Manual — Module 21: Terrakube

> Lệnh trích từ `01-check-prerequisites.sh` → `05-teardown-compose.sh`.

## Phần A — Kiểm tra (`scripts/01-check-prerequisites.sh`)

```bash
docker --version
git --version
mkcert -version
docker compose version
```

**Cài mkcert (macOS):**

```bash
brew install mkcert nss
mkcert -install
```

---

## Phần B — Hosts (`scripts/02-prepare-hosts.sh`)

```bash
cat learn-python-ai/21-terraform-ui-terrakube/config/hosts-entries.txt
sudo sh -c 'cat learn-python-ai/21-terraform-ui-terrakube/config/hosts-entries.txt >> /etc/hosts'
```

**Kiểm tra (`--check`):**

```bash
grep terrakube.platform.local /etc/hosts
```

---

## Phần C — Deploy Compose (`scripts/03-deploy-terrakube-compose.sh`)

```bash
docker network create terrakube-network -d bridge --subnet 10.25.25.0/24 --gateway 10.25.25.254
mkdir -p learn-python-ai/21-terraform-ui-terrakube/.cache
git clone --depth 1 --branch main https://github.com/terrakube-io/terrakube.git \
  learn-python-ai/21-terraform-ui-terrakube/.cache/terrakube-upstream
cd learn-python-ai/21-terraform-ui-terrakube/.cache/terrakube-upstream/docker-compose
mkcert -install
mkcert -key-file key.pem -cert-file cert.pem platform.local "*.platform.local"
cp "$(mkcert -CAROOT)/rootCA.pem" rootCA.pem
docker compose up -d --force-recreate
```

**Kiểm tra containers:**

```bash
docker compose ps
```

---

## Phần D — Chờ healthy (`scripts/04-wait-healthy.sh`)

```bash
curl -sk -o /dev/null -w "%{http_code}\n" https://terrakube.platform.local
```

**Kỳ vọng:** `200` hoặc `302`.

```bash
open https://terrakube.platform.local
```

Login: `admin@example.com` / `admin`

---

## Phần E — Verify lab (`scripts/08-verify-lab.sh`)

```bash
bash learn-python-ai/21-terraform-ui-terrakube/scripts/08-verify-lab.sh 01
```

---

## Phần F — Helm/minikube (`scripts/06-deploy-helm-minikube.sh`, tùy chọn)

```bash
minikube start --cpus=4 --memory=8192
helm repo add terrakube-io https://terrakube-io.github.io/terrakube-helm-chart
helm repo update
kubectl create namespace terrakube --dry-run=client -o yaml | kubectl apply -f -
helm upgrade --install terrakube terrakube-io/terrakube \
  -n terrakube \
  -f learn-python-ai/21-terraform-ui-terrakube/helm/values-minikube.yaml \
  --wait --timeout 10m
helm status terrakube -n terrakube
```

---

## Phần G — Teardown (`scripts/05-teardown-compose.sh`)

```bash
cd learn-python-ai/21-terraform-ui-terrakube/.cache/terrakube-upstream/docker-compose
docker compose down -v
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-check-prerequisites.sh` | A |
| `02-prepare-hosts.sh` | B |
| `03-deploy-terrakube-compose.sh` | C |
| `04-wait-healthy.sh` | D |
| `08-verify-lab.sh` | E |
| `06-deploy-helm-minikube.sh` | F |
| `05-teardown-compose.sh` | G |

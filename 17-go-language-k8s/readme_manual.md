# Hướng dẫn chạy Manual — Module 17: Go + K8s + Helm

> Lệnh trích từ `01-check-prerequisites.sh` → `07-test-api.sh`.

## Phần 0 — `/etc/hosts`

```bash
grep go-api.local /etc/hosts || echo "127.0.0.1 go-api.local" | sudo tee -a /etc/hosts
```

---

## Phần A — Kiểm tra tools (`scripts/01-check-prerequisites.sh`)

```bash
go version
docker --version
kubectl version --client
helm version --short
```

---

## Phần B — Go examples (`scripts/02-run-examples.sh`)

```bash
cd learn-python-ai/17-go-language-k8s
go run ./examples/01_hello/
go run ./examples/02_variables/
go run ./examples/03_functions_structs/
go run ./examples/04_interfaces/
go run ./examples/05_goroutines/
go run ./examples/06_http_json/
go run ./examples/07_context/
```

---

## Phần C — Project (`scripts/03-run-project.sh`)

```bash
cd learn-python-ai/17-go-language-k8s/project
go test ./...
go build -o bin/server ./cmd/server
./bin/server
```

**Kiểm tra (terminal khác, server đang chạy):**

```bash
curl -sf http://localhost:8080/health
```

---

## Phần D — Docker (`scripts/04-build-docker.sh`)

```bash
docker build -t go-task-api:latest learn-python-ai/17-go-language-k8s/project
docker images | grep go-task-api
```

---

## Phần E — K8s deploy (`scripts/05-deploy-k8s.sh`)

```bash
K8S=learn-python-ai/17-go-language-k8s/k8s
kubectl apply -f $K8S/namespace.yaml
kubectl apply -f $K8S/deployment.yaml
kubectl apply -f $K8S/service.yaml
kubectl apply -f $K8S/ingress.yaml
kubectl wait --for=condition=ready pod -l app=go-task-api -n go-api-lab --timeout=120s
```

**Kiểm tra:**

```bash
kubectl get pods -n go-api-lab
curl -sf http://go-api.local/health
```

---

## Phần F — Helm (`scripts/06-deploy-helm.sh`)

```bash
kubectl create namespace go-api-lab --dry-run=client -o yaml | kubectl apply -f -
helm upgrade --install go-task-api learn-python-ai/17-go-language-k8s/helm/go-task-api \
  --namespace go-api-lab \
  --set image.repository=go-task-api \
  --set image.tag=latest \
  --set image.pullPolicy=IfNotPresent \
  --wait --timeout 120s
helm status go-task-api -n go-api-lab
```

---

## Phần G — Test API (`scripts/07-test-api.sh`)

```bash
curl -sf http://localhost:8080/health | python3 -m json.tool
curl -sf -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Task manual test"}' | python3 -m json.tool
curl -sf http://localhost:8080/tasks | python3 -m json.tool
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-check-prerequisites.sh` | A |
| `02-run-examples.sh` | B |
| `03-run-project.sh` | C |
| `04-build-docker.sh` | D |
| `05-deploy-k8s.sh` | E |
| `06-deploy-helm.sh` | F |
| `07-test-api.sh` | G |

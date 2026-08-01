# Hướng dẫn chạy Manual — Module 17: Go + K8s + Helm

> Copy từng lệnh và chạy **tuần tự**. Mỗi phần tương ứng script trong `scripts/`.

## Điều kiện

- Go 1.22+
- Docker Desktop + Kubernetes
- `kubectl`, `helm`
- `/etc/hosts`: `127.0.0.1 go-api.local`

---

## Phần A — Kiểm tra tools (tương ứng `scripts/01-check-prerequisites.sh`)

```bash
go version
docker --version
kubectl version --client
helm version
```

---

## Phần B — Go examples (tương ứng `scripts/02-run-examples.sh`)

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

## Phần C — Build & test project (tương ứng `scripts/03-run-project.sh`)

```bash
cd learn-python-ai/17-go-language-k8s/project
go test ./...
go build -o bin/server ./cmd/server
./bin/server
```

---

## Phần D — Test API local (tương ứng `scripts/07-test-api.sh`)

> Cần server đang chạy ở Phần C

```bash
curl http://localhost:8080/health
curl -X POST http://localhost:8080/tasks -H "Content-Type: application/json" -d '{"title":"Task manual test"}'
curl http://localhost:8080/tasks
```

---

## Phần E — Build Docker (tương ứng `scripts/04-build-docker.sh`)

```bash
cd learn-python-ai
docker build -t go-task-api:latest 17-go-language-k8s/project
docker images | grep go-task-api
```

---

## Phần F — Deploy K8s manifests (tương ứng `scripts/05-deploy-k8s.sh`)

```bash
cd learn-python-ai/17-go-language-k8s
K8S=k8s
kubectl apply -f $K8S/namespace.yaml
kubectl apply -f $K8S/deployment.yaml
kubectl apply -f $K8S/service.yaml
kubectl apply -f $K8S/ingress.yaml
kubectl wait --for=condition=ready pod -l app=go-task-api -n go-api-lab --timeout=120s
echo "127.0.0.1 go-api.local" | sudo tee -a /etc/hosts
curl http://go-api.local/health
```

---

## Phần G — Deploy Helm (tương ứng `scripts/06-deploy-helm.sh`)

```bash
kubectl create namespace go-api-lab --dry-run=client -o yaml | kubectl apply -f -
helm upgrade --install go-task-api learn-python-ai/17-go-language-k8s/helm/go-task-api \
  --namespace go-api-lab \
  --set image.repository=go-task-api \
  --set image.tag=latest \
  --set image.pullPolicy=IfNotPresent \
  --wait --timeout 120s
kubectl get pods -n go-api-lab
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-check-prerequisites.sh` | A |
| `02-run-examples.sh` | B |
| `03-run-project.sh` | C |
| `07-test-api.sh` | D |
| `04-build-docker.sh` | E |
| `05-deploy-k8s.sh` | F |
| `06-deploy-helm.sh` | G |

## Gỡ / dọn dẹp

```bash
helm uninstall go-task-api -n go-api-lab
kubectl delete namespace go-api-lab
```

# Module 17: Go Language — Từ cơ bản đến nâng cao + Kubernetes + Helm

Học **Go (Golang)** từ zero đến deploy production-style API lên **Kubernetes** với **Helm chart** — dành cho Backend/DevOps Engineer.

## Mục tiêu

- Nắm syntax Go: biến, struct, interface, goroutine, channel
- Viết **REST API** chuẩn (HTTP, JSON, middleware, test)
- **Dockerize** ứng dụng Go (multi-stage build)
- Deploy lên K8s: manifest YAML + **Helm chart**
- Hiểu project layout chuẩn Go (`cmd/`, `internal/`)

---

## Lý thuyết nền tảng

### Go khác Python thế nào?

| | Python | Go |
|---|--------|-----|
| Typing | Dynamic | Static (compile-time) |
| Chạy | Interpreter | Compiled → binary |
| Concurrency | asyncio/thread | goroutine + channel |
| Deploy | cần runtime | single binary, không cần runtime |
| Error handling | try/except | `if err != nil` explicit |

### Cấu trúc project Go chuẩn

```
project/
├── cmd/server/main.go      # entry point (main package)
├── internal/               # private code — không import từ bên ngoài module
│   ├── handlers/           # HTTP handlers
│   ├── models/             # struct dữ liệu
│   ├── store/              # data layer
│   └── middleware/         # HTTP middleware
├── go.mod                  # module definition (giống requirements.txt)
├── Dockerfile
└── *_test.go               # tests cạnh source code
```

### Helm là gì?

**Helm** = package manager cho Kubernetes. Thay vì apply 10 file YAML thủ công:

```bash
helm upgrade --install go-task-api ./helm/go-task-api -n go-api-lab
```

Chart gồm:
- `Chart.yaml` — metadata
- `values.yaml` — config mặc định (override được)
- `templates/` — YAML với Go template syntax `{{ .Values.replicaCount }}`

---

## Yêu cầu

- Go 1.22+ — https://go.dev/dl/
- Docker Desktop + Kubernetes
- kubectl, helm (`brew install helm`)

---

## Chạy nhanh

```bash
# 1. Kiểm tra môi trường
bash 17-go-language-k8s/scripts/01-check-prerequisites.sh

# 2. Chạy examples Go (01 → 07)
bash 17-go-language-k8s/scripts/02-run-examples.sh

# 3. Test + build Task API
bash 17-go-language-k8s/scripts/03-run-project.sh
bash 17-go-language-k8s/scripts/03-run-project.sh --run   # chạy server

# 4. Test API (terminal khác)
bash 17-go-language-k8s/scripts/07-test-api.sh

# 5. Docker + K8s + Helm
bash 17-go-language-k8s/scripts/04-build-docker.sh
bash 17-go-language-k8s/scripts/05-deploy-k8s.sh      # YAML thuần
bash 17-go-language-k8s/scripts/06-deploy-helm.sh    # Helm chart
```

Thêm `/etc/hosts`:
```
127.0.0.1 go-api.local
```

---

## Lộ trình học

| Level | File | Nội dung |
|-------|------|----------|
| Cơ bản | `examples/01_hello` | Hello World, fmt |
| Cơ bản | `examples/02_variables` | Slice, map, for range |
| Cơ bản | `examples/03_functions_structs` | Struct, methods, pointer |
| Trung bình | `examples/04_interfaces` | Interface, polymorphism |
| Trung bình | `examples/05_goroutines` | Goroutine, channel, WaitGroup |
| Trung bình | `examples/06_http_json` | HTTP server, JSON API |
| Nâng cao | `examples/07_context` | Context timeout/cancel |
| 🎯 Dự án | `project/` | Task CRUD API hoàn chỉnh |

---

## Task API — Endpoints

| Method | Path | Mô tả |
|--------|------|-------|
| GET | `/health` | Health check |
| GET | `/tasks` | Liệt kê tasks |
| POST | `/tasks` | Tạo task `{"title":"..."}` |
| GET | `/tasks/{id}` | Chi tiết task |
| PATCH | `/tasks/{id}` | Toggle done/pending |
| DELETE | `/tasks/{id}` | Xóa task |

```bash
curl http://localhost:8080/health
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Học Helm chart"}'
curl http://localhost:8080/tasks
curl -X PATCH http://localhost:8080/tasks/1
```

---

## Helm Chart (`helm/go-task-api/`)

```
helm/go-task-api/
├── Chart.yaml           # Tên, version chart
├── values.yaml          # Config mặc định — SỬA FILE NÀY khi customize
└── templates/
    ├── _helpers.tpl     # Template helpers (tên, labels)
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    └── hpa.yaml
```

### Override values khi deploy

```bash
# Tăng replica, đổi host
helm upgrade --install go-task-api ./helm/go-task-api \
  --set replicaCount=3 \
  --set ingress.host=api.example.com

# Dùng file values riêng
helm upgrade --install go-task-api ./helm/go-task-api \
  -f helm/go-task-api/values-prod.yaml
```

### Giải thích values.yaml quan trọng

```yaml
replicaCount: 2              # Số pod chạy song song
image:
  repository: go-task-api    # Tên Docker image
  pullPolicy: IfNotPresent   # Never nếu image local
autoscaling:
  enabled: true              # HPA tự scale khi CPU cao
  maxReplicas: 5
```

---

## Kubernetes (`k8s/`)

Manifest YAML thuần — học trước khi dùng Helm:

| File | Resource |
|------|----------|
| `namespace.yaml` | Namespace `go-api-lab` |
| `deployment.yaml` | Deployment 2 replicas |
| `service.yaml` | ClusterIP port 80 |
| `ingress.yaml` | Route `go-api.local` |

---

## Giải thích code quan trọng

### `if err != nil` — error handling Go

```go
task, ok := store.Get(id)
if !ok {
    writeError(w, 404, "not found")
    return
}
```

Go không có exception — mọi lỗi trả về explicit.

### Goroutine

```go
go fetchData(i, ch, &wg)  // go = chạy async
wg.Wait()                 // đợi tất cả goroutine xong
```

### Middleware chain

```go
handler := middleware.CORS(middleware.Logging(mux))
// Request → CORS → Logging → Handler
```

---

## FAQ

**Hỏi:** `internal/` khác `pkg/`?  
**Đáp:** `internal/` — Go compiler **chặn** import từ bên ngoài module. `pkg/` — public, ai cũng import được.

**Hỏi:** Helm vs Kustomize?  
**Đáp:** Helm = templating + release management. Kustomize = patch YAML. Module này học Helm vì phổ biến hơn trong enterprise.

**Hỏi:** Image pull ErrImagePull?  
**Đáp:** Chạy `04-build-docker.sh` trước, set `image.pullPolicy: Never` trên Docker Desktop.

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

---

## Liên kết

- [Go Tour (official)](https://go.dev/tour/)
- [Helm Documentation](https://helm.sh/docs/)
- [Module 15 — AWX + K8s](../15-ansible-awx-minio-k8s/README.md)
- [Module 16 — K8s Security](../16-k8s-security/README.md)

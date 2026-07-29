# Triển khai Terrakube bằng Helm (minikube)

Lab nâng cao — gần production hơn Docker Compose.

---

## Prerequisites

```bash
minikube start --cpus=4 --memory=8192
kubectl get nodes
helm version
```

---

## Script lab

```bash
bash 21-terraform-ui-terrakube/scripts/06-deploy-helm-minikube.sh
```

Script sẽ:

1. Add helm repo `terrakube-io`
2. Tạo namespace `terrakube`
3. Install chart với `helm/values-minikube.yaml`
4. In URL + credentials (theo chart defaults)

---

## Values tối thiểu (lab)

File: [helm/values-minikube.yaml](../helm/values-minikube.yaml)

```yaml
# Ingress cho minikube
ingress:
  enabled: true
  hostname: terrakube.local

# Resource giảm cho laptop
resources:
  requests:
    memory: "512Mi"
```

---

## Truy cập

```bash
# minikube tunnel (terminal riêng) hoặc
minikube service -n terrakube
```

Thêm `/etc/hosts`:

```
$(minikube ip) terrakube.local
```

Chi tiết chart thay đổi theo version — đọc `helm show values terrakube/terrakube` sau khi add repo.

---

## Teardown

```bash
bash 21-terraform-ui-terrakube/scripts/08-teardown-helm.sh
```

---

## Lab

→ [Lab 09 — Helm minikube](../labs/advanced/lab09-helm-minikube.md)

**Tiếp:** [07-production-checklist.md](07-production-checklist.md)

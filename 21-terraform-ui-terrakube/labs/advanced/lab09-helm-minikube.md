# Lab 09 — Helm trên minikube

**120 phút** | Advanced

## Deploy

```bash
bash 21-terraform-ui-terrakube/scripts/01-check-prerequisites.sh
minikube start --cpus=4 --memory=8192
bash 21-terraform-ui-terrakube/scripts/06-deploy-helm-minikube.sh
```

## Truy cập

```bash
kubectl get pods -n terrakube
kubectl get ingress -n terrakube
# Terminal rieng:
minikube tunnel
```

Thêm hosts (IP minikube):

```bash
minikube ip
# echo "$(minikube ip) terrakube.local" | sudo tee -a /etc/hosts
```

## Bài tập

1. Login UI Helm instance
2. Tạo org/project giống lab 03
3. So sánh Compose vs Helm: component nào chạy trên K8s?

## Teardown

```bash
bash 21-terraform-ui-terrakube/scripts/09-teardown-helm.sh
```

Doc: [docs/06-helm-minikube.md](../../docs/06-helm-minikube.md)

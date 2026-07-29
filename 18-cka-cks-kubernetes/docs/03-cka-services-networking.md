# CKA Domain 3 — Services & Networking (20%)

## Service types

| Type | Dùng khi | Thi CKA |
|------|----------|---------|
| ClusterIP | Nội bộ cluster (mặc định) | ✅ Hay nhất |
| NodePort | Expose qua port node (30000-32767) | ✅ |
| LoadBalancer | Cloud LB | Ít gặp lab |

```bash
# Expose deployment thành service
kubectl expose deployment web --port=80 --target-port=8080 --type=ClusterIP -n exam-ns

# NodePort
kubectl expose deployment web --port=80 --type=NodePort -n exam-ns
```

## DNS trong cluster

```
<service>.<namespace>.svc.cluster.local
web.exam-ns.svc.cluster.local
```

## Ingress

```bash
# Cần Ingress Controller (nginx) đã cài
kubectl create ingress web --rule="web.local/*=web:80" -n exam-ns \
  --dry-run=client -o yaml | kubectl apply -f -
```

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  namespace: exam-ns
spec:
  ingressClassName: nginx
  rules:
    - host: web.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web
                port:
                  number: 80
```

## NetworkPolicy (CKS nhiều hơn CKA)

```yaml
# Chỉ cho phép ingress từ pod label app=frontend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
  namespace: exam-ns
spec:
  podSelector:
    matchLabels:
      role: backend
  policyTypes: [Ingress]
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

## CoreDNS troubleshoot

```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl run dns-test --image=busybox:1.36 -it --rm -- nslookup kubernetes
```

## Lab

- [Lab 03](../labs/basic/lab03-services.md), [Lab 05](../labs/intermediate/lab05-ingress-netpol.md), [Lab 12](../labs/advanced/lab12-netpol-zero-trust.md)

→ [04-cka-storage-troubleshooting.md](04-cka-storage-troubleshooting.md)

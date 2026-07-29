# CKA Domain 2 — Workloads & Scheduling (15%)

## Pod — Đơn vị nhỏ nhất

```bash
# Tạo pod nhanh khi thi — dry-run → edit → apply
kubectl run nginx --image=nginx:1.25 --dry-run=client -o yaml > pod.yaml
# Sửa pod.yaml (labels, namespace, resources...)
kubectl apply -f pod.yaml -n exam-ns

# Debug pod
kubectl describe pod <name> -n exam-ns    # Events — đọc đầu tiên khi lỗi
kubectl logs <name> -n exam-ns
kubectl logs <name> -n exam-ns --previous  # Log container trước khi crash
kubectl exec -it <name> -n exam-ns -- /bin/sh
```

## Deployment — Quản lý ReplicaSet

```bash
# Scale
kubectl scale deployment web --replicas=5 -n exam-ns

# Rolling update
kubectl set image deployment/web nginx=nginx:1.26 -n exam-ns
kubectl rollout status deployment/web -n exam-ns
kubectl rollout undo deployment/web -n exam-ns      # rollback
kubectl rollout history deployment/web -n exam-ns
```

## Scheduling

```bash
# nodeSelector — gán pod lên node có label
# Trong pod spec:
#   nodeSelector:
#     disktype: ssd

# Taint & Toleration — node không nhận pod trừ khi có toleration
kubectl taint nodes node1 key=value:NoSchedule
# Pod spec:
#   tolerations:
#   - key: "key"
#     operator: "Equal"
#     value: "value"
#     effect: "NoSchedule"

# nodeName — ép pod lên node cụ thể (thường thi)
#   spec:
#     nodeName: worker-2
```

## Resource requests/limits (hay thi)

```yaml
resources:
  requests:
    cpu: "100m"      # 100 millicore = 0.1 CPU
    memory: "128Mi"
  limits:
    cpu: "500m"
    memory: "256Mi"
```

## Static Pod

```bash
# Static pod do kubelet quản lý trực tiếp — đặt manifest tại:
# /etc/kubernetes/manifests/   (path mặc định)
# Không qua Deployment — tên pod = tên file-manifest
```

## Lab

- [Lab 01](../labs/basic/lab01-pods-labels.md), [Lab 02](../labs/basic/lab02-deployments.md), [Lab 07](../labs/intermediate/lab07-scheduling.md)

→ [03-cka-services-networking.md](03-cka-services-networking.md)

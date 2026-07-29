# CKA Domain 4 — Storage (10%) + Troubleshooting (30%)

## PVC / PV / StorageClass

```bash
# Luồng: StorageClass → PVC → Pod mount PVC

# 1. Tạo PVC
kubectl apply -f pvc.yaml -n exam-ns

# 2. Kiểm tra Bound
kubectl get pvc -n exam-ns

# 3. Pod mount
# volumes + volumeMounts trong pod spec
```

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
  namespace: exam-ns
spec:
  accessModes: [ReadWriteOnce]
  resources:
    requests:
      storage: 1Gi
  # storageClassName: ""  # default SC
```

## Troubleshooting — Quy trình CKA

```
Pod không Running?
  1. kubectl get pods -n NS
  2. kubectl describe pod NAME -n NS  → xem Events
  3. kubectl logs NAME -n NS [--previous]
  4. kubectl get events -n NS --sort-by='.lastTimestamp'
```

| Triệu chứng | Nguyên nhân | Fix |
|-------------|-------------|-----|
| Pending | PVC chưa Bound, thiếu resource | describe pod, get pvc |
| CrashLoopBackOff | App crash, sai command | logs, describe |
| ImagePullBackOff | Sai image name/tag | describe, sửa image |
| OOMKilled | Vượt memory limit | tăng limits |
| CreateContainerConfigError | Secret/CM thiếu key | describe pod |

## Node NotReady

```bash
kubectl describe node <name>
kubectl get pods -n kube-system -o wide   # kubelet, CNI pods
sudo systemctl status kubelet             # trên node (SSH)
journalctl -u kubelet -f
```

## Service không kết nối được

```bash
kubectl get ep <service> -n exam-ns   # Endpoints — phải có IP pod
kubectl get svc <service> -n exam-ns
# Selector service phải khớp label pod
```

## Lab

- [Lab 06](../labs/intermediate/lab06-storage.md), [Lab 09](../labs/advanced/lab09-troubleshoot.md)

→ [05-cks-cluster-hardening.md](05-cks-cluster-hardening.md)

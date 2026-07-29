# Lab 06 — PVC, PV, StorageClass (Intermediate | CKA)

**Namespace:** `cka-lab` | **Thời gian:** 45 phút

## Bài tập 1 — Tạo PVC

```bash
kubectl apply -f manifests/cka/pvc-data.yaml
kubectl get pvc -n cka-lab   # STATUS phải Bound
```

## Bài tập 2 — Pod mount PVC

```bash
kubectl apply -f manifests/cka/pod-with-pvc.yaml
kubectl exec data-writer -n cka-lab -- sh -c 'echo hello > /data/test.txt'
```

## Bài tập 3 — Pod thứ 2 đọc data (RWO — cùng node)

Scale / tạo pod mới mount cùng PVC, đọc `/data/test.txt`.

## Bài tập 4 — StorageClass

```bash
kubectl get storageclass
kubectl describe storageclass
```

## Verify

```bash
bash scripts/03-verify-lab.sh 06
```

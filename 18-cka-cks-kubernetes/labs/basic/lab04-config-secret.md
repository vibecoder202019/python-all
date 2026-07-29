# Lab 04 — ConfigMap & Secret (Basic | CKA)

**Namespace:** `cka-lab` | **Thời gian:** 30 phút

## Bài tập 1 — ConfigMap

```bash
kubectl create configmap app-config \
  --from-literal=APP_ENV=production \
  --from-literal=LOG_LEVEL=debug \
  -n cka-lab
```

## Bài tập 2 — Secret

```bash
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=s3cr3t \
  -n cka-lab
```

## Bài tập 3 — Mount vào Pod

Pod `config-demo` mount:
- ConfigMap key `APP_ENV` → env var
- Secret key `password` → env var `DB_PASSWORD`

File mẫu: `manifests/cka/pod-config-secret.yaml`

```bash
kubectl apply -f manifests/cka/pod-config-secret.yaml
kubectl exec config-demo -n cka-lab -- env | grep -E 'APP_ENV|DB_PASSWORD'
```

## Bài tập 4 — Decode secret (debug) với JSONPath

Secret lưu dữ liệu ở `.data.<key>` dạng **base64**. Dùng jsonpath để lấy rồi decode:

```bash
# Lấy key password (base64)
kubectl get secret db-secret -n cka-lab -o jsonpath='{.data.password}'

# Decode ra plaintext — hay gặp trong thi CKA
kubectl get secret db-secret -n cka-lab -o jsonpath='{.data.password}' | base64 -d && echo

# Liệt kê tất cả key trong secret
kubectl get secret db-secret -n cka-lab -o jsonpath='{.data}' | tr ',' '\n'
```

**Đọc thêm:** [docs/10-jsonpath-kubectl.md](../../docs/10-jsonpath-kubectl.md) — cú pháp đầy đủ, `{range}`, custom columns.

## Verify

```bash
bash scripts/03-verify-lab.sh 04
```

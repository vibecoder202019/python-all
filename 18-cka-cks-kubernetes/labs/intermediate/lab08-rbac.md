# Lab 08 — RBAC (Intermediate | CKA + CKS)

**Namespace:** `cka-lab` | **Thời gian:** 60 phút

## Bài tập 1 — ServiceAccount

```bash
kubectl create serviceaccount app-sa -n cka-lab
```

## Bài tập 2 — Role

Role `pod-reader`: get, list, watch pods trong namespace `cka-lab`.

```bash
kubectl create role pod-reader \
  --verb=get,list,watch --resource=pods -n cka-lab
```

## Bài tập 3 — RoleBinding

Bind `app-sa` → role `pod-reader`:

```bash
kubectl create rolebinding app-sa-read-pods \
  --role=pod-reader --serviceaccount=cka-lab:app-sa -n cka-lab
```

## Bài tập 4 — Kiểm tra quyền

```bash
kubectl auth can-i list pods --as=system:serviceaccount:cka-lab:app-sa -n cka-lab
kubectl auth can-i create pods --as=system:serviceaccount:cka-lab:app-sa -n cka-lab
```

## Bài tập 5 — ClusterRole (nâng cao)

ClusterRole `nodes-viewer` — list nodes (read-only cluster-wide).

File: `manifests/cks/rbac-clusterrole.yaml`

## Verify

```bash
bash scripts/03-verify-lab.sh 08
```

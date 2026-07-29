# Lab 07 — Scheduling: nodeSelector, Taint, Affinity (Intermediate | CKA)

**Thời gian:** 45 phút

## Bài tập 1 — Label node

```bash
kubectl label nodes <node-name> disktype=ssd
kubectl get nodes --show-labels
```

## Bài tập 2 — nodeSelector

Pod chỉ schedule lên node `disktype=ssd`.

File: `manifests/cka/pod-nodeselector.yaml`

## Bài tập 3 — Taint & Toleration

```bash
kubectl taint nodes <node-name> dedicated=cka-lab:NoSchedule
# Pod cần toleration mới vào node này
```

File: `manifests/cka/pod-toleration.yaml`

## Bài tập 4 — nodeName (ép pod)

```yaml
spec:
  nodeName: <exact-node-name>
```

## Cleanup

```bash
kubectl taint nodes <node-name> dedicated=cka-lab:NoSchedule-
```

## Verify

```bash
bash scripts/03-verify-lab.sh 07
```

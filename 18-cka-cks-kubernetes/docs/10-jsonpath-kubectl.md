# JSONPath với kubectl — CKA & CKS

**JSONPath** là cách trích xuất field cụ thể từ output JSON của Kubernetes API. Trong thi **CKA/CKS**, bạn sẽ dùng rất nhiều để:

- Lấy **IP Pod**, **Node**, **Port**, **Status** nhanh hơn `describe`
- Kiểm tra **readyReplicas**, **phase**, **conditions**
- Decode **Secret** (base64 trong `.data`)
- Tạo **custom columns** cho `kubectl get`
- Sắp xếp output với `--sort-by`

> **Mẹo thi:** JSONPath tiết kiệm thời gian khi đề yêu cầu "in ra IP của pod X" hoặc "liệt kê tên container trong pod Y".

---

## Cú pháp cơ bản

| Ký hiệu | Ý nghĩa | Ví dụ |
|---------|---------|-------|
| `.` | Truy cập field con | `.metadata.name` |
| `[n]` | Phần tử thứ n trong mảng (0-based) | `.items[0].metadata.name` |
| `[*]` | Tất cả phần tử mảng | `.spec.containers[*].name` |
| `..` | Đệ quy (tìm mọi cấp) | `{..name}` |
| `@` | Phần tử hiện tại (trong filter) | `[?(@.status.phase=='Running')]` |
| `'...'` | Bọc path trong dấu nháy đơn | `-o jsonpath='{.metadata.name}'` |

### Quy tắc kubectl

```bash
# Luôn bọc path trong dấu nhay đơn — tránh shell expand
kubectl get pod POD -o jsonpath='{.metadata.name}'

# Path bắt đầu bằng {. — root object
kubectl get pod POD -o jsonpath='{.status.podIP}'

# Nhiều field — dùng {} để nhóm, dấu cách hoặc \n để xuống dòng
kubectl get pod POD -o jsonpath='{range .spec.containers[*]}{.name}{"\n"}{end}'
```

---

## Lệnh cơ bản — CKA hay gặp

### Pod

```bash
# Tên pod
kubectl get pod web-pod -n cka-lab -o jsonpath='{.metadata.name}'

# IP pod
kubectl get pod web-pod -n cka-lab -o jsonpath='{.status.podIP}'

# Node đang chạy pod
kubectl get pod web-pod -n cka-lab -o jsonpath='{.spec.nodeName}'

# Phase (Running, Pending, Failed...)
kubectl get pod web-pod -n cka-lab -o jsonpath='{.status.phase}'

# Tất cả tên container trong pod
kubectl get pod web-pod -n cka-lab -o jsonpath='{.spec.containers[*].name}'

# Image của container đầu tiên
kubectl get pod web-pod -n cka-lab -o jsonpath='{.spec.containers[0].image}'

# Lý do pod chưa Ready (condition False)
kubectl get pod web-pod -n cka-lab -o jsonpath='{.status.conditions[?(@.status=="False")].message}'
```

### Deployment

```bash
# Số replica ready
kubectl get deploy web -n cka-lab -o jsonpath='{.status.readyReplicas}'

# Image hiện tại (container đầu tiên)
kubectl get deploy web -n cka-lab -o jsonpath='{.spec.template.spec.containers[0].image}'

# Selector labels
kubectl get deploy web -n cka-lab -o jsonpath='{.spec.selector.matchLabels}'
```

### Service

```bash
# ClusterIP
kubectl get svc web -n cka-lab -o jsonpath='{.spec.clusterIP}'

# Port
kubectl get svc web -n cka-lab -o jsonpath='{.spec.ports[0].port}'

# Target port
kubectl get svc web -n cka-lab -o jsonpath='{.spec.ports[0].targetPort}'
```

### Node

```bash
# Tên tất cả node
kubectl get nodes -o jsonpath='{.items[*].metadata.name}'

# IP nội bộ node
kubectl get node NODE -o jsonpath='{.status.addresses[?(@.type=="InternalIP")].address}'

# Taints
kubectl get node NODE -o jsonpath='{.spec.taints[*].key}'

# Capacity CPU
kubectl get node NODE -o jsonpath='{.status.capacity.cpu}'
```

### Secret & ConfigMap

```bash
# Giá trị secret (base64) — decode thêm bằng base64 -d
kubectl get secret db-secret -n cka-lab -o jsonpath='{.data.password}' | base64 -d && echo

# Key trong ConfigMap
kubectl get cm app-config -n cka-lab -o jsonpath='{.data.APP_ENV}'
```

### PVC / PV

```bash
# Trạng thái PVC
kubectl get pvc data -n cka-lab -o jsonpath='{.status.phase}'

# Volume được bind
kubectl get pvc data -n cka-lab -o jsonpath='{.spec.volumeName}'
```

---

## Lặp qua danh sách — `{range}` / `{end}`

Rất hữu ích khi cần in nhiều dòng (mỗi pod một dòng):

```bash
# Mỗi pod: tên + IP (mỗi dòng)
kubectl get pods -n cka-lab -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'

# Tất cả container name trong namespace
kubectl get pods -n cka-lab -o jsonpath='{range .items[*]}{.metadata.name}{": "}{.spec.containers[*].name}{"\n"}{end}'

# Pod không Running
kubectl get pods -A -o jsonpath='{range .items[?(@.status.phase!="Running")]}{.metadata.namespace}/{.metadata.name}{" "}{.status.phase}{"\n"}{end}'
```

---

## Custom columns — `kubectl get -o custom-columns`

Thay vì nhớ jsonpath dài, tạo cột tùy chỉnh:

```bash
# Pod: NAME, IP, NODE
kubectl get pods -n cka-lab -o custom-columns=\
NAME:.metadata.name,\
IP:.status.podIP,\
NODE:.spec.nodeName

# Deployment: NAME, READY, IMAGE
kubectl get deploy -n cka-lab -o custom-columns=\
NAME:.metadata.name,\
READY:.status.readyReplicas,\
IMAGE:.spec.template.spec.containers[0].image

# Node: NAME, CPU, MEMORY
kubectl get nodes -o custom-columns=\
NAME:.metadata.name,\
CPU:.status.capacity.cpu,\
MEM:.status.capacity.memory
```

> **Thi CKA:** `custom-columns` dễ đọc hơn jsonpath thuần khi cần bảng nhiều cột.

---

## Sắp xếp — `--sort-by`

Dùng jsonpath (không có `{}`) làm key sort:

```bash
# Pod sort theo tên
kubectl get pods -n cka-lab --sort-by=.metadata.name

# Event mới nhất trước
kubectl get events -n cka-lab --sort-by='.lastTimestamp'

# Node sort theo CPU
kubectl get nodes --sort-by=.status.capacity.cpu
```

---

## Filter với `[?()]`

Lọc phần tử trong mảng theo điều kiện:

```bash
# Condition Ready = False
kubectl get pod POD -n NS -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}'

# Address InternalIP
kubectl get node NODE -o jsonpath='{.status.addresses[?(@.type=="InternalIP")].address}'

# Container có tên "sidecar"
kubectl get pod POD -n NS -o jsonpath='{.spec.containers[?(@.name=="sidecar")].image}'
```

**Lưu ý:** Trong shell, escape hoặc dùng nháy đơn bọc ngoài; bên trong filter dùng `"` cho string.

---

## JSONPath cho CKS

### RBAC & ServiceAccount

```bash
# Secret gắn với SA (legacy token)
kubectl get sa default -n cks-lab -o jsonpath='{.secrets[*].name}'

# Kiểm tra automountServiceAccountToken
kubectl get sa APP-SA -n cks-lab -o jsonpath='{.automountServiceAccountToken}'
```

### Pod SecurityContext

```bash
# runAsUser
kubectl get pod POD -n cks-lab -o jsonpath='{.spec.securityContext.runAsUser}'

# readOnlyRootFilesystem container đầu
kubectl get pod POD -n cks-lab -o jsonpath='{.spec.containers[0].securityContext.readOnlyRootFilesystem}'

# Capabilities drop
kubectl get pod POD -n cks-lab -o jsonpath='{.spec.containers[0].securityContext.capabilities.drop}'
```

### NetworkPolicy

```bash
# Danh sách policyTypes
kubectl get netpol POLICY -n cks-lab -o jsonpath='{.spec.policyTypes}'

# Port cho phép ingress
kubectl get netpol POLICY -n cks-lab -o jsonpath='{.spec.ingress[*].ports[*].port}'
```

---

## So sánh: jsonpath vs json vs yaml vs wide

| Output | Khi nào dùng |
|--------|--------------|
| `-o jsonpath='{...}'` | Lấy **một hoặc vài field** cụ thể |
| `-o json` | Xem toàn bộ object, pipe sang `jq` |
| `-o yaml` | Sửa và apply lại |
| `-o wide` | Bảng nhanh (IP, Node) — không cần nhớ path |
| `-o custom-columns=...` | Bảng tùy chỉnh nhiều cột |

```bash
# wide — nhanh khi ôn lab
kubectl get pods -n cka-lab -o wide

# jsonpath — chính xác field cần thiết khi thi
kubectl get pods -n cka-lab -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'
```

---

## Lỗi thường gặp

| Lỗi | Nguyên nhân | Cách sửa |
|-----|-------------|----------|
| `<no value>` | Field không tồn tại hoặc null | `kubectl get ... -o yaml` kiểm tra path |
| Shell cắt path | Thiếu nháy đơn | `-o jsonpath='{.metadata.name}'` |
| Mảng rỗng | Chưa có replica/condition | Kiểm tra `status` object |
| Base64 lẫn text | Secret `.data` luôn base64 | Pipe `base64 -d` |
| Filter không match | Sai `@.type` hoặc quote | Copy path từ `-o json` |

### Debug path nhanh

```bash
# 1. Xem full JSON
kubectl get pod POD -n NS -o json | less

# 2. Hoặc dùng jq (nếu có trên máy thi — không bắt buộc)
kubectl get pod POD -n NS -o json | jq '.status.conditions'

# 3. explain field
kubectl explain pod.status.conditions
```

---

## Bài tập thực hành (15 phút)

Chạy sau khi setup lab (`scripts/01-setup-lab.sh`):

```bash
kubectl config set-context --current --namespace=cka-lab
kubectl run jp-web --image=nginx:1.25 --labels=app=jp -n cka-lab
kubectl wait --for=condition=Ready pod/jp-web -n cka-lab --timeout=60s
```

1. In **tên** pod `jp-web`.
2. In **podIP** của `jp-web`.
3. In **image** container đầu tiên.
4. In tất cả pod trong `cka-lab` dạng `NAME IP` (mỗi dòng).
5. Tạo custom column: `NAME`, `STATUS`, `NODE`.
6. Lấy giá trị key `password` từ secret `db-secret` (lab 04) và decode.

<details>
<summary>Đáp án</summary>

```bash
kubectl get pod jp-web -n cka-lab -o jsonpath='{.metadata.name}'
kubectl get pod jp-web -n cka-lab -o jsonpath='{.status.podIP}'
kubectl get pod jp-web -n cka-lab -o jsonpath='{.spec.containers[0].image}'
kubectl get pods -n cka-lab -o jsonpath='{range .items[*]}{.metadata.name}{" "}{.status.podIP}{"\n"}{end}'
kubectl get pods -n cka-lab -o custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName
kubectl get secret db-secret -n cka-lab -o jsonpath='{.data.password}' | base64 -d && echo
```

</details>

---

## Liên kết

- Cheatsheet nhanh: [cheatsheet/jsonpath.md](../cheatsheet/jsonpath.md)
- Lab Secret (jsonpath decode): [lab04-config-secret.md](../labs/basic/lab04-config-secret.md)
- Chiến lược thi: [09-mock-exam-chien-luoc.md](09-mock-exam-chien-luoc.md)
- [Kubernetes — JSONPath support](https://kubernetes.io/docs/reference/kubectl/jsonpath/)

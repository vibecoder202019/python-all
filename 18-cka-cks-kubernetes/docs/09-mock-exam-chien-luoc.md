# Chiến lược thi CKA & CKS

## Trước ngày thi

- [ ] Đăng ký slot thi (PSI / Killer.sh remote exam)
- [ ] Test webcam, màn hình, internet
- [ ] Bookmark: https://kubernetes.io/docs/
- [ ] Ôn cheatsheet trong module này
- [ ] Ngủ đủ — thi 2 giờ cần tập trung

## Trong phòng thi

### Setup nhanh (2 phút đầu)

```bash
# Alias tiết kiệm thời gian
alias k=kubectl
export do="--dry-run=client -o yaml"
complete -F __start_kubectl k

# Set namespace nếu đề cho sẵn
k config set-context --current --namespace=<exam-namespace>
```

### Phân bổ thời gian CKA (~17 task / 120 phút)

| Độ khó | Thời gian/task | Chiến lược |
|--------|----------------|------------|
| Dễ | 3–5 phút | Làm trước |
| Trung bình | 7–10 phút | Làm tiếp |
| Khó | 15–20 phút | Skip, quay lại cuối |

### Lệnh tạo YAML nhanh nhất

```bash
# Pod
k run nginx --image=nginx $do > pod.yaml

# Deployment
k create deployment web --image=nginx --replicas=3 $do > deploy.yaml

# Service
k expose deployment web --port=80 $do > svc.yaml

# Role
k create role name --verb=get,list --resource=pods $do > role.yaml
```

### `kubectl explain` — Bạn của bạn

```bash
k explain pod.spec.containers.resources
k explain networkpolicy.spec
k explain persistentvolumeclaim.spec
```

### JSONPath — Lấy field nhanh

Khi đề hỏi IP pod, số replica ready, decode secret — dùng `-o jsonpath`:

```bash
# IP pod
k get pod POD -n NS -o jsonpath='{.status.podIP}'

# Replica ready
k get deploy NAME -n NS -o jsonpath='{.status.readyReplicas}'

# Nhiều pod — mỗi dòng NAME + IP
k get pods -n NS -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'

# Bảng tùy chỉnh
k get pods -n NS -o custom-columns=NAME:.metadata.name,IP:.status.podIP,NODE:.spec.nodeName
```

Chi tiết: [docs/10-jsonpath-kubectl.md](10-jsonpath-kubectl.md) | Cheatsheet: [cheatsheet/jsonpath.md](../cheatsheet/jsonpath.md)

### Checklist trước khi Submit task

- [ ] Đúng **namespace**?
- [ ] Đúng **tên** resource (case-sensitive)?
- [ ] `kubectl get` xác nhận resource **Running/Bound**?
- [ ] Label/selector khớp (Service ↔ Pod)?

## Mock Exam Lab

→ [Lab 14 — Mock Exam](../labs/advanced/lab14-mock-exam.md)

## Tài liệu được phép mở khi thi

- https://kubernetes.io/docs/ (chính thức)
- https://github.com/kubernetes/kubernetes
- https://kubernetes.io/blog/
- **KHÔNG** được: GitHub khác, Stack Overflow, blog cá nhân

## Sau khi đậu

- CKA valid 3 năm → đủ điều kiện thi CKS
- CKS valid 2 năm
- Renewal: exam hoặc PDUs (xem CNCF policy mới nhất)

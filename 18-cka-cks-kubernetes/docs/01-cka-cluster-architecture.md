# CKA Domain 1 — Cluster Architecture, Installation & Configuration (25%)

## Kiến trúc control plane

```
┌─────────────────────────────────────────────────────────┐
│                    Control Plane                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │ kube-    │ │ etcd     │ │ kube-    │ │ kube-    │  │
│  │ apiserver│ │ (DB)     │ │ scheduler│ │ controller│  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
└─────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────────────────────────────────────┐
│  Worker Node(s)                                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                 │
│  │ kubelet  │ │ kube-    │ │ Container│                 │
│  │          │ │ proxy    │ │ Runtime  │                 │
│  └──────────┘ └──────────┘ └──────────┘                 │
└─────────────────────────────────────────────────────────┘
```

| Component | Vai trò |
|-----------|---------|
| **kube-apiserver** | Cổng API duy nhất, xác thực, validate |
| **etcd** | Lưu toàn bộ state cluster (key-value) |
| **kube-scheduler** | Chọn node chạy pod mới |
| **kube-controller-manager** | Vòng lặp điều khiển (ReplicaSet, Node...) |
| **kubelet** | Agent trên worker, quản lý pod |
| **kube-proxy** | Rule network (iptables/IPVS) cho Service |

---

## kubeadm — Cài cluster (thường gặp thi CKA)

```bash
# === Trên ALL nodes ===
# Tắt swap — bắt buộc cho kubelet
sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

# === Chỉ control plane ===
# khởi tạo cluster
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# Cấu hình kubectl cho user thường
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Cài CNI (Flannel ví dụ)
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml

# === Join worker node ===
# Copy lệnh từ output kubeadm init:
sudo kubeadm join <control-plane-ip>:6443 --token <token> \
  --discovery-token-ca-cert-hash sha256:<hash>
```

---

## Backup & Restore etcd (CKA hay thi)

```bash
# Backup etcd — snapshot file
# ETCDCTL_API=3 — dùng etcd v3 API
sudo ETCDCTL_API=3 etcdctl snapshot save /backup/etcd-snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Kiểm tra snapshot
sudo ETCDCTL_API=3 etcdctl snapshot status /backup/etcd-snapshot.db --write-out=table

# Restore (cluster phải stop, lab trên VM)
# 1. kubeadm reset / stop kube-apiserver
# 2. etcdctl snapshot restore ...
# 3. Khởi động lại control plane
```

> **Thi CKA:** Học thuộc đường dẫn cert etcd và lệnh snapshot — đề thường cho sẵn path.

---

## Upgrade cluster (kubeadm)

```bash
# 1. Upgrade kubeadm trên control plane
sudo apt-get update && sudo apt-get install -y kubeadm=1.29.x-00
sudo kubeadm upgrade plan
sudo kubeadm upgrade apply v1.29.x

# 2. Upgrade kubelet + kubectl trên control plane
sudo apt-get install -y kubelet=1.29.x-00 kubectl=1.29.x-00
sudo systemctl daemon-reload && sudo systemctl restart kubelet

# 3. Drain node trước khi upgrade worker
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data

# 4. Lặp bước 2 trên worker, rồi:
sudo kubeadm upgrade node
kubectl uncordon <node-name>
```

---

## kubectl context & namespace mặc định

```bash
# Xem context hiện tại
kubectl config get-contexts

# Đổi context
kubectl config use-context my-cluster

# Set namespace mặc định — tránh gõ -n mỗi lần (tiết kiệm thời gian thi)
kubectl config set-context --current --namespace=exam-ns
```

---

## Lab liên quan

- [Lab 10 — Backup etcd](../labs/advanced/lab10-etcd-backup.md)

## Bước tiếp theo

→ [02-cka-workloads-scheduling.md](02-cka-workloads-scheduling.md)

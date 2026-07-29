# Lab 10 — Backup etcd (Advanced | CKA)

**Thời gian:** 60 phút | **Cần:** cluster kubeadm (VM), quyền root

> Lab local minikube **không có etcd truy cập trực tiếp** — đọc lý thuyết + thực hành trên VM.

## Lý thuyết cần thuộc

```bash
# Đường dẫn cert etcd (kubeadm default)
/etc/kubernetes/pki/etcd/ca.crt
/etc/kubernetes/pki/etcd/server.crt
/etc/kubernetes/pki/etcd/server.key

# Backup
sudo ETCDCTL_API=3 etcdctl snapshot save /opt/backup.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Verify snapshot
sudo ETCDCTL_API=3 etcdctl snapshot status /opt/backup.db -w table
```

## Bài tập lab (simulation trên minikube)

```bash
# Ghi chú lệnh backup vào file
# Giải thích từng flag: --endpoints, --cacert, --cert, --key
cat cheatsheet/etcd-backup.md
```

## VM lab (tuỳ chọn)

1. SSH vào control plane
2. Chạy backup
3. Tạo pod test, backup lại
4. (Advanced) restore theo docs 01

## Verify

Hoàn thành checklist trong `exercises/bai_tap.md` bài 10.

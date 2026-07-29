# Cheatsheet CKA — in ra mang vào phòng thi (ôn tập)
# Alias
alias k=kubectl
export do="--dry-run=client -o yaml"
complete -F __start_kubectl k

# Context / namespace
k config set-context --current --namespace=exam-ns
k config get-contexts

# Tạo nhanh
k run NAME --image=IMG $do > pod.yaml
k create deployment NAME --image=IMG --replicas=3 $do > deploy.yaml
k expose deployment NAME --port=80 --target-port=8080 $do > svc.yaml
k create configmap NAME --from-literal=k=v $do > cm.yaml
k create secret generic NAME --from-literal=k=v $do > secret.yaml

# RBAC
k create role NAME --verb=get,list --resource=pods $do > role.yaml
k create rolebinding NAME --role=ROLE --serviceaccount=NS:SA $do > rb.yaml
k auth can-i create pods --as=system:serviceaccount:NS:SA -n NS

# Debug
k get events -n NS --sort-by='.lastTimestamp'
k describe pod POD -n NS
k logs POD -n NS [--previous] [-c CONTAINER]
k exec -it POD -n NS -- sh

# Deployment
k scale deploy NAME --replicas=N -n NS
k set image deploy/NAME ctr=IMG:TAG -n NS
k rollout status/history/undo deploy/NAME -n NS

# Node
k drain NODE --ignore-daemonsets --delete-emptydir-data
k uncordon NODE
k taint nodes NODE key=val:NoSchedule
k label nodes NODE disktype=ssd

# Explain
k explain pod.spec.containers.resources
k explain networkpolicy.spec

# etcd backup
ETCDCTL_API=3 etcdctl snapshot save /backup.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

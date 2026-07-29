# Cheatsheet CKS

# Pod Security — namespace label
kubectl label ns cks-lab pod-security.kubernetes.io/enforce=restricted

# SecurityContext pod template
securityContext:
  runAsNonRoot: true
  seccompProfile: { type: RuntimeDefault }
  capabilities: { drop: [ALL] }
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true

# NetworkPolicy deny all
spec:
  podSelector: {}
  policyTypes: [Ingress, Egress]

# Audit policy path (kube-apiserver static pod)
--audit-policy-file=/etc/kubernetes/audit-policy.yaml
--audit-log-path=/var/log/kubernetes/audit.log

# Image scan
trivy image nginx:1.25

# SA token (1.24+)
kubectl create token SA -n NS --duration=1h

# Falco
helm install falco falcosecurity/falco -n falco --create-namespace

# JSONPath — kiểm tra security nhanh
kubectl get pod POD -n NS -o jsonpath='{.spec.securityContext.runAsUser}'
kubectl get pod POD -n NS -o jsonpath='{.spec.containers[0].securityContext.readOnlyRootFilesystem}'
kubectl get pod POD -n NS -o jsonpath='{.spec.containers[0].securityContext.capabilities.drop}'
kubectl get sa SA -n NS -o jsonpath='{.automountServiceAccountToken}'
kubectl get netpol POL -n NS -o jsonpath='{.spec.policyTypes}'

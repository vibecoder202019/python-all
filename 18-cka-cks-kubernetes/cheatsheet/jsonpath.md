# Cheatsheet JSONPath — CKA/CKS (in mang vào phòng thi)

# Cú pháp
# .field          truy cập field
# [0] [1]         phần tử mảng
# [*]             tất cả phần tử
# [?(@.x=="y")]   filter
# {range} {end}   lặp in nhiều dòng

# === POD ===
k get pod POD -n NS -o jsonpath='{.metadata.name}'
k get pod POD -n NS -o jsonpath='{.status.podIP}'
k get pod POD -n NS -o jsonpath='{.spec.nodeName}'
k get pod POD -n NS -o jsonpath='{.status.phase}'
k get pod POD -n NS -o jsonpath='{.spec.containers[*].name}'
k get pod POD -n NS -o jsonpath='{.spec.containers[0].image}'
k get pod POD -n NS -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}'

# === DEPLOYMENT ===
k get deploy NAME -n NS -o jsonpath='{.status.readyReplicas}'
k get deploy NAME -n NS -o jsonpath='{.spec.template.spec.containers[0].image}'

# === SERVICE ===
k get svc NAME -n NS -o jsonpath='{.spec.clusterIP}'
k get svc NAME -n NS -o jsonpath='{.spec.ports[0].port}'

# === NODE ===
k get nodes -o jsonpath='{.items[*].metadata.name}'
k get node NODE -o jsonpath='{.status.addresses[?(@.type=="InternalIP")].address}'
k get node NODE -o jsonpath='{.spec.taints[*].key}'

# === SECRET (decode) ===
k get secret SEC -n NS -o jsonpath='{.data.KEY}' | base64 -d && echo

# === PVC ===
k get pvc NAME -n NS -o jsonpath='{.status.phase}'
k get pvc NAME -n NS -o jsonpath='{.spec.volumeName}'

# === LẶP NHIỀU DÒNG ===
k get pods -n NS -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'

# === CUSTOM COLUMNS ===
k get pods -n NS -o custom-columns=NAME:.metadata.name,IP:.status.podIP,NODE:.spec.nodeName

# === SORT ===
k get pods -n NS --sort-by=.metadata.name
k get events -n NS --sort-by='.lastTimestamp'

# === CKS — SecurityContext ===
k get pod POD -n NS -o jsonpath='{.spec.securityContext.runAsUser}'
k get pod POD -n NS -o jsonpath='{.spec.containers[0].securityContext.readOnlyRootFilesystem}'

# Debug: k get POD -n NS -o json | less

# Terrakube cheatsheet

# Deploy Compose
bash scripts/01-check-prerequisites.sh
bash scripts/02-prepare-hosts.sh --check
bash scripts/03-deploy-terrakube-compose.sh
bash scripts/04-wait-healthy.sh

# UI lab
https://terrakube.platform.local
admin@example.com / admin   # DOI PASSWORD

# Teardown
bash scripts/05-teardown-compose.sh

# Helm minikube
bash scripts/06-deploy-helm-minikube.sh
bash scripts/09-teardown-helm.sh

# Hierarchy
Organization > Project > Workspace > Run(Plan/Apply)

# VCS working dir (python-all)
21-terraform-ui-terrakube/terraform/sample-workspace

# Logs compose
cd .cache/terrakube-upstream/docker-compose && docker compose logs -f

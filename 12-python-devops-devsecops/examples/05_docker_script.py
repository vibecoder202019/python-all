"""
Module 12 — Ví dụ 5: Docker Automation Script

Chạy: python examples/05_docker_script.py
(Không cần Docker chạy — demo generate Dockerfile & docker-compose)

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Kiểm tra Docker có sẵn không (docker info).
  2. Generate Dockerfile và docker-compose.yml vào data/generated/.
  3. Nếu Docker chạy → liệt kê containers đang active.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - "Docker available: ✅ Yes" hoặc "❌ No (demo mode)".
  - "Generated: .../Dockerfile" và ".../docker-compose.yml".
  - "Running containers: [...]" hoặc skip nếu không có Docker.
═══════════════════════════════════════════════════════════════════════════
"""
import subprocess
from pathlib import Path

MODULE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = MODULE_DIR / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def check_docker_available() -> bool:
    try:
        result = subprocess.run(
            ["docker", "info"], capture_output=True, text=True, timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def generate_dockerfile(app_name: str, port: int) -> str:
    return f"""# Auto-generated Dockerfile for {app_name}
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE {port}

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \\
  CMD python -c "import httpx; httpx.get('http://localhost:{port}/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "{port}"]
"""


def generate_compose(services: list[dict]) -> str:
    lines = ["version: '3.8'", "services:"]
    for svc in services:
        lines.append(f"  {svc['name']}:")
        lines.append(f"    image: {svc.get('image', svc['name'] + ':latest')}")
        lines.append(f"    ports:")
        lines.append(f'      - "{svc["port"]}:{svc["port"]}"')
        if svc.get("env"):
            lines.append(f"    environment:")
            for k, v in svc["env"].items():
                lines.append(f'      {k}: "{v}"')
    return "\n".join(lines)


print("=== Docker Automation ===\n")

docker_ok = check_docker_available()
print(f"Docker available: {'✅ Yes' if docker_ok else '❌ No (demo mode)'}")

dockerfile = generate_dockerfile("demo-api", 8000)
dockerfile_path = OUTPUT_DIR / "Dockerfile"
dockerfile_path.write_text(dockerfile)
print(f"\n1. Generated: {dockerfile_path}")

compose = generate_compose([
    {"name": "api", "port": 8000, "env": {"ENV": "staging"}},
    {"name": "redis", "image": "redis:7-alpine", "port": 6379},
])
compose_path = OUTPUT_DIR / "docker-compose.yml"
compose_path.write_text(compose)
print(f"2. Generated: {compose_path}")

if docker_ok:
    result = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True)
    containers = [c for c in result.stdout.strip().split("\n") if c]
    print(f"\n3. Running containers: {containers or '(none)'}")
else:
    print("\n3. Skip docker ps (Docker not running)")

print("\n✓ Done")

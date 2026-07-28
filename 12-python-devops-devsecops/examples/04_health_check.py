"""
DevOps 04 — Health Check HTTP Services
Chạy: python examples/04_health_check.py
"""
import time
from dataclasses import dataclass
from datetime import datetime

try:
    import httpx
except ImportError:
    print("pip install httpx")
    raise


@dataclass
class HealthResult:
    name: str
    url: str
    status: str  # healthy | unhealthy | unreachable
    status_code: int | None
    response_time_ms: float
    message: str


def check_endpoint(name: str, url: str, timeout: float = 5.0) -> HealthResult:
    start = time.perf_counter()
    try:
        response = httpx.get(url, timeout=timeout, follow_redirects=True)
        elapsed = (time.perf_counter() - start) * 1000
        healthy = response.status_code < 400
        return HealthResult(
            name=name,
            url=url,
            status="healthy" if healthy else "unhealthy",
            status_code=response.status_code,
            response_time_ms=round(elapsed, 1),
            message=f"HTTP {response.status_code}",
        )
    except httpx.ConnectError:
        elapsed = (time.perf_counter() - start) * 1000
        return HealthResult(name, url, "unreachable", None, round(elapsed, 1), "Connection refused")
    except httpx.TimeoutException:
        return HealthResult(name, url, "unreachable", None, timeout * 1000, "Timeout")


ENDPOINTS = [
    ("GitHub API", "https://api.github.com/zen"),
    ("Google", "https://www.google.com"),
    ("Localhost (expect fail)", "http://localhost:9999/health"),
]

print("=== Health Check Monitor ===\n")
print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

results = [check_endpoint(name, url) for name, url in ENDPOINTS]

for r in results:
    icon = "✅" if r.status == "healthy" else "❌"
    print(f"{icon} {r.name:25s} {r.status:12s} {r.response_time_ms:6.0f}ms  {r.message}")

healthy = sum(1 for r in results if r.status == "healthy")
print(f"\nSummary: {healthy}/{len(results)} healthy")
print("\n✓ Done")

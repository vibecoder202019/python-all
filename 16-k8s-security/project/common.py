"""
Module 16 — Tiện ích bảo mật dùng chung

SQL injection detection, rate limiting, phishing URL check, port scan detection.
"""
from __future__ import annotations

import re
import time
from collections import defaultdict
from dataclasses import dataclass, field
from urllib.parse import urlparse

# ── SQL Injection patterns (WAF cơ bản) ──
SQLI_PATTERNS = [
    r"(\%27)|(\')|(\-\-)|(\%23)|(#)",           # quote, comment
    r"((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))",  # OR '1'='1
    r"\b(union\s+select)\b",                     # UNION SELECT
    r"\b(drop\s+table)\b",                       # DROP TABLE
    r"\b(or\s+1\s*=\s*1)\b",                     # OR 1=1
    r"\b(insert\s+into)\b",                       # INSERT INTO
    r"\b(delete\s+from)\b",                       # DELETE FROM
    r"(\%27).*(\%27)",                            # encoded quotes
    r";\s*shutdown",                              # ; shutdown
]
SQLI_REGEX = [re.compile(p, re.IGNORECASE) for p in SQLI_PATTERNS]

# ── Phishing indicators ──
PHISHING_KEYWORDS = [
    "login-verify", "secure-update", "account-suspended",
    "confirm-password", "wallet-connect", "free-bonus",
    "click-here-now", "urgent-action", "verify-account",
]
SUSPICIOUS_TLDS = {".xyz", ".top", ".click", ".work", ".gq", ".tk", ".ml"}


@dataclass
class SecurityCheckResult:
    """Kết quả kiểm tra bảo mật."""
    passed: bool
    threat_type: str
    detail: str
    score: int = 0  # 0=an toàn, 100=nguy hiểm


def detect_sql_injection(text: str) -> SecurityCheckResult:
    """Phát hiện payload SQL injection trong chuỗi input."""
    if not text:
        return SecurityCheckResult(True, "sqli", "Input rỗng — OK")

    for pattern in SQLI_REGEX:
        if pattern.search(text):
            return SecurityCheckResult(
                passed=False,
                threat_type="sqli",
                detail=f"Phát hiện pattern SQLi: {pattern.pattern[:40]}...",
                score=90,
            )
    return SecurityCheckResult(True, "sqli", "Không phát hiện SQL injection")


def check_phishing_url(url: str) -> SecurityCheckResult:
    """Phân tích URL nghi ngờ phishing."""
    try:
        parsed = urlparse(url if "://" in url else f"http://{url}")
    except Exception:
        return SecurityCheckResult(False, "phishing", "URL không hợp lệ", score=50)

    hostname = (parsed.hostname or "").lower()
    path = (parsed.path or "").lower()
    full = f"{hostname}{path}"

    score = 0
    reasons: list[str] = []

    # IP thay vì domain
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", hostname):
        score += 30
        reasons.append("Dùng IP thay vì domain")

    # TLD đáng ngờ
    for tld in SUSPICIOUS_TLDS:
        if hostname.endswith(tld):
            score += 25
            reasons.append(f"TLD đáng ngờ: {tld}")

    # Keyword phishing
    for kw in PHISHING_KEYWORDS:
        if kw in full:
            score += 20
            reasons.append(f"Keyword nghi ngờ: {kw}")

    # Subdomain quá dài (brand spoofing)
    parts = hostname.split(".")
    if len(parts) > 4:
        score += 15
        reasons.append("Subdomain bất thường (brand spoofing?)")

    # @ trong URL (credential hiding)
    if "@" in url:
        score += 40
        reasons.append("Ký tự @ — có thể giấu domain thật")

    if score >= 40:
        return SecurityCheckResult(
            passed=False,
            threat_type="phishing",
            detail="; ".join(reasons) or "URL đáng ngờ",
            score=min(score, 100),
        )
    return SecurityCheckResult(True, "phishing", "URL có vẻ an toàn", score=score)


@dataclass
class RateLimiter:
    """Token bucket rate limiter — chống DDoS/brute-force cơ bản."""
    max_requests: int = 100
    window_seconds: int = 60
    _buckets: dict[str, list[float]] = field(default_factory=lambda: defaultdict(list))

    def is_allowed(self, client_id: str) -> SecurityCheckResult:
        now = time.time()
        window_start = now - self.window_seconds
        # Xóa request cũ ngoài window
        self._buckets[client_id] = [
            t for t in self._buckets[client_id] if t > window_start
        ]
        if len(self._buckets[client_id]) >= self.max_requests:
            return SecurityCheckResult(
                passed=False,
                threat_type="ddos",
                detail=f"Vượt {self.max_requests} req/{self.window_seconds}s — chặn",
                score=80,
            )
        self._buckets[client_id].append(now)
        return SecurityCheckResult(
            passed=True,
            threat_type="ddos",
            detail=f"OK ({len(self._buckets[client_id])}/{self.max_requests})",
        )


def detect_port_scan(
    connection_log: list[dict],
    threshold: int = 10,
    window_seconds: int = 5,
) -> list[SecurityCheckResult]:
    """
    Phát hiện port scan từ log kết nối.

    Log format: [{"src_ip": "10.0.0.5", "dst_port": 22, "timestamp": 1234567890.0}, ...]
    """
    by_src: dict[str, list[dict]] = defaultdict(list)
    for entry in connection_log:
        by_src[entry["src_ip"]].append(entry)

    alerts: list[SecurityCheckResult] = []
    for src_ip, entries in by_src.items():
        entries.sort(key=lambda e: e["timestamp"])
        ports_in_window: set[int] = set()
        window_start = entries[0]["timestamp"] if entries else 0

        for e in entries:
            if e["timestamp"] - window_start > window_seconds:
                ports_in_window = {e["dst_port"]}
                window_start = e["timestamp"]
            else:
                ports_in_window.add(e["dst_port"])

            if len(ports_in_window) >= threshold:
                alerts.append(SecurityCheckResult(
                    passed=False,
                    threat_type="port_scan",
                    detail=f"{src_ip} quét {len(ports_in_window)} port trong {window_seconds}s",
                    score=85,
                ))
                break

    return alerts


def sanitize_input(text: str, max_length: int = 256) -> str:
    """Làm sạch input cơ bản — dùng trước khi query DB."""
    text = text[:max_length]
    # Loại bỏ null byte
    text = text.replace("\x00", "")
    return text.strip()

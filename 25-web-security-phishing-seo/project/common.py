"""
Module 25 — Tiện ích phòng thủ web (phishing, headers, OWASP, SEO integrity).

Chỉ dùng để phân tích / harden / triage — không dùng để tấn công bên thứ ba.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from html import escape
from typing import Any
from urllib.parse import urlparse

# ── Phishing heuristics ──
PHISHING_KEYWORDS = [
    "login-verify",
    "secure-update",
    "account-suspended",
    "confirm-password",
    "wallet-connect",
    "free-bonus",
    "urgent-action",
    "verify-account",
    "reset-now",
    "claim-reward",
]
SUSPICIOUS_TLDS = {".xyz", ".top", ".click", ".work", ".gq", ".tk", ".ml", ".cf"}
BRAND_SPOOF_HINTS = ["paypal", "google", "apple", "microsoft", "facebook", "amazon", "banking"]

EMAIL_URGENCY = [
    "immediate action",
    "within 24 hours",
    "account will be closed",
    "verify now",
    "unusual login",
    "suspended",
]


@dataclass
class CheckResult:
    passed: bool
    category: str
    detail: str
    score: int = 0  # 0 safe → 100 high risk
    findings: list[str] = field(default_factory=list)


def analyze_phishing_url(url: str) -> CheckResult:
    """Heuristic phishing URL check (defense / awareness)."""
    raw = url.strip()
    try:
        parsed = urlparse(raw if "://" in raw else f"http://{raw}")
    except Exception:
        return CheckResult(False, "phishing_url", "URL không parse được", 50)

    host = (parsed.hostname or "").lower()
    path = (parsed.path or "").lower()
    full = f"{host}{path}"
    score = 0
    findings: list[str] = []

    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host):
        score += 30
        findings.append("Dùng IP thay domain")

    for tld in SUSPICIOUS_TLDS:
        if host.endswith(tld):
            score += 25
            findings.append(f"TLD đáng ngờ: {tld}")

    for kw in PHISHING_KEYWORDS:
        if kw in full:
            score += 20
            findings.append(f"Keyword: {kw}")

    if "@" in raw:
        score += 40
        findings.append("Ký tự @ — có thể che domain thật")

    if len(host.split(".")) > 4:
        score += 15
        findings.append("Subdomain quá sâu (spoof?)")

    # Brand name in subdomain but not matching real brand TLD pattern (heuristic)
    for brand in BRAND_SPOOF_HINTS:
        if brand in host and not host.endswith(f"{brand}.com") and not host.endswith(f"{brand}.vn"):
            if brand in host.replace("-", ""):
                score += 15
                findings.append(f"Có thể giả mạo brand: {brand}")
                break

    if "-" in host and host.count("-") >= 3:
        score += 10
        findings.append("Nhiều dấu gạch trong hostname")

    passed = score < 40
    return CheckResult(
        passed=passed,
        category="phishing_url",
        detail="; ".join(findings) if findings else "Không thấy tín hiệu mạnh",
        score=min(score, 100),
        findings=findings,
    )


def analyze_email_text(text: str) -> CheckResult:
    """Red-flag scan trên nội dung email (lab fixture, không gửi mail thật)."""
    lower = text.lower()
    score = 0
    findings: list[str] = []

    for phrase in EMAIL_URGENCY:
        if phrase in lower:
            score += 15
            findings.append(f"Ngôn ngữ gấp: «{phrase}»")

    if "http://" in lower and "https://" not in lower:
        score += 10
        findings.append("Link HTTP không mã hóa")

    # Lookalike: display text vs URL mismatch (very simple)
    if re.search(r"https?://[^\s]+", text) and ("click here" in lower or "đăng nhập" in lower):
        score += 20
        findings.append("CTA mơ hồ kèm URL — kiểm tra domain thật")

    if "wire transfer" in lower or "gift card" in lower or "crypto" in lower:
        score += 25
        findings.append("Yêu cầu chuyển tiền / gift card / crypto")

    if re.search(r"from:.*@[a-z0-9.-]+\.(xyz|tk|ml|gq)\b", lower):
        score += 30
        findings.append("From domain TLD đáng ngờ")

    passed = score < 35
    return CheckResult(
        passed=passed,
        category="phishing_email",
        detail="; ".join(findings) if findings else "Ít tín hiệu khẩn",
        score=min(score, 100),
        findings=findings,
    )


RECOMMENDED_HEADERS = {
    "strict-transport-security": "HSTS — ép HTTPS",
    "content-security-policy": "CSP — hạn chế script lạ",
    "x-frame-options": "Chống clickjacking / phishing iframe",
    "x-content-type-options": "nosniff",
    "referrer-policy": "Giảm leak referrer",
    "permissions-policy": "Hạn chế camera/mic…",
}


def audit_security_headers(headers: dict[str, str]) -> CheckResult:
    """Kiểm tra thiếu security headers (defense)."""
    normalized = {k.lower(): v for k, v in headers.items()}
    missing: list[str] = []
    for key, why in RECOMMENDED_HEADERS.items():
        if key not in normalized or not normalized[key].strip():
            missing.append(f"{key} ({why})")

    score = min(len(missing) * 15, 100)
    return CheckResult(
        passed=len(missing) == 0,
        category="security_headers",
        detail="Thiếu: " + "; ".join(missing) if missing else "Đủ header cơ bản",
        score=score,
        findings=missing,
    )


XSS_PATTERNS = [
    re.compile(r"<script\b", re.I),
    re.compile(r"javascript:", re.I),
    re.compile(r"onerror\s*=", re.I),
    re.compile(r"onload\s*=", re.I),
]
SQLI_PATTERNS = [
    re.compile(r"\bunion\s+select\b", re.I),
    re.compile(r"\bor\s+1\s*=\s*1\b", re.I),
    re.compile(r";\s*drop\s+table\b", re.I),
    re.compile(r"'?\s*or\s+'?1'?\s*=\s*'?1", re.I),
]


def sanitize_user_input(value: str) -> tuple[str, CheckResult]:
    """
    Defense: phát hiện XSS/SQLi pattern + escape HTML output.
    Không phải WAF production — chỉ lab.
    """
    findings: list[str] = []
    score = 0
    for p in XSS_PATTERNS:
        if p.search(value):
            findings.append(f"XSS pattern: {p.pattern}")
            score += 40
    for p in SQLI_PATTERNS:
        if p.search(value):
            findings.append(f"SQLi pattern: {p.pattern}")
            score += 40

    safe = escape(value)
    return safe, CheckResult(
        passed=score == 0,
        category="input_sanitize",
        detail="; ".join(findings) if findings else "Input sạch (lab heuristics)",
        score=min(score, 100),
        findings=findings,
    )


@dataclass
class SiteAuditInput:
    """Fixture mô phỏng dữ liệu chủ site tự audit."""
    robots_txt: str
    sitemap_urls: list[str]
    indexed_suspicious_paths: list[str]
    security_issues: list[str]
    manual_actions: list[str]
    spammy_outbound_links: int = 0


def audit_seo_integrity(site: SiteAuditInput) -> CheckResult:
    """Triage tín hiệu khiến site của bạn có thể mất trust / ranking."""
    findings: list[str] = []
    score = 0

    if "Disallow: /" in site.robots_txt and "Allow:" not in site.robots_txt:
        score += 25
        findings.append("robots.txt có thể chặn toàn bộ crawl")

    if not site.sitemap_urls:
        score += 10
        findings.append("Không có URL trong sitemap")

    for path in site.indexed_suspicious_paths:
        score += 20
        findings.append(f"Path nghi bị inject/spam index: {path}")

    for issue in site.security_issues:
        score += 30
        findings.append(f"Security Issue (GSC): {issue}")

    for action in site.manual_actions:
        score += 35
        findings.append(f"Manual Action: {action}")

    if site.spammy_outbound_links >= 50:
        score += 20
        findings.append(f"Nhiều outbound link spam ({site.spammy_outbound_links})")

    return CheckResult(
        passed=score < 40,
        category="seo_integrity",
        detail="; ".join(findings) if findings else "Không thấy tín hiệu integrity xấu (fixture)",
        score=min(score, 100),
        findings=findings,
    )


def triage_ranking_drop(signals: dict[str, Any]) -> dict[str, Any]:
    """
    Quyết định nhánh khôi phục khi traffic/organic giảm.
    signals: keys từ fixture Search Console-like.
    """
    security = signals.get("security_issues") or []
    manual = signals.get("manual_actions") or []
    coverage_errors = int(signals.get("coverage_errors") or 0)
    after_core_update = bool(signals.get("after_core_update"))

    if security:
        branch = "security_compromise"
        steps = [
            "Isolate / lấy offline trang độc hại",
            "Đổi toàn bộ password + rotate secrets",
            "Quét backdoor (CMS plugins, web shells)",
            "Xóa URL spam khỏi index (Removals)",
            "Request review trong Search Console",
        ]
    elif manual:
        branch = "manual_action"
        steps = [
            "Đọc Manual Actions report",
            "Gỡ nội dung / link vi phạm",
            "Sửa cloaking / doorway nếu có",
            "Submit reconsideration request",
        ]
    elif coverage_errors > 100:
        branch = "technical_indexing"
        steps = [
            "Kiểm tra robots.txt / noindex",
            "Sửa sitemap & canonical",
            "Xử lý soft-404 / redirect loop",
            "URL Inspection → Request indexing (có chọn lọc)",
        ]
    elif after_core_update:
        branch = "quality_update"
        steps = [
            "So sánh trang top vs đối thủ chất lượng",
            "Giảm thin/AI-spam content",
            "Củng cố E-E-A-T, nguồn gốc tác giả",
            "Theo dõi 2–4 tuần — không panics",
        ]
    else:
        branch = "monitor"
        steps = [
            "Kiểm tra Analytics filter / tracking bug",
            "Đối chiếu seasonality",
            "Theo dõi GSC Performance 28 ngày",
        ]

    return {
        "branch": branch,
        "priority": "P0" if branch in ("security_compromise", "manual_action") else "P1",
        "steps": steps,
        "note": "Checklist cho chủ site — không phải kỹ thuật tấn công SEO đối thủ",
    }

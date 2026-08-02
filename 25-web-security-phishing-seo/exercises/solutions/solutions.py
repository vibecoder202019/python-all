"""Gợi ý đáp án Module 25 — xem sau khi tự làm."""
from __future__ import annotations


def is_lookalike_domain(candidate: str, brand: str, max_distance: int = 2) -> bool:
    c = candidate.lower().split(".")[0]
    b = brand.lower()
    if c == b:
        return False
    # Hamming-ish on equal length; else abs len + mismatch
    if abs(len(c) - len(b)) > max_distance:
        return False
    dist = sum(1 for x, y in zip(c, b) if x != y) + abs(len(c) - len(b))
    return dist <= max_distance and dist > 0


def header_remediation(missing: list[str]) -> list[str]:
    tips = {
        "strict-transport-security": "add_header Strict-Transport-Security 'max-age=31536000' always;",
        "content-security-policy": "add_header Content-Security-Policy \"default-src 'self'\";",
        "x-frame-options": "add_header X-Frame-Options DENY;",
    }
    return [tips.get(m.split()[0].lower(), f"Set header: {m}") for m in missing]


def triage_with_secondary(signals: dict) -> dict:
    security = signals.get("security_issues") or []
    manual = signals.get("manual_actions") or []
    if security:
        out = {"branch": "security_compromise", "priority": "P0"}
        if manual:
            out["secondary"] = "manual_action"
        return out
    if manual:
        return {"branch": "manual_action", "priority": "P0"}
    return {"branch": "monitor", "priority": "P1"}

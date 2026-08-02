"""
Module 12 — Monitoring helpers: website LIVE/DIE + alert noise filter.

Dùng trong examples/07–08 và step06_final (live-or-die, filter-alerts).
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable

try:
    import httpx
except ImportError:  # pragma: no cover
    httpx = None  # type: ignore


# ── Website LIVE / DIE ─────────────────────────────────────────────────────

@dataclass
class SiteCheck:
    name: str
    url: str
    state: str  # LIVE | DIE
    status_code: int | None
    latency_ms: float
    reason: str
    checked_at: str


def check_website(
    name: str,
    url: str,
    *,
    timeout: float = 5.0,
    expect_status: int | None = None,
    expect_body_contains: str | None = None,
) -> SiteCheck:
    """Ping URL — LIVE nếu HTTP OK (và khớp expect_*), ngược lại DIE."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if httpx is None:
        return SiteCheck(name, url, "DIE", None, 0.0, "httpx not installed", now)

    start = time.perf_counter()
    try:
        resp = httpx.get(url, timeout=timeout, follow_redirects=True)
        ms = round((time.perf_counter() - start) * 1000, 1)
        code = resp.status_code

        if expect_status is not None and code != expect_status:
            return SiteCheck(
                name, url, "DIE", code, ms,
                f"expect status {expect_status}, got {code}", now,
            )
        if expect_status is None and code >= 400:
            return SiteCheck(name, url, "DIE", code, ms, f"HTTP {code}", now)
        if expect_body_contains and expect_body_contains not in resp.text:
            return SiteCheck(
                name, url, "DIE", code, ms,
                f"body missing {expect_body_contains!r}", now,
            )
        return SiteCheck(name, url, "LIVE", code, ms, f"HTTP {code}", now)
    except httpx.TimeoutException:
        ms = round((time.perf_counter() - start) * 1000, 1)
        return SiteCheck(name, url, "DIE", None, ms, "timeout", now)
    except httpx.ConnectError as exc:
        ms = round((time.perf_counter() - start) * 1000, 1)
        return SiteCheck(name, url, "DIE", None, ms, f"connect: {exc}"[:80], now)
    except Exception as exc:  # noqa: BLE001
        ms = round((time.perf_counter() - start) * 1000, 1)
        return SiteCheck(name, url, "DIE", None, ms, str(exc)[:80], now)


def summarize_sites(results: Iterable[SiteCheck]) -> dict[str, Any]:
    rows = list(results)
    live = sum(1 for r in rows if r.state == "LIVE")
    return {
        "total": len(rows),
        "live": live,
        "die": len(rows) - live,
        "all_live": live == len(rows) and len(rows) > 0,
    }


# ── Alert noise filter ─────────────────────────────────────────────────────

SEVERITY_RANK = {"info": 0, "low": 1, "warning": 2, "critical": 3}


@dataclass
class AlertEvent:
    """Một sự kiện thô từ monitor / Prometheus / log."""

    alertname: str
    severity: str = "warning"
    status: str = "firing"  # firing | resolved
    instance: str = ""
    labels: dict[str, str] = field(default_factory=dict)
    ts: float = field(default_factory=time.time)
    message: str = ""


@dataclass
class FilterDecision:
    action: str  # SEND | DROP
    reason: str
    alert: AlertEvent


@dataclass
class AlertFilterConfig:
    """Chống nhiễu alert — cấu hình tối thiểu cho lab."""

    min_severity: str = "warning"
    consecutive_failures: int = 3
    cooldown_seconds: float = 300.0
    exclude_alertnames: tuple[str, ...] = ()
    exclude_instances: tuple[str, ...] = ()
    exclude_label_pairs: tuple[tuple[str, str], ...] = ()
    # Chỉ gửi khi đổi trạng thái (LIVE→DIE / DIE→LIVE) — giảm spam
    state_change_only: bool = True


class AlertNoiseFilter:
    """
    Pipeline filter:
      1) exclude name/instance/labels
      2) severity gate
      3) consecutive failures (chỉ gửi khi đủ N lần firing liên tiếp)
      4) cooldown / dedupe
      5) state-change only (resolved cũng gửi 1 lần khi hồi phục)
    """

    def __init__(self, config: AlertFilterConfig | None = None) -> None:
        self.config = config or AlertFilterConfig()
        self._fail_streak: dict[str, int] = {}
        self._last_sent: dict[str, float] = {}
        self._last_state: dict[str, str] = {}  # key → firing|resolved

    def _key(self, alert: AlertEvent) -> str:
        return f"{alert.alertname}|{alert.instance}"

    def evaluate(self, alert: AlertEvent) -> FilterDecision:
        cfg = self.config
        key = self._key(alert)

        if alert.alertname in cfg.exclude_alertnames:
            return FilterDecision("DROP", "exclude_alertname", alert)
        if alert.instance in cfg.exclude_instances:
            return FilterDecision("DROP", "exclude_instance", alert)
        for lk, lv in cfg.exclude_label_pairs:
            if alert.labels.get(lk) == lv:
                return FilterDecision("DROP", f"exclude_label:{lk}={lv}", alert)

        sev = SEVERITY_RANK.get(alert.severity.lower(), 1)
        min_sev = SEVERITY_RANK.get(cfg.min_severity.lower(), 2)
        if sev < min_sev:
            return FilterDecision("DROP", f"severity<{cfg.min_severity}", alert)

        if alert.status == "resolved":
            self._fail_streak[key] = 0
            prev = self._last_state.get(key)
            self._last_state[key] = "resolved"
            if cfg.state_change_only and prev != "firing":
                return FilterDecision("DROP", "resolved_without_prior_firing", alert)
            # Recovery = state change quan trọng → luôn SEND (không cooldown)
            self._last_sent[key] = time.time()
            return FilterDecision("SEND", "recovery", alert)

        # firing
        streak = self._fail_streak.get(key, 0) + 1
        self._fail_streak[key] = streak
        if streak < cfg.consecutive_failures:
            return FilterDecision(
                "DROP",
                f"consecutive {streak}/{cfg.consecutive_failures}",
                alert,
            )

        prev = self._last_state.get(key)
        self._last_state[key] = "firing"
        if cfg.state_change_only and prev == "firing":
            last = self._last_sent.get(key, 0.0)
            if time.time() - last < cfg.cooldown_seconds:
                return FilterDecision("DROP", "cooldown_same_state", alert)

        last = self._last_sent.get(key, 0.0)
        if time.time() - last < cfg.cooldown_seconds and prev == "firing":
            return FilterDecision("DROP", "cooldown", alert)

        self._last_sent[key] = time.time()
        return FilterDecision("SEND", "threshold_met", alert)

    def process_batch(self, alerts: list[AlertEvent]) -> list[FilterDecision]:
        return [self.evaluate(a) for a in alerts]

#!/usr/bin/env python3
"""Ví dụ 04 — Sinh Backstage catalog Resource từ AWX templates."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "project"))

from awx_client import AwxClient, AwxConfig
from backstage_catalog import build_catalog_documents, render_catalog_yaml, validate_catalog_entity


def main() -> None:
    print("=== 04: Backstage catalog from AWX ===\n")
    client = AwxClient(AwxConfig.from_env(force_demo=True))
    docs = build_catalog_documents(client.list_job_templates())
    for d in docs:
        errs = validate_catalog_entity(d)
        assert not errs, errs
        print(f"✓ {d['kind']} {d['metadata']['name']} ← JT #{d['metadata']['annotations']['awx.io/job-template-id']}")

    out = Path(__file__).resolve().parents[1] / "data" / "generated-catalog.yaml"
    out.write_text(render_catalog_yaml(docs), encoding="utf-8")
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()

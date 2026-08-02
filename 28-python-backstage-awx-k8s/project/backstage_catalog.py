"""Sinh Backstage Catalog entities từ AWX job templates."""
from __future__ import annotations

from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore


def template_to_resource(
    template: dict[str, Any],
    *,
    org: str = "default",
    system: str = "platform",
) -> dict[str, Any]:
    """Map 1 AWX Job Template → Backstage Resource entity."""
    tid = template["id"]
    name = str(template.get("name", f"template-{tid}")).lower().replace(" ", "-")
    return {
        "apiVersion": "backstage.io/v1alpha1",
        "kind": "Resource",
        "metadata": {
            "name": f"awx-jt-{name}"[:63],
            "title": template.get("name"),
            "description": template.get("description") or f"AWX job template #{tid}",
            "annotations": {
                "awx.io/job-template-id": str(tid),
                "awx.io/playbook": str(template.get("playbook", "")),
                "backstage.io/managed-by-location": "url:python-bridge",
            },
            "tags": ["awx", "automation", "ansible"],
        },
        "spec": {
            "type": "awx-job-template",
            "owner": f"group:{org}/platform-team",
            "system": f"system:{org}/{system}",
        },
    }


def build_catalog_documents(
    templates: list[dict[str, Any]],
    *,
    org: str = "default",
    system: str = "platform",
) -> list[dict[str, Any]]:
    return [template_to_resource(t, org=org, system=system) for t in templates]


def render_catalog_yaml(documents: list[dict[str, Any]]) -> str:
    if yaml is None:
        raise ImportError("pip install pyyaml")
    return yaml.safe_dump_all(documents, sort_keys=False, allow_unicode=True)


def validate_catalog_entity(entity: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("apiVersion", "kind", "metadata", "spec"):
        if key not in entity:
            errors.append(f"missing {key}")
    meta = entity.get("metadata") or {}
    if not meta.get("name"):
        errors.append("metadata.name required")
    return errors

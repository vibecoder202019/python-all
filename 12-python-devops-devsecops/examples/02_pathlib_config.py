"""
Module 12 — Ví dụ 2: pathlib và Config (YAML/JSON)

Chạy: python examples/02_pathlib_config.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Đọc config YAML từ data/config.yaml (app name, services).
  2. Quét thư mục examples/ — liệt kê file .py kèm size.
  3. Ghi kết quả quét ra data/scan_result.json.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - "Config loaded: ... (env=...)" và danh sách services.
  - Top 5 file .py với path và size KB.
  - "Saved: .../data/scan_result.json" và "✓ Done".
═══════════════════════════════════════════════════════════════════════════
"""
import json
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

MODULE_DIR = Path(__file__).parent.parent
DATA_DIR = MODULE_DIR / "data"


def load_config(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        if yaml is None:
            raise ImportError("pip install pyyaml")
        return yaml.safe_load(content)
    return json.loads(content)


def scan_directory(path: Path, pattern: str = "*") -> list[dict]:
    results = []
    for p in path.rglob(pattern):
        if p.is_file():
            results.append({
                "path": str(p.relative_to(path)),
                "size_kb": round(p.stat().st_size / 1024, 2),
                "modified": p.stat().st_mtime,
            })
    return sorted(results, key=lambda x: x["size_kb"], reverse=True)


print("=== pathlib & Config Management ===\n")

config_path = DATA_DIR / "config.yaml"
if config_path.exists():
    config = load_config(config_path)
    print(f"1. Config loaded: {config['app']['name']} (env={config['app']['env']})")
    print(f"   Services: {[s['name'] for s in config['services']]}")
else:
    print("1. Chạy bash scripts/setup.sh để tạo sample data")

print("\n2. Scan thư mục examples/:")
files = scan_directory(MODULE_DIR / "examples", "*.py")
for f in files[:5]:
    print(f"   {f['path']:40s} {f['size_kb']:6.1f} KB")

print("\n3. Tạo output JSON:")
output = {"scanned_files": len(files), "top_files": files[:3]}
out_path = DATA_DIR / "scan_result.json"
DATA_DIR.mkdir(exist_ok=True)
out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
print(f"   Saved: {out_path}")

print("\n✓ Done")

"""Đáp án Module 12 — Backup script"""
import shutil
from datetime import datetime
from pathlib import Path


def backup_directory(src: str, dest_base: str = "backup") -> Path:
    src_path = Path(src)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = Path(dest_base) / f"{src_path.name}_{timestamp}"
    shutil.copytree(src_path, dest)
    return dest


if __name__ == "__main__":
    module_dir = Path(__file__).parent.parent.parent
    data_dir = module_dir / "data"
    if data_dir.exists():
        result = backup_directory(str(data_dir), str(module_dir / "backup"))
        print(f"Backup created: {result}")

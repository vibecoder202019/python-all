"""
Module 12 — Đáp án bài tập: Backup thư mục
Chạy: python exercises/solutions/solutions.py

YÊU CẦU ĐỀ BÀI:
  - Viết hàm backup_directory(src, dest_base) copy cả thư mục
  - Tên backup có timestamp để không ghi đè
  - Dùng pathlib và shutil.copytree

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Nếu thư mục data/ tồn tại → in "Backup created: backup/data_YYYYMMDD_HHMMSS"
  - Thư mục backup mới chứa bản sao đầy đủ của data/
"""
import shutil
from datetime import datetime
from pathlib import Path


def backup_directory(src: str, dest_base: str = "backup") -> Path:
    """Copy cả thư mục src vào dest_base/<tên>_<timestamp>."""
    src_path = Path(src)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = Path(dest_base) / f"{src_path.name}_{timestamp}"
    shutil.copytree(src_path, dest)  # copy đệ quy toàn bộ file/thư mục con
    return dest


if __name__ == "__main__":
    module_dir = Path(__file__).parent.parent.parent
    data_dir = module_dir / "data"
    if data_dir.exists():
        result = backup_directory(str(data_dir), str(module_dir / "backup"))
        print(f"Backup created: {result}")

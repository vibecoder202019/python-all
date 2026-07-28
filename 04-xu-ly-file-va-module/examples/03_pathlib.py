"""
Module 04 — Ví dụ 3: pathlib
Chạy: python examples/03_pathlib.py

YÊU CẦU ĐỀ BÀI:
  - Tạo thư mục và file bằng Path.mkdir(), write_text()
  - Đọc file, tính thống kê (count, sum, average, max, min)
  - Ghi kết quả ra file output
  - Duyệt cây thư mục với rglob("*")

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Tạo data/input/numbers.txt (1-10)
  - Ghi data/output/stats.txt với 5 chỉ số thống kê
  - Liệt kê tất cả file trong data/ kèm kích thước
"""
from pathlib import Path


def demo_pathlib():
    base = Path(__file__).parent / "data"
    base.mkdir(exist_ok=True)

    # ── Tạo cấu trúc thư mục ──
    (base / "input").mkdir(exist_ok=True)
    (base / "output").mkdir(exist_ok=True)

    input_file = base / "input" / "numbers.txt"
    input_file.write_text("\n".join(str(i) for i in range(1, 11)), encoding="utf-8")

    numbers = [int(line) for line in input_file.read_text().splitlines()]
    result = {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
    }

    output_file = base / "output" / "stats.txt"
    output_file.write_text(
        "\n".join(f"{k}: {v}" for k, v in result.items()),
        encoding="utf-8",
    )

    print("=== pathlib demo ===")
    print(f"Input:  {input_file} ({input_file.stat().st_size} bytes)")
    print(f"Output: {output_file}")
    print(output_file.read_text())

    print("=== Files in data/ ===")
    for p in base.rglob("*"):  # duyệt đệ quy mọi file/thư mục
        if p.is_file():
            print(f"  {p.relative_to(base)} ({p.stat().st_size} bytes)")


# ── Demo ──
if __name__ == "__main__":
    demo_pathlib()

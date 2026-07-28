"""Module 04 — File I/O"""
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def demo_text_file():
    filepath = DATA_DIR / "sample.txt"
    lines = ["Python là ngôn ngữ tuyệt vời", "Học ML với Python", "FastAPI cho API"]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"=== Đọc file: {filepath.name} ===")
    with open(filepath, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            print(f"  {i}. {line.strip()}")

    content = filepath.read_text(encoding="utf-8")
    print(f"Tổng ký tự: {len(content)}")


def demo_append():
    log_file = DATA_DIR / "app.log"
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Application started\n")
        f.write(f"[{timestamp}] Processing data...\n")
        f.write(f"[{timestamp}] Done\n")

    print(f"\n=== Log file ===")
    print(log_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    demo_text_file()
    demo_append()

"""
Module 05 — Ví dụ 3: Logging
Chạy: python examples/03_logging.py

YÊU CẦU ĐỀ BÀI:
  - Cấu hình logger với FileHandler (ghi file) và StreamHandler (in console)
  - Ghi log ở các mức: DEBUG, INFO, WARNING, ERROR
  - Dùng logger.exception để ghi traceback khi có exception

KẾT QUẢ MONG ĐỢI (khi chạy):
  - In các dòng log ra console (mức INFO trở lên)
  - Ghi đầy đủ log (kể cả DEBUG) vào file logs/ml_app.log
  - In đường dẫn file log đã lưu
"""

import logging
from pathlib import Path

# ── Cấu hình thư mục log ──
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """Tạo logger với handler ghi file và in console."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # logger nhận tất cả mức log

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # ── Handler ghi file — lưu mọi mức log ──
    fh = logging.FileHandler(LOG_DIR / log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # ── Handler console — chỉ hiện INFO trở lên ──
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


def demo_logging():
    """Demo các mức log và ghi exception."""
    logger = setup_logger("ml_app", "ml_app.log")

    logger.debug("Debug: loading config")
    logger.info("Info: Model training started")
    logger.warning("Warning: Dataset has 5% missing values")
    logger.error("Error: Failed to connect to database")

    # ── Ghi traceback khi có exception ──
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.exception("Exception caught:")

    print(f"\nLog file saved to: {LOG_DIR / 'ml_app.log'}")


if __name__ == "__main__":
    demo_logging()

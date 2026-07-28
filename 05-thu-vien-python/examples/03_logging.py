"""Module 05 — logging"""
import logging
from pathlib import Path

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


def setup_logger(name: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    fh = logging.FileHandler(LOG_DIR / log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


def demo_logging():
    logger = setup_logger("ml_app", "ml_app.log")

    logger.debug("Debug: loading config")
    logger.info("Info: Model training started")
    logger.warning("Warning: Dataset has 5% missing values")
    logger.error("Error: Failed to connect to database")

    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.exception("Exception caught:")

    print(f"\nLog file saved to: {LOG_DIR / 'ml_app.log'}")


if __name__ == "__main__":
    demo_logging()

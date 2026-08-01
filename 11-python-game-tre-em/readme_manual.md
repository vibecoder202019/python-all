# Hướng dẫn chạy Manual — Module 11: Game Pygame

> Lệnh trích từ `scripts/setup.sh`, `run_all_examples.sh`, `run_project.sh`.

## Phần 0 — Kiểm tra

```bash
python3 --version
python3 -c "import sys; print(sys.platform)"
```

## Phần A — Cài đặt (`scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pygame
```

**Kiểm tra sau cài đặt:**

```bash
python -c "import pygame; print(pygame.ver)"
```

## Phần B — Ví dụ (`scripts/run_all_examples.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 11-python-game-tre-em/examples/01_cua_so_va_mau.py
python 11-python-game-tre-em/examples/02_hinh_va_text.py
python 11-python-game-tre-em/examples/03_ban_phim_chuot.py
python 11-python-game-tre-em/examples/04_sprite_va_anh.py
python 11-python-game-tre-em/examples/05_va_cham_diem.py
python 11-python-game-tre-em/examples/06_game_snake.py
```

**Kiểm tra:** Mỗi game mở cửa sổ; ESC để thoát.

## Phần C — Dự án (`scripts/run_project.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 11-python-game-tre-em/project/step01_window.py
python 11-python-game-tre-em/project/step02_player.py
python 11-python-game-tre-em/project/step03_stars.py
python 11-python-game-tre-em/project/step04_collision.py
python 11-python-game-tre-em/project/step05_score_lives.py
python 11-python-game-tre-em/project/step06_final.py
```

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `run_all_examples.sh` | B |
| `run_project.sh` | C |

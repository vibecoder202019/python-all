# Hướng dẫn chạy Manual — Module 11: Game cho trẻ em

> Copy từng lệnh và chạy **tuần tự**. Mỗi nhóm bước tương ứng một script trong `scripts/`.

## Điều kiện

- Python 3.10+
- macOS/Linux (Pygame cần display)

---

## Phần A — Setup (tương ứng `scripts/setup.sh`)

### Bước A1: Tạo venv ở root repo

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
```

### Bước A2: Cài Pygame

```bash
pip install --upgrade pip
pip install pygame
```

### Bước A3: Kiểm tra Pygame

```bash
python -c "import pygame; print(pygame.ver)"
```

---

## Phần B — Chạy tất cả ví dụ (tương ứng `scripts/run_all_examples.sh`)

```bash
cd learn-python-ai/11-python-game-tre-em
source ../.venv/bin/activate
```

```bash
python examples/01_cua_so_va_mau.py
```

```bash
python examples/02_hinh_va_text.py
```

```bash
python examples/03_ban_phim_chuot.py
```

```bash
python examples/04_sprite_va_anh.py
```

```bash
python examples/05_va_cham_diem.py
```

```bash
python examples/06_game_snake.py
```

**Lưu ý:** Nhấn ESC hoặc đóng cửa sổ để thoát mỗi game.

---

## Phần C — Dự án Catch the Stars (tương ứng `scripts/run_project.sh`)

```bash
cd learn-python-ai/11-python-game-tre-em
source ../.venv/bin/activate
python project/step01_window.py
python project/step02_player.py
python project/step03_stars.py
python project/step04_collision.py
python project/step05_score_lives.py
python project/step06_final.py
```

---

## Bản đồ script ↔ manual

| Script | Phần manual |
|--------|-------------|
| `scripts/setup.sh` | Phần A (A1–A3) |
| `scripts/run_all_examples.sh` | Phần B (6 lệnh python) |
| `scripts/run_project.sh` | Phần C (step01→step06) |

## Gỡ / dọn dẹp

Không cần — không tạo container hay cloud resource.

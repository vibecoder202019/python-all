# Module 11: Làm Game cho Trẻ em với Python

Học lập trình game bằng **Pygame** — từ vẽ hình cơ bản đến game hoàn chỉnh có điểm số, âm thanh và nhiều level.

## Mục tiêu

- Hiểu game loop: input → update → render
- Vẽ hình, xử lý bàn phím/chuột
- Sprite, va chạm (collision), điểm số
- Hoàn thành game **"Bắt Sao" (Catch the Stars)** qua 6 bước tuần tự

## Yêu cầu

- Python 3.10+
- Pygame (`pip install pygame`)
- Màn hình (game cần cửa sổ đồ họa)

---

## Chạy nhanh (1 lệnh)

```bash
# Cài môi trường + chạy TẤT CẢ ví dụ lần lượt
bash scripts/setup.sh
bash scripts/run_all_examples.sh

# Chạy dự án game hoàn chỉnh (6 bước ghép lại)
bash scripts/run_project.sh
```

---

## Lộ trình trong module

| Bước | File | Nội dung | Level |
|------|------|----------|-------|
| 01 | `examples/01_cua_so_va_mau.py` | Cửa sổ, màu sắc, game loop | Cơ bản |
| 02 | `examples/02_hinh_va_text.py` | Vẽ hình, hiển thị chữ | Cơ bản |
| 03 | `examples/03_ban_phim_chuot.py` | Di chuyển nhân vật | Cơ bản |
| 04 | `examples/04_sprite_va_anh.py` | Sprite, animation đơn giản | Trung bình |
| 05 | `examples/05_va_cham_diem.py` | Collision, ghi điểm | Trung bình |
| 06 | `examples/06_game_snake.py` | Game Rắn săn mồi | Nâng cao |
| 🎯 | `project/` | Game **Catch the Stars** (6 step) | Dự án |

---

## Game Loop — Khái niệm cốt lõi

```
┌─────────────────────────────────────┐
│           GAME LOOP (60 FPS)        │
│                                     │
│  1. Xử lý input (phím, chuột)       │
│  2. Cập nhật logic (di chuyển...)   │
│  3. Vẽ lên màn hình (render)        │
│  4. Lặp lại                         │
└─────────────────────────────────────┘
```

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update logic ở đây
    screen.fill((30, 30, 60))
    # Draw ở đây
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
```

---

## Dự án tuần tự: Catch the Stars

Game cho trẻ em — điều khiển phi hành gia bắt sao rơi, tránh đá.

```
project/
├── step01_window.py      # Cửa sổ + nền trời
├── step02_player.py      # Thêm nhân vật
├── step03_stars.py       # Sao rơi ngẫu nhiên
├── step04_collision.py   # Bắt sao + hiệu ứng
├── step05_score_lives.py # Điểm, mạng, game over
└── step06_final.py       # Menu, level, hoàn chỉnh
```

Chạy từng bước:
```bash
python project/step01_window.py
python project/step02_player.py
# ... đến step06_final.py
```

Hoặc chạy tất cả tuần tự:
```bash
bash scripts/run_project.sh
```

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 12: Python DevOps & DevSecOps](../12-python-devops-devsecops/README.md)

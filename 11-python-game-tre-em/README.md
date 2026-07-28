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

## Lý thuyết nền tảng — Lập trình game là gì?

Game = **vòng lặp liên tục** cập nhật và vẽ hình 60 lần/giây (60 FPS).

```
┌──────────────────────────────────────┐
│  while game_running:                 │
│    1. Đọc input (phím, chuột)        │
│    2. Cập nhật logic (di chuyển...)  │
│    3. Vẽ frame mới lên màn hình      │
│    4. Chờ 16ms (60 FPS)              │
└──────────────────────────────────────┘
```

### Pygame — thư viện game 2D cho Python

Pygame wrap **SDL** (Simple DirectMedia Layer) — thư viện C đa nền tảng cho đồ họa 2D.

**Phù hợp cho:** game giáo dục, prototype, game đơn giản cho trẻ em  
**Không phù hợp:** game 3D AAA — cần Unity/Unreal/Godot

### Toạ độ màn hình

```
(0,0) ──────────────► X (800)
  │
  │    (400, 300) = giữa màn hình
  │
  ▼
  Y (600)
```

- Góc trên-trái = `(0, 0)`
- `y` **tăng xuống dưới** (khác toán học!)

### Collision — va chạm

```python
player.colliderect(star)  # True nếu 2 hình chữ nhật chồng nhau
```

Đơn giản, nhanh — đủ cho game 2D học tập. Game phức tạp dùng polygon collision.

### State machine — quản lý trạng thái game

```
menu  ──SPACE──►  playing  ──hết mạng──►  gameover  ──R──►  playing
  ▲                                          │
  └──────────────── ESC ─────────────────────┘
```

Mỗi state vẽ và xử lý input khác nhau — pattern cơ bản mọi game đều dùng.

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

---

## Giải thích chi tiết (Tự học)

### Script `scripts/setup.sh` — từng dòng

```bash
set -euo pipefail
```
| Flag | Ý nghĩa |
|------|---------|
| `-e` | Dừng ngay nếu lệnh lỗi |
| `-u` | Lỗi nếu dùng biến chưa khai báo |
| `-o pipefail` | Pipeline fail nếu bất kỳ lệnh nào fail |

```bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
```
- Lấy đường dẫn tuyệt đối thư mục chứa script — chạy được từ bất kỳ đâu

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -q pygame
```
- `venv` — môi trường Python cô lập
- `source .venv/bin/activate` — kích hoạt venv cho session terminal hiện tại

---

### Game Loop — giải thích code

```python
running = True
while running:
    for event in pygame.event.get():      # 1. INPUT
        if event.type == pygame.QUIT:
            running = False
    # 2. UPDATE — di chuyển, va chạm, ghi điểm
    screen.fill(SKY)                       # 3. RENDER — xóa frame cũ
    pygame.draw.rect(screen, COLOR, player)
    pygame.display.flip()                # Hiện frame mới
    clock.tick(60)                         # Giới hạn 60 FPS
```

- **`clock.tick(60)`** — chờ đủ ~16ms/frame → game chạy mượt, không quá nhanh
- **`pygame.display.flip()`** — double buffering: vẽ xong mới hiện lên màn hình

---

### Dự án Catch the Stars — từng bước

| Step | Code thêm vào | Học được |
|------|---------------|----------|
| `step01_window` | `screen.fill()`, `clock.tick()` | Cửa sổ + game loop |
| `step02_player` | `keys = pygame.key.get_pressed()` | Input liên tục |
| `step03_stars` | `random`, list sao/đá rơi | Spawn object ngẫu nhiên |
| `step04_collision` | `player.colliderect(star)` | Va chạm hình chữ nhật |
| `step05_score_lives` | `lives -= 1`, `game_over` | Game state |
| `step06_final` | `state = "menu"/"playing"` | State machine |

```python
if player.colliderect(star):
    score += 10
    stars.remove(star)
```
- `colliderect` — True nếu 2 hình chữ nhật chồng nhau
- Xóa sao khỏi list sau khi bắt — tránh bắt lại nhiều lần

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.x -= speed
```
- `get_pressed()` — trạng thái phím **đang giữ** (mượt hơn event KEYDOWN)

---

### Script `run_project.sh`

```bash
for step in "${STEPS[@]}"; do
  python "$MODULE_DIR/project/$step"
done
```
- Chạy lần lượt 6 file Python — mỗi bước build trên bước trước
- Game cuối (`step06_final.py`) chạy liên tục đến khi đóng cửa sổ

---

## Câu hỏi thường gặp (FAQ)

**Q: Pygame cài lỗi trên macOS?**  
A: Thử `pip install pygame` trong venv. macOS M1+: cần Python native ARM.

**Q: Game chạy quá nhanh/chậm?**  
A: Dùng `clock.tick(60)` — số càng lớn càng nhanh (FPS).

**Q: Làm sao thoát game?**  
A: ESC, đóng cửa sổ, hoặc `pygame.QUIT` event.

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module tiếp theo

→ [Module 12: Python DevOps & DevSecOps](../12-python-devops-devsecops/README.md)

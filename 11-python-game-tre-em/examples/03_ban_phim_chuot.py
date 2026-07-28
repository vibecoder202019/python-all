"""
Module 11 — Ví dụ 3: Điều khiển bằng bàn phím và chuột

Chạy: python examples/03_ban_phim_chuot.py
Mũi tên / WASD di chuyển — Click chuột đặt cờ

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Di chuyển nhân vật (hình tròn vàng) bằng phím mũi tên hoặc WASD.
  2. Giới hạn nhân vật trong biên cửa sổ.
  3. Click chuột trái đặt cờ đỏ tại vị trí click.

KẾT QUẢ MONG ĐỢI (trên màn hình):
  - Nhân vật di chuyển mượt, không ra ngoài màn hình.
  - Mỗi click tạo thêm một chấm đỏ (cờ).
  - Thanh gợi ý điều khiển ở dưới cùng.
═══════════════════════════════════════════════════════════════════════════
"""
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Module 11 — Bước 3: Bàn phím & Chuột")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)

player_x, player_y = WIDTH // 2, HEIGHT // 2
player_size = 40
speed = 5
flags: list[tuple[int, int]] = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flags.append(event.pos)

    # Đọc trạng thái phím liên tục (giữ phím = di chuyển liên tục)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x = max(player_size, player_x - speed)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x = min(WIDTH - player_size, player_x + speed)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y = max(player_size, player_y - speed)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y = min(HEIGHT - player_size, player_y + speed)

    screen.fill((200, 230, 255))
    pygame.draw.circle(screen, (255, 180, 0), (player_x, player_y), player_size)
    pygame.draw.circle(screen, (255, 255, 255), (player_x - 10, player_y - 8), 10)
    pygame.draw.circle(screen, (255, 255, 255), (player_x + 10, player_y - 8), 10)
    pygame.draw.circle(screen, (30, 30, 30), (player_x - 10, player_y - 8), 4)
    pygame.draw.circle(screen, (30, 30, 30), (player_x + 10, player_y - 8), 4)

    for fx, fy in flags:
        pygame.draw.circle(screen, (255, 50, 50), (fx, fy), 8)

    hint = font.render("Mũi tên/WASD di chuyển | Click đặt cờ | ESC thoát", True, (50, 50, 50))
    screen.blit(hint, (20, HEIGHT - 35))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

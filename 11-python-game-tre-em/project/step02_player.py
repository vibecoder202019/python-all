"""
Module 11 — Dự án Bước 2: Thêm nhân vật phi hành gia

Chạy: python project/step02_player.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Vẽ nhân vật (hình chữ nhật bo góc) ở gần đáy màn hình.
  2. Di chuyển trái/phải bằng phím mũi tên, giới hạn trong biên cửa sổ.
  3. Dùng PLAYER_W, PLAYER_H, PLAYER_COLOR từ common.py.

KẾT QUẢ MONG ĐỢI (trên màn hình):
  - Nhân vật xanh nhạt di chuyển mượt trên nền trời + cỏ.
  - Không thể di chuyển ra ngoài mép trái/phải.
═══════════════════════════════════════════════════════════════════════════
"""
import pygame
import sys
from common import WIDTH, HEIGHT, FPS, SKY, GRASS, PLAYER_COLOR, PLAYER_W, PLAYER_H

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Stars — Bước 2")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)

player = pygame.Rect(WIDTH // 2 - PLAYER_W // 2, HEIGHT - 100, PLAYER_W, PLAYER_H)
speed = 7

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x = max(0, player.x - speed)
    if keys[pygame.K_RIGHT]:
        player.x = min(WIDTH - PLAYER_W, player.x + speed)

    screen.fill(SKY)
    pygame.draw.rect(screen, GRASS, (0, HEIGHT - 80, WIDTH, 80))
    pygame.draw.rect(screen, PLAYER_COLOR, player, border_radius=10)
    pygame.draw.circle(screen, (255, 255, 255), (player.centerx, player.top + 15), 12)

    hint = font.render("← → di chuyển phi hành gia", True, (255, 255, 255))
    screen.blit(hint, (20, 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

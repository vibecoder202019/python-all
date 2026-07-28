"""
Module 11 — Dự án Bước 3: Sao và đá rơi

Chạy: python project/step03_stars.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Spawn sao vàng (75%) và đá xám (25%) rơi từ trên xuống.
  2. Nhân vật vẫn di chuyển trái/phải như bước 2.
  3. Xóa vật thể khi rơi ra khỏi màn hình.

KẾT QUẢ MONG ĐỢI (trên màn hình):
  - Sao tròn vàng và đá vuông xám rơi liên tục.
  - Chữ "Bước 3: Sao vàng (+) / Đá xám (-) đang rơi!" góc trên trái.
  - Chưa có va chạm/điểm (thêm ở bước 4).
═══════════════════════════════════════════════════════════════════════════
"""
import random
import pygame
import sys
from common import WIDTH, HEIGHT, FPS, SKY, GRASS, PLAYER_COLOR, PLAYER_W, PLAYER_H, STAR_COLOR, ROCK_COLOR, STAR_SIZE, ROCK_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Stars — Bước 3")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)

player = pygame.Rect(WIDTH // 2 - PLAYER_W // 2, HEIGHT - 100, PLAYER_W, PLAYER_H)
stars: list[pygame.Rect] = []
rocks: list[pygame.Rect] = []
spawn_timer = 0
speed = 7

running = True
while running:
    spawn_timer += 1
    if spawn_timer > 35:
        spawn_timer = 0
        if random.random() < 0.75:
            stars.append(pygame.Rect(random.randint(0, WIDTH - STAR_SIZE), -STAR_SIZE, STAR_SIZE, STAR_SIZE))
        else:
            rocks.append(pygame.Rect(random.randint(0, WIDTH - ROCK_SIZE), -ROCK_SIZE, ROCK_SIZE, ROCK_SIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x = max(0, player.x - speed)
    if keys[pygame.K_RIGHT]:
        player.x = min(WIDTH - PLAYER_W, player.x + speed)

    for star in stars:
        star.y += 4
    for rock in rocks:
        rock.y += 5
    stars = [s for s in stars if s.top < HEIGHT]
    rocks = [r for r in rocks if r.top < HEIGHT]

    screen.fill(SKY)
    pygame.draw.rect(screen, GRASS, (0, HEIGHT - 80, WIDTH, 80))
    pygame.draw.rect(screen, PLAYER_COLOR, player, border_radius=10)
    for star in stars:
        pygame.draw.circle(screen, STAR_COLOR, star.center, STAR_SIZE // 2)
    for rock in rocks:
        pygame.draw.rect(screen, ROCK_COLOR, rock, border_radius=5)

    screen.blit(font.render("Bước 3: Sao vàng (+) / Đá xám (-) đang rơi!", True, (255, 255, 255)), (20, 20))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

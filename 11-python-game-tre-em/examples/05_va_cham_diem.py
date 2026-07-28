"""
Module 11 — Ví dụ 5: Va chạm và ghi điểm

Chạy: python examples/05_va_cham_diem.py
Di chuyển nhân vật bắt sao vàng (+10 điểm), tránh đá xám (-1 mạng)

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Nhân vật di chuyển trái/phải; sao và đá rơi từ trên xuống.
  2. Va chạm sao: +10 điểm; va chạm đá: -1 mạng.
  3. Game Over khi hết mạng; hiển thị điểm cuối 2 giây.

KẾT QUẢ MONG ĐỢI (trên màn hình):
  - HUD hiển thị "Điểm: N" và "Mạng: ❤️❤️❤️".
  - Bắt sao → điểm tăng 10; chạm đá → mất 1 tim.
  - Hết mạng → màn hình đỏ "Game Over! Điểm: N".
═══════════════════════════════════════════════════════════════════════════
"""
import random
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Module 11 — Bước 5: Va chạm & Điểm")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24, bold=True)

player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 80, 50, 50)
stars: list[pygame.Rect] = []
rocks: list[pygame.Rect] = []
score = 0
lives = 3
spawn_timer = 0

running = True
while running and lives > 0:
    # Spawn sao/đá mỗi 40 frame (~0.67 giây ở 60 FPS)
    spawn_timer += 1
    if spawn_timer > 40:
        spawn_timer = 0
        if random.random() < 0.7:
            stars.append(pygame.Rect(random.randint(20, WIDTH - 30), -30, 25, 25))
        else:
            rocks.append(pygame.Rect(random.randint(20, WIDTH - 30), -30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x = max(0, player.x - 6)
    if keys[pygame.K_RIGHT]:
        player.x = min(WIDTH - 50, player.x + 6)

    for star in stars[:]:
        star.y += 4
        if player.colliderect(star):
            score += 10
            stars.remove(star)
        elif star.top > HEIGHT:
            stars.remove(star)

    for rock in rocks[:]:
        rock.y += 5
        if player.colliderect(rock):
            lives -= 1
            rocks.remove(rock)
        elif rock.top > HEIGHT:
            rocks.remove(rock)

    screen.fill((30, 30, 80))
    pygame.draw.rect(screen, (100, 200, 255), player, border_radius=8)
    for star in stars:
        pygame.draw.circle(screen, (255, 220, 0), star.center, 12)
    for rock in rocks:
        pygame.draw.rect(screen, (120, 120, 120), rock, border_radius=5)

    screen.blit(font.render(f"Điểm: {score}", True, (255, 255, 255)), (20, 20))
    screen.blit(font.render(f"Mạng: {'❤️' * lives}", True, (255, 100, 100)), (20, 50))

    pygame.display.flip()
    clock.tick(60)

if lives <= 0:
    screen.fill((50, 0, 0))
    msg = font.render(f"Game Over! Điểm: {score}", True, (255, 255, 255))
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

pygame.quit()
sys.exit()

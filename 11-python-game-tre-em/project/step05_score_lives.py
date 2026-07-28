"""
Dự án Bước 5 — Điểm số, mạng, Game Over
Chạy: python project/step05_score_lives.py
"""
import random
import pygame
import sys
from common import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Stars — Bước 5")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22, bold=True)
big_font = pygame.font.SysFont("Arial", 48, bold=True)

player = pygame.Rect(WIDTH // 2 - PLAYER_W // 2, HEIGHT - 100, PLAYER_W, PLAYER_H)
stars: list[pygame.Rect] = []
rocks: list[pygame.Rect] = []
score = 0
lives = 3
level = 1
spawn_timer = 0
speed = 7
game_over = False

running = True
while running:
    if not game_over:
        spawn_timer += 1
        interval = max(15, 40 - level * 3)
        if spawn_timer > interval:
            spawn_timer = 0
            if random.random() < 0.75:
                stars.append(pygame.Rect(random.randint(0, WIDTH - STAR_SIZE), -STAR_SIZE, STAR_SIZE, STAR_SIZE))
            else:
                rocks.append(pygame.Rect(random.randint(0, WIDTH - ROCK_SIZE), -ROCK_SIZE, ROCK_SIZE, ROCK_SIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            score, lives, level, game_over = 0, 3, 1, False
            stars, rocks = [], []

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x = max(0, player.x - speed)
        if keys[pygame.K_RIGHT]:
            player.x = min(WIDTH - PLAYER_W, player.x + speed)

        for star in stars[:]:
            star.y += 3 + level
            if player.colliderect(star):
                score += 10
                if score > 0 and score % 50 == 0:
                    level += 1
                stars.remove(star)
            elif star.top > HEIGHT:
                stars.remove(star)

        for rock in rocks[:]:
            rock.y += 4 + level
            if player.colliderect(rock):
                lives -= 1
                rocks.remove(rock)
                if lives <= 0:
                    game_over = True
            elif rock.top > HEIGHT:
                rocks.remove(rock)

    screen.fill(SKY)
    pygame.draw.rect(screen, GRASS, (0, HEIGHT - 80, WIDTH, 80))
    pygame.draw.rect(screen, PLAYER_COLOR, player, border_radius=10)
    for star in stars:
        pygame.draw.circle(screen, STAR_COLOR, star.center, STAR_SIZE // 2)
    for rock in rocks:
        pygame.draw.rect(screen, ROCK_COLOR, rock, border_radius=5)

    screen.blit(font.render(f"Điểm: {score}  Level: {level}", True, (255, 255, 255)), (20, 20))
    screen.blit(font.render(f"Mạng: {'❤️' * lives}", True, (255, 100, 100)), (20, 50))

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        msg = big_font.render("Game Over!", True, (255, 100, 100))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 60))
        sub = font.render(f"Điểm: {score} — Nhấn R chơi lại", True, (255, 255, 255))
        screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2 + 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

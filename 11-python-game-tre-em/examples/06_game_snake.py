"""
Bước 06 — Game Rắn săn mồi (Snake) — Nâng cao
Chạy: python examples/06_game_snake.py
Mũi tên điều khiển — Ăn táo đỏ (+1), đừng cắn đuôi!
"""
import random
import pygame
import sys

pygame.init()

CELL = 25
COLS, ROWS = 24, 20
WIDTH, HEIGHT = COLS * CELL, ROWS * CELL + 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Module 11 — Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22, bold=True)

snake = [(COLS // 2, ROWS // 2)]
direction = (1, 0)
food = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
score = 0
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    if not game_over:
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if head[0] < 0 or head[0] >= COLS or head[1] < 0 or head[1] >= ROWS or head in snake:
            game_over = True
        else:
            snake.insert(0, head)
            if head == food:
                score += 1
                food = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
                while food in snake:
                    food = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            else:
                snake.pop()

    screen.fill((20, 40, 20))
    for x, y in snake:
        pygame.draw.rect(screen, (50, 200, 50), (x * CELL, y * CELL, CELL - 1, CELL - 1), border_radius=4)
    pygame.draw.rect(screen, (255, 50, 50), (food[0] * CELL, food[1] * CELL, CELL - 1, CELL - 1), border_radius=4)

    pygame.draw.rect(screen, (30, 30, 30), (0, ROWS * CELL, WIDTH, 50))
    screen.blit(font.render(f"Điểm: {score}", True, (255, 255, 255)), (20, ROWS * CELL + 12))
    if game_over:
        msg = font.render("Game Over! ESC thoát", True, (255, 100, 100))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, ROWS * CELL + 12))

    pygame.display.flip()
    clock.tick(10 if not game_over else 30)

pygame.quit()
sys.exit()

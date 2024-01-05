import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up paddles and ball
paddle_width, paddle_height = 20, 100
ball_size = 20

player1 = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)

ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
ball_speed = [random.choice([-1, 1]) * 7, random.choice([-1, 1]) * 7]

# Set up game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # Player 1 controls
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= 5
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += 5

    # Player 2 controls
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= 5
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += 5

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] = -ball_speed[0]

    # Draw everything on the screen
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, player1)
    pygame.draw.rect(win, WHITE, player2)
    pygame.draw.ellipse(win, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

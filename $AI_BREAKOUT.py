# PyPong - Breakout Game

# Importing necessary Pygame modules
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('PyPong - Breakout Game')

# Paddle properties
paddle = pygame.Rect(350, 550, 100, 10)
paddle_speed = 5

# Ball properties
ball = pygame.Rect(390, 300, 10, 10)
ball_speed_x = 3
ball_speed_y = 3

# Bricks
brick_layout = []
for i in range(5):
    for j in range(7):
        brick_layout.append(pygame.Rect(j * 110 + 5, i * 30 + 5, 100, 20))

# Power-ups
power_ups = []

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < 800:
        paddle.move_ip(paddle_speed, 0)

    # Ball movement
    ball.move_ip(ball_speed_x, ball_speed_y)
    if ball.left <= 0 or ball.right >= 800:
        ball_speed_x *= -1
    if ball.top <= 0 or ball.colliderect(paddle):
        ball_speed_y *= -1
    if ball.bottom >= 600:
        # Reset ball
        ball = pygame.Rect(390, 300, 10, 10)
        ball_speed_y *= -1

    # Collision detection with bricks
    for brick in brick_layout:
        if ball.colliderect(brick):
            brick_layout.remove(brick)
            ball_speed_y *= -1
            # Random chance to spawn a power-up
            if random.random() < 0.1:
                power_ups.append(pygame.Rect(brick.x, brick.y, 20, 20))
            break

    # Power-up movement
    for power_up in power_ups:
        power_up.move_ip(0, 2)
        if power_up.colliderect(paddle):
            # Apply power-up effect
            power_ups.remove(power_up)

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in brick_layout:
        pygame.draw.rect(screen, RED, brick)
    for power_up in power_ups:
        pygame.draw.ellipse(screen, GREEN, power_up)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

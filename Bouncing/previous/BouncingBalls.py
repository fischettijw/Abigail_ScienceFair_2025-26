# https://chatgpt.com/share/67c97ac4-ed98-8011-beb0-7f2d693df82a

import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball class
class Ball:
    def __init__(self, x, y, radius, color, speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = random.choice([-1, 1]) * speed
        self.speed_y = random.choice([-1, 1]) * speed

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

def check_collision(ball1, ball2):
    # Check if the balls overlap
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y
    distance = math.sqrt(dx**2 + dy**2)

    return distance < ball1.radius + ball2.radius

def resolve_collision(ball1, ball2):
    # Simple elastic collision resolution
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y
    distance = math.sqrt(dx**2 + dy**2)

    if distance == 0:
        return  # Avoid division by zero

    overlap = ball1.radius + ball2.radius - distance
    if overlap > 0:
        # Push balls apart
        ball1.x += (dx / distance) * (overlap / 2)
        ball1.y += (dy / distance) * (overlap / 2)
        ball2.x -= (dx / distance) * (overlap / 2)
        ball2.y -= (dy / distance) * (overlap / 2)

        # Swap speeds (basic elastic collision handling)
        ball1.speed_x, ball2.speed_x = ball2.speed_x, ball1.speed_x
        ball1.speed_y, ball2.speed_y = ball2.speed_y, ball1.speed_y

# Create balls
NUM_BALLS = 20
balls = []
for _ in range(NUM_BALLS):
    # radius = random.randint(15, 30)
    radius = 10
    x = random.randint(radius, WIDTH - radius)
    y = random.randint(radius, HEIGHT - radius)
    color = [random.randint(50, 255) for _ in range(3)]
    speed = random.uniform(2, 4)

    balls.append(Ball(x, y, radius, color, speed))

balls.append(Ball(WIDTH//2, HEIGHT//2, 10, RED, speed))

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move balls
    for ball in balls:
        ball.move()

    # Check ball collisions
    for i in range(NUM_BALLS):
        for j in range(i + 1, NUM_BALLS):
            if check_collision(balls[i], balls[j]):
                resolve_collision(balls[i], balls[j])

    # Draw everything
    screen.fill(BLACK)
    for ball in balls:
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(15)

pygame.quit()

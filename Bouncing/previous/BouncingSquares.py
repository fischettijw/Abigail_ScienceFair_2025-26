# https://chatgpt.com/share/67c97ac4-ed98-8011-beb0-7f2d693df82a

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Blocks Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Block class
class Block:
    def __init__(self, x, y, size, color, speed):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed_x = random.choice([-1, 1]) * speed
        self.speed_y = random.choice([-1, 1]) * speed

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x <= 0 or self.x + self.size >= WIDTH:
            self.speed_x *= -1
        if self.y <= 0 or self.y + self.size >= HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

def check_collision(block1, block2):
    # Axis-Aligned Bounding Box (AABB) collision detection
    return (
        block1.x < block2.x + block2.size and
        block1.x + block1.size > block2.x and
        block1.y < block2.y + block2.size and
        block1.y + block1.size > block2.y
    )

def resolve_collision(block1, block2):
    # Push blocks apart (basic collision handling)
    overlap_x = min(block1.x + block1.size - block2.x, block2.x + block2.size - block1.x)
    overlap_y = min(block1.y + block1.size - block2.y, block2.y + block2.size - block1.y)

    if overlap_x < overlap_y:
        if block1.x < block2.x:
            block1.x -= overlap_x / 2
            block2.x += overlap_x / 2
        else:
            block1.x += overlap_x / 2
            block2.x -= overlap_x / 2

        # Swap horizontal speeds
        block1.speed_x, block2.speed_x = block2.speed_x, block1.speed_x
    else:
        if block1.y < block2.y:
            block1.y -= overlap_y / 2
            block2.y += overlap_y / 2
        else:
            block1.y += overlap_y / 2
            block2.y -= overlap_y / 2

        # Swap vertical speeds
        block1.speed_y, block2.speed_y = block2.speed_y, block1.speed_y

# Create blocks
NUM_BLOCKS = 40
blocks = []
for _ in range(NUM_BLOCKS):
    # size = random.randint(30, 50)
    size = 20
    x = random.randint(0, WIDTH - size)
    y = random.randint(0, HEIGHT - size)
    color = [random.randint(50, 255) for _ in range(3)]
    # speed = random.uniform(2, 4)
    speed = random.randint(2, 4)
    blocks.append(Block(x, y, size, color, speed))

red_block = blocks.append(Block(WIDTH//2, HEIGHT//2, 10, RED, 1))

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move blocks
    for block in blocks:
        block.move()


    # Check block collisions
    for i in range(NUM_BLOCKS):
        for j in range(i + 1, NUM_BLOCKS):
            if check_collision(blocks[i], blocks[j]):
                resolve_collision(blocks[i], blocks[j])

    # Draw everything
    screen.fill(BLACK)
    for block in blocks:
        block.draw(screen)

    pygame.display.flip()
    clock.tick(15)

pygame.quit()

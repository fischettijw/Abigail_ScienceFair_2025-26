
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Herd Immunity")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

people = []
for person in range(10):
    people.append((random.randint(0, WIDTH), random.randint(0, HEIGHT), 10, 10))


# Main game loop
running = True
while running:
    # Fill screen with a any background color
    screen.fill(YELLOW)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw game objects here (optional)
    for person in people:
        pygame.draw.ellipse(screen, RED, person)




    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
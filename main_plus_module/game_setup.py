import pygame

# Initialize Pygame
pygame.init()

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0, 0, 0)  # Black

# Create game objects
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Game")
clock = pygame.time.Clock()

# Define a list of variables
game_data = {
    "score": 0,
    "lives": 3,
    "level": 1
}

def print_test(a):
    return 2*a

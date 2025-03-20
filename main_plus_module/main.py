# https://chatgpt.com/share/67db1fdb-9e24-8011-b3cb-18fdd3fa738e

import pygame
from game_setup import *
import os; os.system('cls')

print(SCREEN_HEIGHT, SCREEN_WIDTH)
print(game_data["lives"])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Modify game_data (example: increase score)
    game_data["score"] += 1
    abc = 5
    print(print_test(abc), game_data["score"])

    # Rendering
    screen.fill(BG_COLOR)
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

pygame.quit()
print("Final Score:", game_data["score"])

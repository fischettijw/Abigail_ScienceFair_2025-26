import pygame  # Import the pygame library

# Initialize Pygame
pygame.init()

# Set up the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Move the Red Square")

# Colors (RGB format)
BLACK = (0, 0, 0)       # Background color
RED = (255, 0, 0)       # Red square color
YELLOW = (255, 255, 0)  # Yellow square color

# Square size (both red and yellow will be the same size)
SQUARE_SIZE = 50

# Start position for the red square (upper left corner area)
red_x = 100
red_y = 100

# Position the yellow square in the center of the screen
yellow_x = (SCREEN_WIDTH - SQUARE_SIZE) // 2
yellow_y = (SCREEN_HEIGHT - SQUARE_SIZE) // 2

# Speed for moving the red square
SQUARE_SPEED = 5

# Function to check if two squares overlap (touching each other)
def squares_overlap(x1, y1, x2, y2, size):
    if (x1 < x2 + size and          # Red left edge is to the left of yellow right edge
        x1 + size > x2 and          # Red right edge is to the right of yellow left edge
        y1 < y2 + size and          # Red top edge is above yellow bottom edge
        y1 + size > y2):            # Red bottom edge is below yellow top edge
        return True
    else:
        return False

# Main game loop
running = True
clock = pygame.time.Clock()  # Controls how fast the game runs

while running:
    # Check for quit event (close window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys being pressed
    keys = pygame.key.get_pressed()

    # Store the red square's new position based on keys
    new_red_x = red_x
    new_red_y = red_y

    if keys[pygame.K_LEFT]:
        new_red_x -= SQUARE_SPEED
    if keys[pygame.K_RIGHT]:
        new_red_x += SQUARE_SPEED
    if keys[pygame.K_UP]:
        new_red_y -= SQUARE_SPEED
    if keys[pygame.K_DOWN]:
        new_red_y += SQUARE_SPEED

    # Keep the red square inside the screen (don't go off the edges)
    if new_red_x < 0:
        new_red_x = 0
    if new_red_x > SCREEN_WIDTH - SQUARE_SIZE:
        new_red_x = SCREEN_WIDTH - SQUARE_SIZE
    if new_red_y < 0:
        new_red_y = 0
    if new_red_y > SCREEN_HEIGHT - SQUARE_SIZE:
        new_red_y = SCREEN_HEIGHT - SQUARE_SIZE

    # Only update red square's position if it does NOT overlap the yellow square
    if not squares_overlap(new_red_x, new_red_y, yellow_x, yellow_y, SQUARE_SIZE):
        red_x = new_red_x
        red_y = new_red_y

    # Draw everything
    screen.fill(BLACK)  # Clear screen
    pygame.draw.rect(screen, RED, (red_x, red_y, SQUARE_SIZE, SQUARE_SIZE))  # Draw red square
    pygame.draw.rect(screen, YELLOW, (yellow_x, yellow_y, SQUARE_SIZE, SQUARE_SIZE))  # Draw yellow square

    # Update the display
    pygame.display.flip()

    # Control the speed of the loop (frames per second)
    clock.tick(60)

# Quit Pygame when the loop ends
pygame.quit()

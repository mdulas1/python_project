import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the Rectangle")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the rectangle
rect_width = 50
rect_height = 50
rect_x = screen_width // 2 - rect_width // 2
rect_y = screen_height // 2 - rect_height // 2
rect_speed = 5

# Game loop
clock = pygame.time.Clock()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get key states (arrow keys)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Fill the screen with a white color
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
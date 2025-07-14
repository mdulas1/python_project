import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the snake
snake_block = 20
snake_speed = 5
snake_list = []
snake_length = 1

# Set up the initial position of the snake
x1 = screen_width // 2
y1 = screen_height // 2

# Set up the initial direction of the snake
x1_change = 0
y1_change = 0

# Set up the food
foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width // 6, screen_height // 3])

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block

    # Update the position of the snake
    x1 += x1_change
    y1 += y1_change

    # Check for collision with the boundaries
    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        message("You Lost! Press Q-Quit or C-Play Again", RED)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Fill the screen with a white color
    screen.fill(WHITE)

    # Draw the food
    pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block, snake_block])

    # Update the snake's body
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collision with itself
    for x in snake_list[:-1]:
        if x == snake_head:
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

    # Draw the snake
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], snake_block, snake_block])

    # Update the display
    pygame.display.update()

    # Check for collision with the food
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
        foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
        snake_length += 1

    # Cap the frame rate
    clock.tick(snake_speed)
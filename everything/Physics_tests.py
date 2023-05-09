'''

import math

# Define a value for a
a = 0.5

# Compute the sine of a using the sin() function
sine = math.sin(a)
print(f"sin({a}) = {sine}")

# Compute the inverse sine of a using the asin() function
inverse_sine = math.asin(a)
print(f"sin^-1({a}) = {inverse_sine}")
'''

import pygame

# Initialize Pygame
pygame.init()

caption = "Refraction Simulator"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(caption)

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define font and text
font = pygame.font.SysFont("Arial", 72)
text = font.render("Hello, World!", True,  white)

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the screen with black
    screen.fill(black)

    # Draw the text
    screen.blit(text, (800 // 2 - text.get_width() // 2, 600 // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()

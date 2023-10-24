'''
name = input('Quel est votre prénom:')
print('Bonjour', name, 'avez-vous passé une bonne journée ?')

date = input('Quel est votre année de naissance : ')
date = int(date)
print ('Cette année, vous allez avoir', 2023-date,'ans !')


h = input('Donnez moi la hauteur d\'un cylindre en mètres:')
r = input("Donnez moi le rayon d'un cylindre en mètres:")

h = int(h)
r = int(r)

print('Le volume du cylindre est : ')



q = input('Quel est le nom de notre planète ? : ')
if q == ('terre'):
    print('bien.')
    
elif q == ('Terre'):
    
    print('bien. avec la majuscule en plus :)')
else:
    print('tu est nul')



while True:
    n = input('donne moi un nombre entre 1 et 5 : ')
    n = int(n)
    if 1 <= n <= 5:
        print("bien.")
    else:
        print("c'est mal")



while True:
    a = input('donne moi ton age : ')
    a = int(a)
    if  a <= 18:
        print("tu dois grandir !")
    else:
        print("+18ans")

#test



import pygame
import math

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 800
HEIGHT = 400

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Initialize the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Refraction Simulation")

# Laser attributes
laser_length = 400  # Length of the laser beam
laser_x = 0  # Initial x-coordinate of the laser
laser_y = HEIGHT // 2  # Initial y-coordinate of the laser
laser_angle = math.pi / 4  # Initial angle of the laser (45 degrees)

# Square attributes
square_size = 100  # Size of the square
square_x = WIDTH // 2 - square_size // 2  # Initial x-coordinate of the square
square_y = HEIGHT // 2 - square_size // 2  # Initial y-coordinate of the square
refraction_index = 1.5  # Initial refractive index of the square

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(BLACK)

    # Draw the laser beam
    laser_end_x = laser_x + laser_length * math.cos(laser_angle)
    laser_end_y = laser_y - laser_length * math.sin(laser_angle)
    pygame.draw.line(window, RED, (laser_x, laser_y), (laser_end_x, laser_end_y), 2)

    # Draw the transparent square stroke
    pygame.draw.rect(window, WHITE, (square_x, square_y, square_size, square_size), 2)

    # Update the window
    pygame.display.update()

    # Move the square with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= 3
    if keys[pygame.K_RIGHT]:
        square_x += 3
    if keys[pygame.K_UP]:
        square_y -= 3
    if keys[pygame.K_DOWN]:
        square_y += 3

    # Rotate the laser with the mouse movement
    mouse_x, mouse_y = pygame.mouse.get_pos()
    laser_angle = math.atan2(mouse_y - laser_y, mouse_x - laser_x)

    # Handle laser-square collision
    if square_x <= laser_end_x <= square_x + square_size and square_y <= laser_end_y <= square_y + square_size:
        # Calculate the refracted angle
        incident_angle = math.atan2(laser_y - laser_end_y, laser_end_x - laser_x)
        normal_angle = math.atan2(square_y + square_size / 2 - laser_y, square_x + square_size / 2 - laser_x)
        theta = math.asin(math.sin(incident_angle - normal_angle) / refraction_index)
        refracted_angle = incident_angle - normal_angle - theta

        # Calculate the new laser endpoint after refraction
        laser_end_x = laser_x + laser_length * math.cos(laser_angle + refracted_angle)
        laser_end_y = laser_y - laser_length * math.sin(laser_angle + refracted_angle)

        # Draw the refracted laser beam
        pygame.draw.line(window, RED, (laser_x, laser_y), (laser_end_x, laser_end_y), 2)

pygame.quit()


'''


import pygame
import math

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 800
HEIGHT = 400

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Initialize the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Refraction Simulation")

# Laser attributes
laser_length = 400  # Length of the laser beam
laser_x = 0  # Initial x-coordinate of the laser
laser_y = HEIGHT // 2  # Initial y-coordinate of the laser
laser_angle = math.pi / 4  # Initial angle of the laser (45 degrees)

# Square attributes
square_size = 100  # Size of the square
square_x = WIDTH // 2 - square_size // 2  # Initial x-coordinate of the square
square_y = HEIGHT // 2 - square_size // 2  # Initial y-coordinate of the square
refraction_index = 1.5  # Initial refractive index of the square

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(BLACK)

    # Draw the laser beam
    laser_end_x = laser_x + laser_length * math.cos(laser_angle)
    laser_end_y = laser_y - laser_length * math.sin(laser_angle)
    pygame.draw.line(window, RED, (laser_x, laser_y), (laser_end_x, laser_end_y), 2)

    # Draw the transparent square stroke
    pygame.draw.rect(window, WHITE, (square_x, square_y, square_size, square_size), 2)

    # Update the window
    pygame.display.update()

    # Move the square with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= 3
    if keys[pygame.K_RIGHT]:
        square_x += 3
    if keys[pygame.K_UP]:
        square_y -= 3
    if keys[pygame.K_DOWN]:
        square_y += 3

    # Rotate the laser with the mouse movement
    mouse_x, mouse_y = pygame.mouse.get_pos()
    laser_angle = math.atan2(mouse_y - laser_y, mouse_x - laser_x)

    # Handle laser-square collision
    if square_x <= laser_end_x <= square_x + square_size and square_y <= laser_end_y <= square_y + square_size:
        # Calculate the incident angle
        incident_angle = math.atan2(laser_y - laser_end_y, laser_end_x - laser_x)

        # Calculate the normal angle and the angle of entry/exit
        normal_angle = math.atan2(square_y + square_size / 2 - laser_y, square_x + square_size / 2 - laser_x)
        entry_angle = math.pi - incident_angle + normal_angle
        exit_angle = math.asin(math.sin(entry_angle) / refraction_index) - normal_angle

        # Calculate the new laser endpoint after refraction
        laser_end_x = laser_x + laser_length * math.cos(laser_angle - exit_angle)
        laser_end_y = laser_y - laser_length * math.sin(laser_angle - exit_angle)

    # Draw the refracted laser beam
    pygame.draw.line(window, RED, (laser_x, laser_y), (laser_end_x, laser_end_y), 2)

    # Update laser position for further refractions
    laser_x = laser_end_x
    laser_y = laser_end_y

pygame.quit()

'''
import tkinter as tk

# create a new window
window = tk.Tk()

# set the window size
window.geometry("800x600")

# set the window background color to black
window.configure(bg="black")

# set the font and text
font = ("Arial", 36)
text = "Hello, World!"

# create a label with the text
label = tk.Label(window, text=text, font=font, fg="white", bg="black")

# center the label in the window
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# run the window loop
window.mainloop()


# ask for two numbers with commas
number1_input = input("Enter the first number with commas: ")
number2_input = input("Enter the second number with commas: ")

# remove commas from the input strings
number1_input = number1_input.replace(",", "")
number2_input = number2_input.replace(",", "")

# convert the input strings to floats and perform the calculation
result = float(number1_input) + float(number2_input)

# print the result
print(result)



import math
import pygame

#Asking for things

Angle_of_Arrival_Degrees = input("Donne moi un angle d'arrivée : ")
Angle_of_Arrival_Degrees = float(Angle_of_Arrival_Degrees)

Angle_of_Arrival_Radians = math.radians(Angle_of_Arrival_Degrees)

Refracion_index_1 = input("Donne moi l'indice de réfraction du milieu 1 (air = 1; eau = 1,333; plexiglass = 1,51) : ")
Refracion_index_1 = float(Refracion_index_1)

Refracion_index_2 = input("Donne moi l'indice de réfraction du milieu 2 (air = 1; eau = 1,333; plexiglass = 1,51) : ")
Refracion_index_2 = float(Refracion_index_2)

#The fun part !

First_Part_of_Calculation = ((Refracion_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refracion_index_2)

if -1 <= First_Part_of_Calculation <= 1:
    Angle_of_Refraction_Radians = math.asin((Refracion_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refracion_index_2)

    Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
    Angle_of_Refraction_Degrees_Rounded = round(Angle_of_Refraction_Degrees, 2)
else:
    Angle_of_Refraction_Degrees_Rounded = ('Reflexion')
    





#print(((Refracion_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refracion_index_2))

#Create window !

pygame.init()

Black = (0,0,0)
White = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simulator Refraction')
screen.fill(Black)
done = False



while True:
   for event in pygame.event.get():
      screen.fill(Black)
      if event.type == pygame.QUIT:
        font = pygame.font.SysFont("Arial", 36)
    txtsurf = font.render("Hello, World", True, White)
    screen.blit(txtsurf,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
pygame.display.update()


while not done:
   for event in pygame.event.get():
      screen.fill(Black)
      if event.type == pygame.QUIT:
         done = True
      font = pygame.font.SysFont("Arial", 36)
   txtsurf = font.render(str(Angle_of_Refraction_Degrees_Rounded), True, White)
   screen.blit(txtsurf,(400 - txtsurf.get_width() // 2, 300 - txtsurf.get_height() // 2))
   pygame.display.update()





import pygame

# Initialize pygame
pygame.init()

# Set up the window
window_width = 400
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Slider Demo")

# Set up the font
font = pygame.font.Font(None, 48)

# Set up the initial value of the number
number = 50

# Set up the initial position of the slider
slider_position = window_width // 2

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                slider_position -= 10
            elif event.key == pygame.K_RIGHT:
                slider_position += 10

    # Keep the slider within the window
    slider_position = max(slider_position, 0)
    slider_position = min(slider_position, window_width)

    # Calculate the value of the number based on the position of the slider
    number = int(slider_position / window_width * 100)

    # Fill the window with white
    window.fill((255, 255, 255))

    # Draw the slider
    slider_rect = pygame.Rect(slider_position - 10, window_height // 2 - 10, 20, 20)
    pygame.draw.rect(window, (255, 0, 0), slider_rect)

    # Draw the number
    number_text = font.render(str(number), True, (0, 0, 0))
    number_rect = number_text.get_rect(center=(window_width // 2, window_height // 3))
    window.blit(number_text, number_rect)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()


import pygame

# Initialize pygame
pygame.init()

# Set up the window
window_width = 400
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Slider Demo")

# Set up the font
font = pygame.font.Font(None, 48)

# Set up the initial value of the number
number = 50

# Set up the initial position of the slider
slider_position = window_width // 2

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            # Move the slider with the mouse
            slider_position = event.pos[0]

    # Keep the slider within the window
    slider_position = max(slider_position, 0)
    slider_position = min(slider_position, window_width)

    # Calculate the value of the number based on the position of the slider
    number = int(slider_position / window_width * 100)

    # Fill the window with white
    window.fill((255, 255, 255))

    # Draw the slider
    slider_rect = pygame.Rect(slider_position - 10, window_height // 2 - 10, 20, 20)
    pygame.draw.rect(window, (255, 0, 0), slider_rect)

    # Draw the number
    number_text = font.render(str(number), True, (0, 0, 0))
    number_rect = number_text.get_rect(center=(window_width // 2, window_height // 3))
    window.blit(number_text, number_rect)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()

'''

import pygame

# Initialize pygame
pygame.init()

# Set up the window
window_width = 400
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Slider Demo")

# Set up the font
font = pygame.font.Font(None, 48)

# Set up the initial value of the number
number = 50

# Set up the initial position of the slider
slider_position = window_width // 2

# Keep track of whether the left mouse button is pressed down
mouse_down = False

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the left mouse button is pressed down
            if event.button == 1:
                mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if the left mouse button is released
            if event.button == 1:
                mouse_down = False
        elif event.type == pygame.MOUSEMOTION and mouse_down:
            # Move the slider with the mouse while the left button is pressed down
            slider_position = event.pos[0]

    # Keep the slider within the window
    slider_position = max(slider_position, 0)
    slider_position = min(slider_position, window_width)

    # Calculate the value of the number based on the position of the slider
    number = int(slider_position / window_width * 100)

    # Fill the window with white
    window.fill((255, 255, 255))

    # Draw the slider
    slider_rect = pygame.Rect(slider_position - 10, window_height // 2 - 10, 20, 20)
    pygame.draw.rect(window, (255, 0, 0), slider_rect)

    # Draw the number
    number_text = font.render(str(number), True, (0, 0, 0))
    number_rect = number_text.get_rect(center=(window_width // 2, window_height // 3))
    window.blit(number_text, number_rect)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()

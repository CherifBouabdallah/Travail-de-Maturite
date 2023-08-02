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




import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Slider Example")

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the slider
slider_x = 100
slider_y = 200
slider_width = 200
slider_height = 20
slider_value = 0.5
slider_grabbed = False

# Main loop
done = False
while not done:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if slider_x <= mouse_x <= slider_x + slider_width and slider_y <= mouse_y <= slider_y + slider_height:
                    slider_grabbed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                slider_grabbed = False
        elif event.type == pygame.MOUSEMOTION:
            if slider_grabbed:
                mouse_x, mouse_y = event.pos
                slider_value = (mouse_x - slider_x) / slider_width
                slider_value = max(0, min(slider_value, 1))

    # Update
    result = slider_value ** 2

    # Draw
    screen.fill(WHITE)

    # Draw the slider
    pygame.draw.rect(screen, GRAY, [slider_x, slider_y, slider_width, slider_height])
    pygame.draw.rect(screen, BLACK, [slider_x + slider_value * slider_width - 5, slider_y, 10, slider_height])
    
    # Draw the result
    result_text = font.render("Result: {}".format(result), True, BLACK)
    screen.blit(result_text, [screen_width // 2 - result_text.get_width() // 2, slider_y + slider_height + 20])

    pygame.display.flip()

# Quit
pygame.quit()



import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Slider Example")

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the slider
slider_x = 100
slider_y = 200
slider_width = 200
slider_height = 20
slider_value = 0.5
slider_grabbed = False

# Main loop
done = False
while not done:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if slider_x <= mouse_x <= slider_x + slider_width and slider_y <= mouse_y <= slider_y + slider_height:
                    slider_grabbed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                slider_grabbed = False
        elif event.type == pygame.MOUSEMOTION:
            if slider_grabbed:
                mouse_x, mouse_y = event.pos
                slider_value = (mouse_x - slider_x) / slider_width
                slider_value = max(0, min(slider_value, 1))

    # Update
    variable = round(slider_value * 10, 2)
    result = round(variable ** 2, 2)

    # Draw
    screen.fill(WHITE)

    # Draw the slider
    pygame.draw.rect(screen, GRAY, [slider_x, slider_y, slider_width, slider_height])
    pygame.draw.rect(screen, BLACK, [slider_x + slider_value * slider_width - 5, slider_y, 10, slider_height])
    
    # Draw the variable
    variable_text = font.render("Variable: {}".format(variable), True, BLACK)
    screen.blit(variable_text, [slider_x - variable_text.get_width() - 10, slider_y + slider_height // 2 - variable_text.get_height() // 2])
    
    # Draw the result
    result_text = font.render("Result: {}".format(result), True, BLACK)
    screen.blit(result_text, [screen_width // 2 - result_text.get_width() // 2, slider_y + slider_height + 20])

    pygame.display.flip()

# Quit
pygame.quit()


import pygame

# Slider class definition
class Slider:
    def __init__(self, value, pos_x, pos_y):
        self.value = value
        self.grabbed = False
        self.width = 200
        self.height = 20
        self.pos_x = pos_x
        self.pos_y = pos_y


# Initialize Pygame
pygame.init()

# Set up the window
window_width = 400
window_height = 200
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Slider Demo")

# Create two instances of the Slider class
slider1 = Slider(0.5, 200, 50)
slider2 = Slider(0.5, 200, 100)

# Run the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Clear the window
    window.fill((0, 0, 0))

    # Draw the sliders
    pygame.draw.rect(window, 'gray', (100, 50, slider1.width, slider1.height))
    pygame.draw.rect(window, 'white', [slider1.pos_x + slider1.value * slider1.width - 5, slider1.pos_y, 10, slider1.height])

    pygame.draw.rect(window, 'gray', (100, 100, slider2.width, slider2.height))
    pygame.draw.rect(window, 'white', [slider2.pos_x + slider2.value * slider2.width - 5, slider2.pos_y, 10, slider2.height])





    # Update the display
    pygame.display.flip()

# Quit the Pygame application
pygame.quit()





import pygame

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Create a font object
font = pygame.font.Font(None, 36)

# Render the text
text = font.render("Hello, Pygame!", True, (255, 255, 255))

# Blit the text onto the screen
screen.blit(text, (100, 100))

# Update the display
pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()




import pygame
import math
import time

pygame.init()
caption = "Refraction Simulator"
screen_width, screen_height = 1000, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(caption)

#Definition of colors and font sizes
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
Bigfont = pygame.font.SysFont("Calibri", 72)
font = pygame.font.SysFont("Calibri", 52)
Smallfont = pygame.font.SysFont("Calibri", 20)

slider_width = 200
slider_height = 20

mouse_x = 0
mouse_y = 0

class Slider:
    def __init__(self, value, pos_x, pos_y, min_value, max_value, round):
        self.value = value
        self.grabbed = False
        self.width = slider_width
        self.height = slider_height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.header = 0
        self.align_x = 0
        self.align_y = 0
        self.start_value = 0
        self.min_value = min_value
        self.max_value = max_value
        self.round = round

    def update_grabbed(self, mouse_x, mouse_y):
        mouse_x, mouse_y = event.pos
        if self.pos_x <= mouse_x <= self.pos_x + self.width and self.pos_y <= mouse_y <= self.pos_y + self.height:
            self.grabbed = True

    def update_released(self):
        if event.button == 1:
            self.grabbed = False

    def update_motion(self, mouse_x):
        if self.grabbed:
            mouse_x, _ = event.pos
            self.value = (mouse_x - self.pos_x) / self.width
            self.value = max(self.min_value, min(self.value, self.max_value))

    def calculation_value(self, multiplyer):
        self.real_value = round(self.value * multiplyer, self.round)

    def draw_slider(self):
        pygame.draw.rect(screen, gray, [self.pos_x, self.pos_y, self.width, self.height])
        pygame.draw.rect(screen, white, [self.pos_x + self.value * self.width - 5, self.pos_y, 10, self.height])

    def render_header(self, header):
        self.header = Smallfont.render(header, True, (255, 255, 255))

    def blit_header(self, align_x, align_y):
        screen.blit(self.header, (screen_width // align_x - self.header.get_width() // align_x, screen_height // align_y - self.header.get_height() // align_y))

slider_RI1 = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // 10 - slider_height // 10, -1, 1, 2) #this is experimental, remove when final ! (the -1 is exp)
slider_RI2 = Slider(0.5, screen_width // (1.2) - slider_width // (1.2), screen_height // 10 - slider_height // 10, 0, 1, 2)
slider_angle = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // 10 - slider_height // 10, 0, 1, 2)

slider_square_x = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0)
slider_square_y = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (100/95) - slider_height // (100/95), 0, 1, 0)


def Calculation():
    pre_calculation = ((slider_RI1.real_value * math.sin(math.radians(slider_angle.real_value))) / slider_RI2.real_value)

    if -1 <= pre_calculation <= 1:
        Angle_of_Refraction_Radians = math.asin(pre_calculation)
        Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
        Angle_of_Refraction_Degrees = round(Angle_of_Refraction_Degrees, 2)
        
    else:
        Angle_of_Refraction_Degrees = 'Reflexion'
    
    #print(Angle_of_Refraction_Degrees)


done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                slider_RI1.update_grabbed(mouse_x, mouse_y)
                slider_RI2.update_grabbed(mouse_x, mouse_y)
                slider_angle.update_grabbed(mouse_x, mouse_y)
                slider_square_x.update_grabbed(mouse_x, mouse_y)
                slider_square_y.update_grabbed(mouse_x, mouse_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            slider_RI1.update_released()
            slider_RI2.update_released()
            slider_angle.update_released()
            slider_square_x.update_released()
            slider_square_y.update_released()

        elif event.type == pygame.MOUSEMOTION:
            slider_RI1.update_motion(mouse_x)
            slider_RI2.update_motion(mouse_x)
            slider_angle.update_motion(mouse_x)
            slider_square_x.update_motion(mouse_x)
            slider_square_y.update_motion(mouse_x)

    screen.fill(black)

    slider_RI1.calculation_value(3)
    slider_RI1.render_header(str(slider_RI1.real_value))
    slider_RI1.draw_slider()
    slider_RI1.blit_header(4.45, 15)

    slider_RI2.calculation_value(2)
    slider_RI2.render_header(str(slider_RI2.real_value))
    slider_RI2.draw_slider()
    slider_RI2.blit_header(1.3, 15)
    
    slider_angle.calculation_value(180)
    slider_angle.render_header(str(slider_angle.real_value))
    slider_angle.draw_slider()
    slider_angle.blit_header(2, 15)

    slider_square_x.calculation_value(1000)
    slider_square_x.render_header(str(slider_square_x.real_value))
    slider_square_x.draw_slider()
    slider_square_x.blit_header(3, 1.11)

    slider_square_y.calculation_value(700)
    slider_square_y.render_header(str(slider_square_y.real_value))
    slider_square_y.draw_slider()
    slider_square_y.blit_header(3, 1.05)

    
    #Calculation()

    pygame.draw.rect(screen, white, [slider_square_x.real_value - 50, slider_square_y.real_value - 50, 100, 100])
    pygame.draw.rect(screen, black, [slider_square_x.real_value - 45, slider_square_y.real_value - 45, 90, 90])

    x = 25
    y = screen_height / 2
    square_entered = False
    square_first_face_touched = False
    square_last_face_touched = False
    square_up_face_touched = False
    square_down_face_touched = False

    while(x < screen_width):

        if slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50:
            square_entered = True

        if x == slider_square_x.real_value - 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50:
            square_first_face_touched = True
            y = y + slider_RI1.real_value
        if square_first_face_touched:
            y = y + slider_RI1.real_value

        if x == slider_square_x.real_value + 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50:
            y = y + slider_RI2.real_value
            square_last_face_touched = True
        if square_last_face_touched:
            y = y + slider_RI2.real_value

        if y >= slider_square_y.real_value + 50 and slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and not square_down_face_touched and square_entered:
            y = y + slider_RI2.real_value
            square_down_face_touched = True
        if square_down_face_touched:
            y = y + slider_RI2.real_value

        if y <= slider_square_y.real_value - 50 and slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and not square_up_face_touched and square_entered:
            y = y + slider_RI2.real_value
            square_up_face_touched = True
        if square_up_face_touched:
            y = y + slider_RI2.real_value

        pygame.draw.line(screen, 'red', (x, y), (x + 1, y), 5)
        x = x + 1

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
'''
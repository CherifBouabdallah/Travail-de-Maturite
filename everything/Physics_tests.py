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




import math
import pygame



Angle_of_Arrival_Degrees = input("Donne moi un angle d'arrivée : ")
Angle_of_Arrival_Degrees = float(Angle_of_Arrival_Degrees)

Angle_of_Arrival_Radians = math.radians(Angle_of_Arrival_Degrees)

Refracion_index_1 = input("Donne moi l'indice de réfraction du milieu 1 (air = 1; eau = 1.333; plexiglass = 1.51) : ")
Refracion_index_1 = float(Refracion_index_1)

Refracion_index_2 = input("Donne moi l'indice de réfraction du milieu 2 (air = 1; eau = 1.333; plexiglass = 1.51) : ")
Refracion_index_2 = float(Refracion_index_2)





First_Part_of_Calculation = ((Refracion_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refracion_index_2)

if -1 <= First_Part_of_Calculation <= 1:
    Angle_of_Refraction_Radians = math.asin((Refracion_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refracion_index_2)

    Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
    Angle_of_Refraction_Degrees_Rounded = round(Angle_of_Refraction_Degrees, 2)
else:
    Angle_of_Refraction_Degrees_Rounded = ('Reflexion')
    Angle_of_Refraction_Degrees = ('Reflexion')


#Create window !
pygame.init()

caption = "Refraction Simulator"
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption(caption)
screen_width, screen_height = 1000, 700

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

Bigfont = pygame.font.SysFont("Calibri", 72)
font = pygame.font.SysFont("Calibri", 52)
Smallfont = pygame.font.SysFont("Calibri", 20)

# Set up the slider

slider_RI2_width = 200
slider_RI2_height = 20
slider_RI2_x = (screen_width // (8/7) - slider_RI2_width // (8/7))
slider_RI2_y = ((screen_height // 5 - slider_RI2_height // 5))
slider_RI2_value = 0.5
slider_RI2_grabbed = False


Angle_of_Refraction_Display = Bigfont.render((str(Angle_of_Refraction_Degrees)), True,  white)
Angle_of_Arrival_Display = font.render((str(Angle_of_Arrival_Degrees)), True,  white)
Refracion_index_1_Display = font.render((str(Refracion_index_1)), True,  white)
Refracion_index_2_Display = font.render((str(Refracion_index_2)), True,  white)

Angle_of_Refraction_Display_Header = font.render((str("Angle réfracté")), True,  white)
Angle_of_Arrival_Display_Header = Smallfont.render(("Angle d'arrivée"), True,  white)
Refracion_index_1_Display_Header = Smallfont.render(("Indice de réfraction du milieu 1"), True,  white)
Refracion_index_2_Display_Header = Smallfont.render(("Indice de réfraction du milieu 2"), True,  white)

# Main Loop
done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if slider_RI2_x <= mouse_x <= slider_RI2_x + slider_RI2_width and slider_RI2_y <= mouse_y <= slider_RI2_y + slider_RI2_height:
                    slider_RI2_grabbed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                slider_RI2_grabbed = False
        elif event.type == pygame.MOUSEMOTION:
            if slider_RI2_grabbed:
                mouse_x, mouse_y = event.pos
                slider_RI2_value = (mouse_x - slider_RI2_x) / slider_RI2_width
                slider_RI2_value = max(0.01, min(slider_RI2_value, 1))
    if -1 <= First_Part_of_Calculation <= 1:
        Angle_of_Refraction_Radians = math.asin((Refracion_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refracion_index_2)

        Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
    else:
        Angle_of_Refraction_Degrees = ('Reflexion')

    screen.fill(black)

    Refracion_index_2 = round(slider_RI2_value * 2, 2)
    #Refracion_index_1 = round(slider_RI1_value * 10, 2)
    result = round(Angle_of_Refraction_Degrees, 2)

    Refracion_index_2_text = Smallfont.render(str(Refracion_index_2), True, white)
    result_text = font.render(str(result), True, white)

    pygame.draw.rect(screen, gray, [slider_RI2_x, slider_RI2_y, slider_RI2_width, slider_RI2_height])
    pygame.draw.rect(screen, white, [slider_RI2_x + slider_RI2_value * slider_RI2_width - 5, slider_RI2_y, 10, slider_RI2_height])


    #Shows things on screen
    #screen.blit(Angle_of_Refraction_Display, (screen_width // 2 - Angle_of_Refraction_Display.get_width() // 2, screen_height // 2 - Angle_of_Refraction_Display.get_height() // 2))
    screen.blit(Angle_of_Arrival_Display, (screen_width // 2 - Angle_of_Arrival_Display.get_width() // 2, screen_height // 5 - Angle_of_Arrival_Display.get_height() // 5))
    screen.blit(Refracion_index_1_Display, (screen_width // 8 - Refracion_index_1_Display.get_width() // 8, screen_height // 5 - Refracion_index_1_Display.get_height() // 5))
    #screen.blit(Refracion_index_2_Display, (screen_width // (8/7) - Refracion_index_2_Display.get_width() // (8/7), screen_height // 5 - Refracion_index_2_Display.get_height() // 5))

    screen.blit(Angle_of_Refraction_Display_Header, (screen_width // 2 - Angle_of_Refraction_Display_Header.get_width() // 2, screen_height // 2.5 - Angle_of_Refraction_Display_Header.get_height() // 2.5))
    screen.blit(Angle_of_Arrival_Display_Header, (screen_width // 2 - Angle_of_Arrival_Display_Header.get_width() // 2, screen_height // 10 - Angle_of_Arrival_Display_Header.get_height() // 10))
    screen.blit(Refracion_index_1_Display_Header, (screen_width // 8 - Refracion_index_1_Display_Header.get_width() // 8, screen_height // 10 - Refracion_index_1_Display_Header.get_height() // 10))
    screen.blit(Refracion_index_2_Display_Header, (screen_width // (8/7) - Refracion_index_2_Display_Header.get_width() // (8/7), screen_height // 10 - Refracion_index_2_Display_Header.get_height() // 109))
    

    screen.blit(Refracion_index_2_text, [slider_RI2_x - Refracion_index_2_text.get_width() - 10, slider_RI2_y + slider_RI2_height // 2 - Refracion_index_2_text.get_height() // 2])
    screen.blit(result_text, (screen_width // 2 - Refracion_index_2_Display.get_width() // 2, screen_height // 2 - Refracion_index_2_Display.get_height() // 2))
   
   
   
   
   
   
    pygame.display.update()
    pygame.time.Clock().tick(30)

pygame.quit()



# TO ADD : 


# A slider to choose angle and RI
# the laser
# the transparent objects

# DONE :
# A window with the output angle
# In case of a reflexion !
# # add comas
# go from tkiner to pygame
# show RI and Angle on screen






import math
import pygame


Angle_of_Arrival_Degrees = input("Donne moi un angle d'arrivée : ")
Angle_of_Arrival_Degrees = float(Angle_of_Arrival_Degrees)

Angle_of_Arrival_Radians = math.radians(Angle_of_Arrival_Degrees)

Refraction_index_1 = input("Donne moi l'indice de réfraction du milieu 1 (air = 1; eau = 1.333; plexiglass = 1.51) : ")
Refraction_index_1 = float(Refraction_index_1)

Refraction_index_2 = input("Donne moi l'indice de réfraction du milieu 2 (air = 1; eau = 1.333; plexiglass = 1.51) : ")
Refraction_index_2 = float(Refraction_index_2)





First_Part_of_Calculation = ((Refraction_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refraction_index_2)

if -1 <= First_Part_of_Calculation <= 1:
    Angle_of_Refraction_Radians = math.asin((Refraction_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refraction_index_2)

    Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
    Angle_of_Refraction_Degrees_Rounded = round(Angle_of_Refraction_Degrees, 2)
else:
    Angle_of_Refraction_Degrees_Rounded = ('Reflexion')
    Angle_of_Refraction_Degrees = ('Reflexion')




#Create window !
pygame.init()

caption = "Refraction Simulator"
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption(caption)
screen_width, screen_height = 1000, 700

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

Bigfont = pygame.font.SysFont("Calibri", 72)
font = pygame.font.SysFont("Calibri", 52)
Smallfont = pygame.font.SysFont("Calibri", 20)

# Set up the slider

slider_RI2_width = 200
slider_RI2_height = 20
slider_RI2_x = (screen_width // (8/7) - slider_RI2_width // (8/7))
slider_RI2_y = ((screen_height // 5 - slider_RI2_height // 5))
slider_RI2_value = 0.5
slider_RI2_grabbed = False

slider_RI1_width = 200
slider_RI1_height = 20
slider_RI1_x = (screen_width // 8 - slider_RI2_width // 8)
slider_RI1_y = ((screen_height // 5 - slider_RI2_height // 5))
slider_RI1_value = 0.5
slider_RI1_grabbed = False

slider_AOA_width = 200
slider_AOA_height = 20
slider_AOA_x = (screen_width // 2 - slider_AOA_width // 2)
slider_AOA_y = ((screen_height // 5 - slider_AOA_height // 5))
slider_AOA_value = 0.5
slider_AOA_grabbed = False



Angle_of_Refraction_Display = Bigfont.render((str(Angle_of_Refraction_Degrees)), True,  white)
Angle_of_Arrival_Display = font.render((str(Angle_of_Arrival_Degrees)), True,  white)
Refraction_index_1_Display = font.render((str(Refraction_index_1)), True,  white)
Refraction_index_2_Display = font.render((str(Refraction_index_2)), True,  white)

Angle_of_Refraction_Display_Header = font.render((str("Angle réfracté")), True,  white)
Angle_of_Arrival_Display_Header = Smallfont.render(("Angle d'arrivée"), True,  white)
Refraction_index_1_Display_Header = Smallfont.render(("Indice de réfraction du milieu 1"), True,  white)
Refraction_index_2_Display_Header = Smallfont.render(("Indice de réfraction du milieu 2"), True,  white)

# Main Loop
done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if slider_RI2_x <= mouse_x <= slider_RI2_x + slider_RI2_width and slider_RI2_y <= mouse_y <= slider_RI2_y + slider_RI2_height:
                    slider_RI2_grabbed = True
                if slider_RI1_x <= mouse_x <= slider_RI1_x + slider_RI1_width and slider_RI1_y <= mouse_y <= slider_RI1_y + slider_RI1_height:
                    slider_RI1_grabbed = True
                if slider_AOA_x <= mouse_x <= slider_AOA_x + slider_AOA_width and slider_AOA_y <= mouse_y <= slider_AOA_y + slider_AOA_height:
                    slider_AOA_grabbed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                slider_RI2_grabbed = False
            if event.button == 1:
                slider_RI1_grabbed = False
            if event.button == 1:
                slider_AOA_grabbed = False

        elif event.type == pygame.MOUSEMOTION:
            if slider_RI2_grabbed:
                mouse_x, mouse_y = event.pos
                slider_RI2_value = (mouse_x - slider_RI2_x) / slider_RI2_width
                slider_RI2_value = max(0.01, min(slider_RI2_value, 1))
            if slider_RI1_grabbed:
                mouse_x, mouse_y = event.pos
                slider_RI1_value = (mouse_x - slider_RI1_x) / slider_RI1_width
                slider_RI1_value = max(0.01, min(slider_RI1_value, 1))
            if slider_AOA_grabbed:
                mouse_x, mouse_y = event.pos
                slider_AOA_value = (mouse_x - slider_AOA_x) / slider_AOA_width
                slider_AOA_value = max(0, min(slider_AOA_value, 1))

    if -1 <= First_Part_of_Calculation <= 1:
        Angle_of_Refraction_Radians = math.asin((Refraction_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refraction_index_2)

        Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
    else:
        Angle_of_Refraction_Degrees = ('Reflexion')

    screen.fill(black)

    Refraction_index_2 = round(slider_RI2_value * 2, 2)
    Refraction_index_1 = round(slider_RI1_value * 2, 2)
    Angle_of_Arrival_Radians = round(slider_AOA_value * 90, 2)
    
    result = round(Angle_of_Refraction_Degrees, 2)

    Refraction_index_2_text = Smallfont.render(str(Refraction_index_2), True, white)
    Refraction_index_1_text = Smallfont.render(str(Refraction_index_1), True, white)
    Angle_of_Arrival_Radians_text = Smallfont.render(str(Angle_of_Arrival_Radians), True, white)
    result_text = font.render(str(result), True, white)

    pygame.draw.rect(screen, gray, [slider_RI2_x, slider_RI2_y, slider_RI2_width, slider_RI2_height])
    pygame.draw.rect(screen, white, [slider_RI2_x + slider_RI2_value * slider_RI2_width - 5, slider_RI2_y, 10, slider_RI2_height])

    pygame.draw.rect(screen, gray, [slider_RI1_x, slider_RI1_y, slider_RI1_width, slider_RI1_height])
    pygame.draw.rect(screen, white, [slider_RI1_x + slider_RI1_value * slider_RI1_width - 5, slider_RI1_y, 10, slider_RI1_height])

    pygame.draw.rect(screen, gray, [slider_AOA_x, slider_AOA_y, slider_AOA_width, slider_AOA_height])
    pygame.draw.rect(screen, white, [slider_AOA_x + slider_AOA_value * slider_AOA_width - 5, slider_AOA_y, 10, slider_AOA_height])


    #Shows things on screen

    screen.blit(Angle_of_Refraction_Display_Header, (screen_width // 2 - Angle_of_Refraction_Display_Header.get_width() // 2, screen_height // 2.5 - Angle_of_Refraction_Display_Header.get_height() // 2.5))
    screen.blit(Angle_of_Arrival_Display_Header, (screen_width // 2 - Angle_of_Arrival_Display_Header.get_width() // 2, screen_height // 10 - Angle_of_Arrival_Display_Header.get_height() // 10))
    screen.blit(Refraction_index_1_Display_Header, (screen_width // 8 - Refraction_index_1_Display_Header.get_width() // 8, screen_height // 10 - Refraction_index_1_Display_Header.get_height() // 10))
    screen.blit(Refraction_index_2_Display_Header, (screen_width // (8/7) - Refraction_index_2_Display_Header.get_width() // (8/7), screen_height // 10 - Refraction_index_2_Display_Header.get_height() // 109))
    

    screen.blit(Refraction_index_2_text, [slider_RI2_x - Refraction_index_2_text.get_width() - 10, slider_RI2_y + slider_RI2_height // 2 - Refraction_index_2_text.get_height() // 2])
    screen.blit(result_text, (screen_width // 2 - Refraction_index_2_Display.get_width() // 2, screen_height // 2 - Refraction_index_2_Display.get_height() // 2))

    screen.blit(Refraction_index_1_text, [slider_RI1_x - Refraction_index_1_text.get_width() - 10, slider_RI1_y + slider_RI1_height // 2 - Refraction_index_1_text.get_height() // 2])
    screen.blit(result_text, (screen_width // 2 - Refraction_index_1_Display.get_width() // 2, screen_height // 2 - Refraction_index_1_Display.get_height() // 2))   

    screen.blit(Angle_of_Arrival_Radians_text, [slider_AOA_x - Angle_of_Arrival_Radians_text.get_width() - 10, slider_AOA_y + slider_AOA_height // 2 - Angle_of_Arrival_Radians_text.get_height() // 2])
    screen.blit(result_text, (screen_width // 2 - Angle_of_Arrival_Display.get_width() // 2, screen_height // 2 - Angle_of_Arrival_Display.get_height() // 2))   
   
   
   
   
   
    pygame.display.update()
    pygame.time.Clock().tick(30)

pygame.quit()




    x = 25
    y = screen_height / 2
    refracted_down = False
    refracted_up = False
    square_touched = False

    while(x < screen_width):

        if not square_touched and x >= slider_square_x.real_value / 2 - 50 and slider_square_y.real_value / 2 - 50 <= y <= slider_square_y.real_value / 2 + 50:
            y = y + slider_RI1.real_value
            square_touched = True

        if square_touched == True:
            y = y + slider_RI1.real_value

        if not refracted_down and y >= slider_square_y.real_value / 2 + 50 and slider_square_x.real_value / 2 - 50 <= x <= slider_square_x.real_value / 2 + 50:
            y = y + slider_RI2.real_value
            refracted_down = True

        if refracted_down:
            y = y + slider_RI2.real_value

        if not refracted_up and y <= slider_square_y.real_value / 2 - 50 and slider_square_x.real_value / 2 - 50 <= x <= slider_square_x.real_value / 2 + 50:
            y = y - slider_RI2.real_value
            refracted_up = True  

        if refracted_up:
            y = y + slider_RI2.real_value

        if (x >= slider_square_x.real_value / 2 + 50 and not refracted_down and not refracted_up):
            y = y + slider_RI2.real_value    
    
'''


import pygame
import math
#from MyFunctions import * #the "*" imports all functions !

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
Smallfont = pygame.font.SysFont("Calibri", 22)

slider_width = 200
slider_height = 20
mouse_x = 0
mouse_y = 0
refraction = None


class Slider:
    def __init__(self, value, pos_x, pos_y, min_value, max_value, round, real_value, multiplyer):
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
        self.negative_value = 0
        self.real_value = real_value
        self.multiplyer = multiplyer

    def update_grabbed(self, event, mouse_x, mouse_y):
        mouse_x, mouse_y = event.pos
        if self.pos_x <= mouse_x <= self.pos_x + self.width and self.pos_y <= mouse_y <= self.pos_y + self.height:
            self.grabbed = True

    def update_released(self, event):
        if event.button == 1:
            self.grabbed = False

    def update_motion(self, event, mouse_x):
        if self.grabbed:
            mouse_x, _ = event.pos
            self.value = (mouse_x - self.pos_x) / self.width
            self.value = max(self.min_value, min(self.value, self.max_value))

    def calculation_value(self, addon):
        self.real_value = round(self.value * self.multiplyer + addon, self.round)
        if self.value == 0:
            self.negative_value = 0
        if self.value < 0.5:
            self.negative_value = 1-self.value - 0.5
        if self.value > 0.5:
            self.negative_value = -self.value + 0.5

        self.negative_value = -round(self.negative_value * self.multiplyer, self.round)
    
    def draw_slider(self):
        pygame.draw.rect(screen, gray, [self.pos_x, self.pos_y, self.width, self.height])
        pygame.draw.rect(screen, white, [self.pos_x + self.value * self.width - 5, self.pos_y, 10, self.height])

    def render_header(self, header):
        self.header = Smallfont.render(header, True, black)

    def blit_header(self, align_x, align_y):
        screen.blit(self.header, (screen_width // align_x - self.header.get_width() // align_x, screen_height // align_y - self.header.get_height() // align_y))


slider_RI1 = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // 10 - slider_height // 10, 0.05, 1, 2, None, 2)
slider_RI2 = Slider(0.5, screen_width // (1.2) - slider_width // (1.2), screen_height // 10 - slider_height // 10, 0.05, 1, 2, None, 2)
slider_angle = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // 10 - slider_height // 10, 0, 1, 2, None, 180)
slider_square_x = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0, None, screen_width)
slider_square_y = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (100/95) - slider_height // (100/95), 0, 1, 0, None , screen_height)
slider_laser_x = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0, None, screen_height)
slider_laser_angle = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (100/95) - slider_height // (100/95), 0.01, 0.99, 2, None, 180)

all_sliders = slider_RI1, slider_RI2, slider_angle, slider_square_x, slider_square_y, slider_laser_x, slider_laser_angle

def Calculation():


    Angle_of_Refraction_Degrees_in = 0
    x_laser_increment = round(math.sin(math.radians(abs(slider_laser_angle.real_value-90))), 2)

    if round(math.sin(math.radians(slider_laser_angle.real_value-90)), 2) == 0:
            y_laser_increment = 0
    else:
            y_laser_increment = round(math.cos(math.radians(abs(slider_laser_angle.real_value-90))), 2) / x_laser_increment

    pre_calculation_in = ((slider_RI1.real_value * math.sin(math.radians(round(abs(slider_laser_angle.real_value-90), 2)))) / slider_RI2.real_value)
    
    if slider_RI1.real_value == 1 and slider_RI2.real_value == 1:

        x_square_increment_in = round(math.sin(math.radians(abs(slider_laser_angle.real_value-90))), 2)

        if round(math.sin(math.radians(slider_laser_angle.real_value-90)), 2) == 0:
            y_square_increment_in = 0
        else:
            y_square_increment_in = round(math.cos(math.radians(abs(slider_laser_angle.real_value-90))), 2) / x_square_increment_in

    else:
        if -1 <= pre_calculation_in <= 1:
            refraction = True
            Angle_of_Refraction_Radians = math.asin(pre_calculation_in)
            Angle_of_Refraction_Degrees_in = math.degrees(Angle_of_Refraction_Radians)
            Angle_of_Refraction_Degrees_in = round(Angle_of_Refraction_Degrees_in, 2)

            x_square_increment_in = round(math.sin(math.radians(Angle_of_Refraction_Degrees_in)), 2)
            y_square_increment_in = round((math.cos(math.radians(Angle_of_Refraction_Degrees_in)))/ x_square_increment_in, 2)

        else:
            refraction = False

    return x_laser_increment, y_laser_increment, x_square_increment_in, y_square_increment_in, Angle_of_Refraction_Degrees_in


def Square_function():

    x_laser_increment, y_laser_increment, x_square_increment_in, y_square_increment_in, Angle_of_Refraction_Degrees_in = Calculation()

    pygame.draw.rect(screen, white, [slider_square_x.real_value - 50, slider_square_y.real_value - 50, 100, 100])
    pygame.draw.rect(screen, black, [slider_square_x.real_value - 45, slider_square_y.real_value - 45, 90, 90])

    x = 25
    y = slider_laser_x.real_value
    square_entered = False
    square_first_face_touched = False


    while(x < screen_width):
        print(Angle_of_Refraction_Degrees_in, x_square_increment_in, y_square_increment_in, x_laser_increment, y_laser_increment)

        if slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50:
            square_entered = True

        if round(x, 0)+-1 <= slider_square_x.real_value - 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50 and not square_first_face_touched and square_entered:
            square_first_face_touched = True
            y = y + ((y_laser_increment - y_square_increment_in)- y_laser_increment)

        if square_first_face_touched:
            y = y + ((y_laser_increment - y_square_increment_in)- y_laser_increment)

        pygame.draw.line(screen, 'red', (x, y), (x + 1, y), 5)
        x = x + 1
        y = y + y_laser_increment


def Slider_printer(slider_RI1, slider_RI2, slider_angle, slider_square_x, slider_square_y, slider_laser_x, slider_laser_angle):
    slider_RI1.calculation_value(0)
    slider_RI1.render_header(str(slider_RI1.real_value))
    slider_RI1.draw_slider()
    slider_RI1.blit_header(4.45, 10)

    slider_RI2.calculation_value(0)
    slider_RI2.render_header(str(slider_RI2.real_value))
    slider_RI2.draw_slider()
    slider_RI2.blit_header(1.3, 10)
    
    slider_angle.calculation_value(0)
    slider_angle.render_header(str(slider_angle.real_value))
    slider_angle.draw_slider()
    slider_angle.blit_header(2, 10)

    slider_square_x.calculation_value(0)
    slider_square_x.render_header(str(slider_square_x.real_value))
    slider_square_x.draw_slider()
    slider_square_x.blit_header(2, 1.11)

    slider_square_y.calculation_value(0)
    slider_square_y.render_header(str(slider_square_y.real_value))
    slider_square_y.draw_slider()
    slider_square_y.blit_header(2, 1.05)

    slider_laser_x.calculation_value(0)
    slider_laser_x.render_header(str(slider_laser_x.real_value))
    slider_laser_x.draw_slider()
    slider_laser_x.blit_header(4.45, 1.11)

    slider_laser_angle.calculation_value(0)
    slider_laser_angle.render_header(str(round(slider_laser_angle.real_value - 90, 0)))
    slider_laser_angle.draw_slider()
    slider_laser_angle.blit_header(4.45, 1.05)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                slider_RI1.update_grabbed(event, mouse_x, mouse_y)
                slider_RI2.update_grabbed(event, mouse_x, mouse_y)
                slider_angle.update_grabbed(event, mouse_x, mouse_y)
                slider_square_x.update_grabbed(event, mouse_x, mouse_y)
                slider_square_y.update_grabbed(event, mouse_x, mouse_y)
                slider_laser_x.update_grabbed(event, mouse_x, mouse_y)
                slider_laser_angle.update_grabbed(event, mouse_x, mouse_y)


        elif event.type == pygame.MOUSEBUTTONUP:
            slider_RI1.update_released(event)
            slider_RI2.update_released(event)
            slider_angle.update_released(event)
            slider_square_x.update_released(event)
            slider_square_y.update_released(event)
            slider_laser_x.update_released(event)
            slider_laser_angle.update_released(event)



        elif event.type == pygame.MOUSEMOTION:
            slider_RI1.update_motion(event, mouse_x)
            slider_RI2.update_motion(event, mouse_x)
            slider_angle.update_motion(event, mouse_x)
            slider_square_x.update_motion(event, mouse_x)
            slider_square_y.update_motion(event, mouse_x)
            slider_laser_x.update_motion(event, mouse_x)
            slider_laser_angle.update_motion(event, mouse_x)

    screen.fill(black)
    Slider_printer(slider_RI1, slider_RI2, slider_angle, slider_square_x, slider_square_y, slider_laser_x, slider_laser_angle)
    Square_function()
    pygame.display.update()
    pygame.time.Clock().tick(60)
    
pygame.quit()
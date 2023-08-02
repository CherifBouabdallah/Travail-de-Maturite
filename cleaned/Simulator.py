import pygame
import math
from Slider_Class import Slider
from Slider_Printer import Slider_printer

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

def Square_function():

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

    Slider_printer()
    #Calculation()

    Square_function()

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()

# TO ADD : 

# optimization
# the laser movement
# the transparent square
# the transparent triangle

# DONE :

# A window with the output angle
# In case of a reflexion !
# # add comas
# go from tkiner to pygame
# show RI and Angle on screen
# A slider to choose angle and RI
# remove the prompt to ask for angles
# fix crash !
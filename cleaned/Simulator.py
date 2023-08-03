import pygame
import math
from MyFunctions import * #the "*" imports all functions !

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


slider_RI1 = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // 10 - slider_height // 10, 0, 1, 2)
slider_RI2 = Slider(0.5, screen_width // (1.2) - slider_width // (1.2), screen_height // 10 - slider_height // 10, 0, 1, 2)
slider_angle = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // 10 - slider_height // 10, 0, 1, 2)
slider_square_x = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0)
slider_square_y = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (100/95) - slider_height // (100/95), 0, 1, 0)
slider_laser_x = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0)
slider_laser_angle = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (100/95) - slider_height // (100/95), 0, 1, 2)

all_sliders = slider_RI1, slider_RI2, slider_angle, slider_square_x, slider_square_y, slider_laser_x, slider_laser_angle

def Square_function():

    pygame.draw.rect(screen, white, [slider_square_x.real_value - 50, slider_square_y.real_value - 50, 100, 100])
    pygame.draw.rect(screen, black, [slider_square_x.real_value - 45, slider_square_y.real_value - 45, 90, 90])

    x_increment = (math.sin(math.radians(slider_laser_angle.real_value)))
    y_increment = (math.cos(math.radians(slider_laser_angle.real_value)))

    

    x = 25
    y = slider_laser_x.real_value
    square_entered = False
    square_first_face_touched = False
    square_last_face_touched = False
    square_up_face_touched = False
    square_down_face_touched = False

    while(x < screen_width):

        if slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50:
            square_entered = True

        if x <= slider_square_x.real_value - 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50 and not square_first_face_touched and square_entered:
            square_first_face_touched = True
            y = y + slider_RI1.real_value
        if square_first_face_touched:
            y = y + slider_RI1.real_value

        if x == slider_square_x.real_value + 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50 and not square_last_face_touched and square_entered:
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
        x = x + round(x_increment, 2)
        y = y + round(y_increment, 2)

angle_of_refraction_degrees = Calculation(slider_RI1, slider_angle, slider_RI2)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                all_sliders.update_grabbed(event, mouse_x, mouse_y)


        elif event.type == pygame.MOUSEBUTTONUP:
            all_sliders.update_released(event)


        elif event.type == pygame.MOUSEMOTION:
            all_sliders.update_motion(event, mouse_x)

    screen.fill(black)
    Slider_printer(slider_RI1, slider_RI2, slider_angle, slider_square_x, slider_square_y, slider_laser_x, slider_laser_angle)
    angle_of_refraction_degrees = Calculation(slider_RI1, slider_angle, slider_RI2)
    Square_function()

    pygame.display.update()
    pygame.time.Clock().tick(60)
    
pygame.quit()

# TO ADD : 

# optimization
# the laser movement
# the transparent square
# the transparent triangle
# a reset button

# DONE :

# A window with the output angle
# In case of a reflexion !
# # add comas
# go from tkiner to pygame
# show RI and Angle on screen
# A slider to choose angle and RI
# remove the prompt to ask for angles
# fix crash !
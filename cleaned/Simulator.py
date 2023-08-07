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
refraction = None


slider_RI1 = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // 10 - slider_height // 10, 0.05, 1, 2, None, 2)
slider_RI2 = Slider(0.5, screen_width // (1.2) - slider_width // (1.2), screen_height // 10 - slider_height // 10, 0.05, 1, 2, None, 2)
slider_angle = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // 10 - slider_height // 10, 0, 1, 2, None, 180)
slider_square_x = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0, None, screen_width)
slider_square_y = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (100/95) - slider_height // (100/95), 0, 1, 0, None , screen_height)
slider_laser_x = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0, None, screen_height)
slider_laser_angle = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (100/95) - slider_height // (100/95), 0, 1, 2, None, 180)

all_sliders = slider_RI1, slider_RI2, slider_angle, slider_square_x, slider_square_y, slider_laser_x, slider_laser_angle

def Calculation():
    x_laser_increment = round(math.sin(math.radians(slider_laser_angle.real_value-90)), 2)
    y_laser_increment = round(math.cos(math.radians(slider_laser_angle.real_value-90)), 2)

    pre_calculation_in = ((slider_RI1.real_value * math.sin(math.radians(round(slider_laser_angle.real_value, 2)-90))) / slider_RI2.real_value)

    if -1 <= pre_calculation_in <= 1:
        Angle_of_Refraction_Radians = math.asin(pre_calculation_in)
        Angle_of_Refraction_Degrees_in = math.degrees(Angle_of_Refraction_Radians)
        Angle_of_Refraction_Degrees_in = round(Angle_of_Refraction_Degrees_in, 2)

        x_square_increment_in = round(math.sin(math.radians(Angle_of_Refraction_Degrees_in)), 2)
        y_square_increment_in = round(math.cos(math.radians(Angle_of_Refraction_Degrees_in)), 2)
        x_square_angle_in = round(math.sin(math.radians(slider_laser_angle.real_value-90)), 2)
        y_square_angle_in = round(math.cos(math.radians(slider_laser_angle.real_value-90)), 2)
        x_square_delta_increment_in = x_square_increment_in - x_square_angle_in
        y_square_delta_increment_in = y_square_increment_in - y_square_angle_in   
        refraction = True

    else:
        x_square_delta_increment_in = -round(math.sin(math.radians(slider_laser_angle.real_value-90)), 2) 
        y_square_delta_increment_in = -round(math.cos(math.radians(slider_laser_angle.real_value-90)), 2)
        refraction = False

    return x_laser_increment, y_laser_increment, x_square_delta_increment_in, y_square_delta_increment_in, refraction


def Square_function():

    x_laser_increment, y_laser_increment, x_square_delta_increment_in, y_square_delta_increment_in, refraction = Calculation()

    pygame.draw.rect(screen, white, [slider_square_x.real_value - 50, slider_square_y.real_value - 50, 100, 100])
    pygame.draw.rect(screen, black, [slider_square_x.real_value - 45, slider_square_y.real_value - 45, 90, 90])

    x = 25
    y = slider_laser_x.real_value
    square_entered = False
    square_first_face_touched = False
    square_last_face_touched = False
    square_up_face_touched = False
    square_down_face_touched = False

    while(x < screen_width):
        print(round(slider_laser_angle.real_value, 2) - 180, y_square_delta_increment_in)

        if slider_laser_angle.real_value - 180 > 0:
            y_square_delta_increment_in = -y_square_delta_increment_in

        #print(x_square_delta_increment_in, x_square_delta_increment_in, x_square_increment_in, x_square_angle_in, y_square_increment_in, y_square_angle_in)

        if slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50:
            square_entered = True

        if round(x, 0)+-1 <= slider_square_x.real_value - 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50 and not square_first_face_touched and square_entered:
            square_first_face_touched = True
            x = x + x_square_delta_increment_in
            y = y + y_square_delta_increment_in

        if square_first_face_touched:
            x = x + x_square_delta_increment_in
            y = y + y_square_delta_increment_in

        """ if round(x, 0)+-1 >= slider_square_x.real_value + 50 and slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50 and not square_last_face_touched and square_entered:
            square_last_face_touched = True
            y = y + slider_RI2.real_value
            x = x + 0
        if square_last_face_touched:
            y = y + slider_RI2.real_value
            x = x + 0

        if round(y, 0)+-1 >= slider_square_y.real_value + 50 and slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and not square_down_face_touched and square_entered:
            y = y + slider_RI2.real_value
            square_down_face_touched = True
        if square_down_face_touched:
            y = y + slider_RI2.real_value

        if round(y, 0)+-1 <= slider_square_y.real_value - 50 and slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and not square_up_face_touched and square_entered:
            y = y + slider_RI2.real_value
            square_up_face_touched = True
        if square_up_face_touched:
            y = y + slider_RI2.real_value """

        pygame.draw.line(screen, 'red', (x, y), (x + 1, y), 5)

        x = x + x_laser_increment
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

    slider_laser_angle.calculation_value(90)
    slider_laser_angle.render_header(str(round(slider_laser_angle.real_value - 180, 0)))
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

# TO ADD : 

# optimization

# the transparent square
# the transparent triangle
# a reset button

# DONE :

# the laser movement
# A window with the output angle
# In case of a reflexion !
# # add comas
# go from tkiner to pygame
# show RI and Angle on screen
# A slider to choose angle and RI
# remove the prompt to ask for angles
# fix crash !
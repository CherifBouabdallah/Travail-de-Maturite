import pygame
import math
from MyFunctions import Slider

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
'''
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
        self.negative_value = 0

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
        if self.value == 0:
            self.negative_value = 0
        if self.value < 0.5:
            self.negative_value = 1-self.value - 0.5
        if self.value > 0.5:
            self.negative_value = -self.value + 0.5

        self.negative_value = -round(self.negative_value * multiplyer, self.round)
    
        

    def draw_slider(self):
        pygame.draw.rect(screen, gray, [self.pos_x, self.pos_y, self.width, self.height])
        pygame.draw.rect(screen, white, [self.pos_x + self.value * self.width - 5, self.pos_y, 10, self.height])

    def render_header(self, header):
        self.header = Smallfont.render(header, True, black)

    def blit_header(self, align_x, align_y):
        screen.blit(self.header, (screen_width // align_x - self.header.get_width() // align_x, screen_height // align_y - self.header.get_height() // align_y))
'''
slider_RI1 = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // 10 - slider_height // 10, 0, 1, 2)
slider_RI2 = Slider(0.5, screen_width // (1.2) - slider_width // (1.2), screen_height // 10 - slider_height // 10, 0, 1, 2)
slider_angle = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // 10 - slider_height // 10, 0, 1, 2)

slider_square_x = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0)
slider_square_y = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (100/95) - slider_height // (100/95), 0, 1, 0)

slider_laser_x = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0)
slider_laser_angle = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (100/95) - slider_height // (100/95), 0, 1, 2)

def Slider_printer():
    slider_RI1.calculation_value(2)
    slider_RI1.render_header(str(slider_RI1.real_value))
    slider_RI1.draw_slider()
    slider_RI1.blit_header(4.45, 10)

    slider_RI2.calculation_value(2)
    slider_RI2.render_header(str(slider_RI2.real_value))
    slider_RI2.draw_slider()
    slider_RI2.blit_header(1.3, 10)
    
    slider_angle.calculation_value(180)
    slider_angle.render_header(str(slider_angle.real_value))
    slider_angle.draw_slider()
    slider_angle.blit_header(2, 10)

    slider_square_x.calculation_value(screen_width)
    slider_square_x.render_header(str(slider_square_x.real_value))
    slider_square_x.draw_slider()
    slider_square_x.blit_header(2, 1.11)

    slider_square_y.calculation_value(screen_height)
    slider_square_y.render_header(str(slider_square_y.real_value))
    slider_square_y.draw_slider()
    slider_square_y.blit_header(2, 1.05)

    slider_laser_x.calculation_value(screen_height)
    slider_laser_x.render_header(str(slider_laser_x.real_value))
    slider_laser_x.draw_slider()
    slider_laser_x.blit_header(4.45, 1.11)

    slider_laser_angle.calculation_value(180)
    slider_laser_angle.render_header(str(slider_laser_angle.real_value))
    slider_laser_angle.draw_slider()
    slider_laser_angle.blit_header(4.45, 1.05)

def Calculation(slider_RI1, slider_angle, slider_RI2):
    pre_calculation = ((slider_RI1.real_value * math.sin(math.radians(slider_angle.real_value))) / slider_RI2.real_value)

    if -1 <= pre_calculation <= 1:
        Angle_of_Refraction_Radians = math.asin(pre_calculation)
        Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
        Angle_of_Refraction_Degrees = round(Angle_of_Refraction_Degrees, 2)
        
    else:
        Angle_of_Refraction_Degrees = 'Reflexion'
    
    return Angle_of_Refraction_Degrees

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
                slider_laser_x.update_grabbed(mouse_x, mouse_y)
                slider_laser_angle.update_grabbed(mouse_x, mouse_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            slider_RI1.update_released()
            slider_RI2.update_released()
            slider_angle.update_released()
            slider_square_x.update_released()
            slider_square_y.update_released()
            slider_laser_x.update_released()
            slider_laser_angle.update_released()

        elif event.type == pygame.MOUSEMOTION:
            slider_RI1.update_motion(mouse_x)
            slider_RI2.update_motion(mouse_x)
            slider_angle.update_motion(mouse_x)
            slider_square_x.update_motion(mouse_x)
            slider_square_y.update_motion(mouse_x)
            slider_laser_x.update_motion(mouse_x)
            slider_laser_angle.update_motion(mouse_x)
    
    screen.fill(black)
    Slider_printer()
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
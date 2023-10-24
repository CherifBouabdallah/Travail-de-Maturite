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
gray = (60, 60, 60)

Bigfont = pygame.font.SysFont("Calibri", 72)
font = pygame.font.SysFont("Calibri", 52)
Smallfont = pygame.font.SysFont("Calibri", 22)
minifont = pygame.font.SysFont("Calibri", 16)

slider_width = 200
slider_height = 20
mouse_x = 0
mouse_y = 0
angle_of_refraction_in_header = 0



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

class Button:
    def __init__(self, text, pos_x, pos_y, width, height, font_size):
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.font_size = font_size
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self):
        pygame.draw.rect(screen, gray, self.rect)
        font = pygame.font.SysFont("Calibri", self.font_size)
        text_surface = font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

slider_RI1 = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // 10 - slider_height // 10, 0.05, 1, 5, None, 2)
slider_RI2 = Slider(0.5, screen_width // (1.2) - slider_width // (1.2), screen_height // 10 - slider_height // 10, 0.05, 1, 5, None, 2)
slider_square_x = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0, None, screen_width)
slider_square_y = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (100/95) - slider_height // (100/95), 0, 1, 0, None , screen_height)
slider_laser_pos = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0, None, screen_height)
slider_laser_angle = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (100/95) - slider_height // (100/95), 0.01, 0.99, 5, None, math.pi)
all_sliders = slider_RI1, slider_RI2, slider_square_x, slider_square_y, slider_laser_pos, slider_laser_angle


reset_button = Button("Reset Sliders", screen_width // 1.25 - 150 // 1.25, screen_height // (100/94) - 50 // (100/94), 150, 50, 28)
preset1_button = Button("Air to Glass", screen_width // 1.05 - 75 // 1.05, screen_height // (100/94) - 50 // (100/94), 75, 50, 12)




def Slider_printer(slider_RI1, slider_RI2, slider_square_x, slider_square_y, slider_laser_x, slider_laser_angle):
    slider_RI1.calculation_value(0)
    slider_RI1.render_header(str(slider_RI1.real_value))
    slider_RI1.draw_slider()
    slider_RI1.blit_header(4.45, 10)

    slider_RI2.calculation_value(0)
    slider_RI2.render_header(str(slider_RI2.real_value))
    slider_RI2.draw_slider()
    slider_RI2.blit_header(1.3, 10)

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

    slider_laser_angle.calculation_value(-math.pi/2)
    slider_laser_angle.render_header(str(round(math.degrees(slider_laser_angle.real_value), 0)))
    slider_laser_angle.draw_slider()
    slider_laser_angle.blit_header(4.45, 1.05)

def colors(slider = 1):
    if slider is None or slider < 1:
        color = (0, 0, 0)
    else:
        color = ((slider-1)*30, (slider-1)*30, (slider-1)*30)
    return color

def Square_function():
    x = 25
    y = slider_laser_pos.real_value
    laser_color = 'red'
    square_color = white
    refraction = None
    square_entered = False
    square_exited =  False
    backround_color = black

    pygame.draw.rect(screen, square_color, [slider_square_x.real_value - 50, slider_square_y.real_value - 50, 100, 100])
    pygame.draw.rect(screen, colors(slider_RI2.real_value), [slider_square_x.real_value - 45, slider_square_y.real_value - 45, 90, 90])

    x_increment_in = 0
    y_increment_in = 0
    angle_of_refraction_in = 0
    intersect = 0
    reflected = False

    x_laser_increment = round(math.cos(slider_laser_angle.real_value), 5)
    y_laser_increment = -round(math.sin(slider_laser_angle.real_value), 5)

    while(x < screen_width):

        pre_calculation_in = (slider_RI1.real_value * math.sin(slider_laser_angle.real_value) / slider_RI2.real_value) #starts the refraction calculus from out to in
        if -1 <= pre_calculation_in <= 1:
            
            angle_of_refraction_in = math.asin(pre_calculation_in) #ends the refraction calculus only if there's no reflexion
            
            x_increment_in = round(math.cos(angle_of_refraction_in), 5) #finds the increments to render an angle
            y_increment_in = -round(math.sin(angle_of_refraction_in), 5)
        
        else: #tentative de reflexion
            
            if (slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50) and (slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50) and not reflected:
                laser_color = black
                intersect = y
                reflected = True
            pygame.draw.line(screen, 'red', (slider_square_x.real_value - 50, intersect), (0, 0), 5)
            

        pre_calculation_out = (slider_RI2.real_value * math.sin(angle_of_refraction_in) / slider_RI1.real_value) #starts the refraction calculus from in to out
        if -1 <= pre_calculation_out <= 1:
            
            angle_of_refraction_out = math.asin(pre_calculation_out) #ends the refraction calculus only if there's no reflexion
            
            x_increment_out = round(math.cos(angle_of_refraction_out), 5)  #finds the increments to render an angle
            y_increment_out = -round(math.sin(angle_of_refraction_out), 5)


        if slider_RI1.real_value != slider_RI2.real_value and slider_laser_angle.real_value != 0: #checks if there is a refraction
            refraction = True
        
        if round(y, 0) == slider_square_y.real_value - 50 and slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and refraction: #checks if up face is touched and adapts the angle
            x_increment_in = round(math.cos(math.pi/2 - angle_of_refraction_in), 5)
            y_increment_in = -round(math.sin(math.pi/2 - angle_of_refraction_in), 5)

        
        if round(y, 0) == slider_square_y.real_value + 50 and slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50 and refraction: #checks if down face if touched and adapts the angle
            x_increment_in = round(math.cos(math.pi/2 - angle_of_refraction_in), 5)
            y_increment_in = -round(math.sin(math.pi/2 - angle_of_refraction_in), 5)
        
        if (slider_square_x.real_value - 50 <= x <= slider_square_x.real_value + 50) and (slider_square_y.real_value - 50 <= y <= slider_square_y.real_value + 50): #checks if we are inside of square
            square_entered = True
            #laser_color = 'green'

        if square_entered:
            if (x < slider_square_x.real_value - 50 or x > slider_square_x.real_value + 50) or (y < slider_square_y.real_value - 50 or y > slider_square_y.real_value + 50): #checks if laser exited
                square_entered = False
                square_exited = True
                #laser_color = 'blue'
                
        if not refraction: #this adjusts every increment (angle) depending on the situation
            x += x_laser_increment
            y += y_laser_increment
        
        if square_entered and refraction:
            x += x_increment_in
            y += y_increment_in
 
        if square_exited and refraction:
            x += x_increment_out
            y += y_increment_out

        else:
            x += x_laser_increment
            y += y_laser_increment

        if refraction and square_entered: #prints the angle of refraction if there is one
            angle_of_refraction_in_header = Smallfont.render(str(round(math.degrees(angle_of_refraction_in), 2)), True, white)
            screen.blit(angle_of_refraction_in_header, (screen_width // 2 - 20, screen_height // 10))
        
        angle_of_refraction_in_text = Smallfont.render('Angle de réfraction', True, white) #prints the angle of refraction text
        screen.blit(angle_of_refraction_in_text, (screen_width // 2 - 70, screen_height // 20))
        pygame.draw.line(screen, laser_color, (x, y), (x + 1, y), 5)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                for slider in all_sliders:
                    slider.update_grabbed(event, mouse_x, mouse_y)

                if reset_button.is_clicked((mouse_x, mouse_y)):    
                    for slider in all_sliders:
                        slider.value = 0.5

                if preset1_button.is_clicked((mouse_x, mouse_y)):    
                    for slider in all_sliders:
                        slider.value = 0.5
                    slider_RI2.value = 0.755
                    slider_laser_angle.value = 0.32
                    slider_laser_pos.value = 0.085

        elif event.type == pygame.MOUSEBUTTONUP:
            for slider in all_sliders:
                slider.update_released(event)

        elif event.type == pygame.MOUSEMOTION:
            for slider in all_sliders:
                slider.update_motion(event, mouse_x)

    screen.fill(colors(slider_RI1.real_value))
    Slider_printer(slider_RI1, slider_RI2, slider_square_x, slider_square_y, slider_laser_pos, slider_laser_angle)
    Square_function()
    reset_button.draw()
    preset1_button.draw()
    pygame.display.update()
    pygame.time.Clock().tick(60)
    
pygame.quit()
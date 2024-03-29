import pygame
import math

#initialization of pygame
pygame.init()
caption = "Refraction Simulator"
screen_width, screen_height = 1400, 980 #Definition of the window size
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

#Definition of variables
slider_width = 200
slider_height = 20
mouse_x = 0
mouse_y = 0
angle_of_refraction_in_header = 0


# creation of the sliders by defining a class
class Slider:
    #Definition of the sliders attributes
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

    #definition of the sliders multiples functions
    def update_grabbed(self, event, mouse_x, mouse_y):
        mouse_x, mouse_y = event.pos
        if self.pos_x <= mouse_x <= self.pos_x + self.width and self.pos_y <= mouse_y <= self.pos_y + self.height:
            self.grabbed = True

    def update_released(self, event): #this function is used to stop the slider from moving when the mouse is released
        if event.button == 1:
            self.grabbed = False

    def update_motion(self, event, mouse_x): #this function is used to move the slider
        if self.grabbed:
            mouse_x, _ = event.pos
            self.value = (mouse_x - self.pos_x) / self.width
            self.value = max(self.min_value, min(self.value, self.max_value))

    def calculation_value(self, addon): #this function is used to calculate the real value of the slider (the default value is between 0 and 1)
        self.real_value = round(self.value * self.multiplyer + addon, self.round)
        self.neg_value = -round(self.value * self.multiplyer + addon, self.round)
    
    def draw_slider(self): #this function is used to draw the slider
        pygame.draw.rect(screen, gray, [self.pos_x, self.pos_y, self.width, self.height])
        pygame.draw.rect(screen, white, [self.pos_x + self.value * self.width - 5, self.pos_y, 10, self.height])

    def render_header(self, header): #this function is used to render the header of the slider
        self.header = Smallfont.render(header, True, white)

    def blit_header(self, align_x, align_y): #this function is used to print the header of the slider
        header_x = self.pos_x + self.value * self.width - self.header.get_width() // 2
        header_y = self.pos_y - self.header.get_height()  # Adjust the vertical position as needed
        screen.blit(self.header, (header_x, header_y))

    def blit_text(self, text, offset = -45): #this function is used to print the name of the slider
        self.text = Smallfont.render(text, True, white)
        screen.blit(self.text, (self.pos_x, self.pos_y + offset))

#creation of the buttons by defining a class
class Button:
    def __init__(self, text, pos_x, pos_y, width, height, font_size): #definition of the buttons attributes
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.font_size = font_size
    
    def is_clicked(self, mouse_pos):  #this function is used to check if the button is clicked
        return self.rect.collidepoint(mouse_pos)
    
    def draw(self): #this function is used to draw the button
        pygame.draw.rect(screen, gray, self.rect)
        font = pygame.font.SysFont("Calibri", self.font_size)
        text_surface = font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


#creation of the sliders and buttons by using the classes created before

slider_RI1 = Slider(0, screen_width // 6 - slider_width // 6, screen_height // 10 - slider_height // 10, 0, 1, 5, None, 1)
slider_RI2 = Slider(0, screen_width // (1.2) - slider_width // (1.2), screen_height // 10 - slider_height // 10, 0, 1, 5, None, 1)
slider_square_x = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0, None, screen_width)
slider_square_y = Slider(0.5, screen_width // 2 - slider_width // 2, screen_height // (100/95) - slider_height // (100/95), 0, 1, 0, None , screen_height)
slider_laser_pos = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (10/9) - slider_height // (10/9), 0, 1, 0, None, screen_height)
slider_laser_angle = Slider(0.5, screen_width // 6 - slider_width // 6, screen_height // (100/95) - slider_height // (100/95), 0.01, 0.99, 5, None, math.pi)
all_sliders = slider_RI1, slider_RI2, slider_square_x, slider_square_y, slider_laser_pos, slider_laser_angle

reset_button = Button("Reset Sliders", screen_width // 1.25 - 150 // 1.25, screen_height // (100/94) - 50 // (100/94), 150, 50, 28)
preset1_button = Button("Air to Glass", screen_width // 1.1 - 75 // 1.1, screen_height // (100/94) - 50 // (100/94), 150, 50, 28)




def Slider_printer(slider_RI1, slider_RI2, slider_square_x, slider_square_y, slider_laser_pos, slider_laser_angle): #function that creates the different sliders with the functions created before
    slider_RI1.calculation_value(1)
    slider_RI1.render_header(str(slider_RI1.real_value))
    slider_RI1.draw_slider()
    slider_RI1.blit_text('    Refraction Index 1')

    slider_RI2.calculation_value(1)
    slider_RI2.render_header(str(slider_RI2.real_value))
    slider_RI2.draw_slider()
    slider_RI2.blit_text('    Refraction Index 2')

    slider_square_x.calculation_value(0)
    slider_square_x.render_header(str(slider_square_x.real_value))
    slider_square_x.draw_slider()
    slider_square_x.blit_text(' Square position axis x')

    slider_square_y.calculation_value(0)
    slider_square_y.render_header(str(slider_square_y.real_value))
    slider_square_y.draw_slider()
    slider_square_y.blit_text(' Square position axis y', 25)

    slider_laser_pos.calculation_value(0)
    slider_laser_pos.render_header(str(slider_laser_pos.real_value))
    slider_laser_pos.draw_slider()
    slider_laser_pos.blit_text('  Laser position axis y')

    slider_laser_angle.calculation_value(-math.pi/2)
    slider_laser_angle.render_header(str(round(math.degrees(slider_laser_angle.real_value), 0)))
    slider_laser_angle.draw_slider()
    slider_laser_angle.blit_text('          Laser angle', 25)

def colors(slider = 1): #function that creates the different colors depending on the refraction index
    if slider is None or slider < 1:
        color = (0, 0, 0)
    else:
        color = ((slider-1)*30, (slider-1)*30, (slider-1)*30)
    return color

def Square_function(): #function that creates the square and the laser and makes them move
    #definition of the variables of the square and the laser
    x = 25
    y = slider_laser_pos.real_value
    laser_color = 'red'
    laser_thickness = 5
    square_color = white
    refraction = None
    reflexion = None
    #definition of the state of the square and the laser
    square_entered = False
    square_exited =  False
    up_face_touched = False
    down_face_touched = False
    up_face_touched_out = False
    down_face_touched_out = False

    #creation of the square 
    pygame.draw.rect(screen, square_color, [slider_square_x.real_value - 75, slider_square_y.real_value - 75, 150, 150])
    pygame.draw.rect(screen, colors(slider_RI2.real_value), [slider_square_x.real_value - 70, slider_square_y.real_value - 70, 140, 140])

    #definition of the increments that will allow us to manipulate the angle of the laser
    x_increment_in = 0
    y_increment_in = 0
    x_increment_out = 0
    y_increment_out = 0
    angle_of_refraction_in = 0
    angle_of_refraction_out = 0

    #calculation of 2 of these increments
    x_laser_increment = round(math.cos(slider_laser_angle.real_value), 5)
    y_laser_increment = round(math.sin(slider_laser_angle.real_value), 5)

    if slider_RI1.real_value != slider_RI2.real_value and slider_laser_angle.real_value != 0: #checks if there is a refraction
        refraction = True

    while(x < screen_width): #this loop is used to make the laser move according to the angle of the laser and the refraction index
        
        pre_calculation_in = (slider_RI1.real_value * math.sin(slider_laser_angle.real_value) / slider_RI2.real_value) #starts the refraction calculus from out to in
        if -1 <= pre_calculation_in <= 1: #if the refraction index is too high, the laser will not refract this is why there is this condition
            reflexion = False
            angle_of_refraction_in = math.asin(pre_calculation_in) #ends the refraction calculus only if there's no reflexion
            x_increment_in = round(math.cos(angle_of_refraction_in), 5) 
            y_increment_in = round(math.sin(angle_of_refraction_in), 5)

            if slider_square_y.real_value - 74.5 >= round(y, 0) >= slider_square_y.real_value - 75.5 and slider_square_x.real_value - 75 <= x <= slider_square_x.real_value + 75 and refraction and not down_face_touched and not up_face_touched: #checks if up face is touched and adapts the angle
                x_increment_in = round(math.sin(angle_of_refraction_in), 5) #adapts the angle if the up face is touched going in the square
                y_increment_in = round(math.cos(angle_of_refraction_in), 5)
                up_face_touched = True

            if up_face_touched:
                x_increment_in = round(math.sin(angle_of_refraction_in), 5) #keeps the same angle if the up face going in the square is touched until something else happens
                y_increment_in = round(math.cos(angle_of_refraction_in), 5)

        
            if slider_square_y.real_value + 74.5 <= round(y, 0) <= slider_square_y.real_value + 75.5 and slider_square_x.real_value - 75 <= x <= slider_square_x.real_value + 75 and refraction and not up_face_touched and not down_face_touched: #checks if down face if touched and adapts the angle
                x_increment_in = -round(math.sin(angle_of_refraction_in), 5)
                y_increment_in = -round(math.cos(angle_of_refraction_in), 5) #adapts the angle if the down face is touched going in of the square
                down_face_touched = True

            if down_face_touched:
                x_increment_in = -round(math.sin(angle_of_refraction_in), 5) #keeps the same angle if the down face going in the square is touched until something else happens
                y_increment_in = -round(math.cos(angle_of_refraction_in), 5)
        
        else: #if the refraction index is too high, the laser will not refract and reflect instead
            if square_entered:
                reflexion = True
                laser_thickness = 0

        if reflexion and square_entered: #this prints the reflexion of the laser
            reflexion = True
            laser_thickness = 0
            distance_reflexion = 0          

            #reflexion values to not create any crashes              
            x_increment_in = 1
            y_increment_in = 0
            x_increment_out = 1
            y_increment_out = 0
            
            #some calculations to find the reflexion of the laser depending on the position of the square and the laser
            if slider_laser_pos.real_value > slider_square_y.real_value:
                distance_reflexion = slider_laser_pos.real_value - 2*(slider_laser_pos.real_value - slider_square_y.real_value)

            if slider_laser_pos.real_value < slider_square_y.real_value:
                distance_reflexion = 2*(slider_square_y.real_value - slider_laser_pos.real_value) + slider_laser_pos.real_value

            pygame.draw.line(screen, 'red', (slider_square_x.real_value-75, slider_square_y.real_value), (25, distance_reflexion), 5) #prints the reflexion of the laser



        pre_calculation_out = (slider_RI2.real_value * math.sin(angle_of_refraction_in) / slider_RI1.real_value) #starts the refraction calculus from in to out

        if -1 <= pre_calculation_out <= 1:

            angle_of_refraction_out = math.asin(pre_calculation_out) #ends the refraction calculus only if there's no reflexion
            

            x_increment_out = round(math.cos(angle_of_refraction_out), 5) #finds the increments to render an angle if everything is normal
            y_increment_out = round(math.sin(angle_of_refraction_out), 5) 

            if slider_square_y.real_value - 74.5 >= round(y, 0) >= slider_square_y.real_value - 75.5 and slider_square_x.real_value - 75 <= x <= slider_square_x.real_value + 75 and refraction and square_entered and not reflexion: #checks if up face is touched and adapts the angle

                x_increment_out = -round(math.sin(angle_of_refraction_out), 5) #adapts the angle if the up face is touched going out of the square
                y_increment_out = round(math.cos(angle_of_refraction_out), 5)
                up_face_touched_out = True

            
            if up_face_touched_out:
                x_increment_out = -round(math.sin(angle_of_refraction_out), 5) #keeps the same angle if the up face is touched until something else happens going out of the square
                y_increment_out = round(math.cos(angle_of_refraction_out), 5)


            if slider_square_y.real_value + 74.5 <= round(y, 0) <= slider_square_y.real_value + 75.5 and slider_square_x.real_value - 75 <= x <= slider_square_x.real_value + 75 and refraction and square_entered and not reflexion: #checks if down face if touched and adapts the angle

                x_increment_out = round(math.sin(angle_of_refraction_out), 5) #adapts the angle if the down face is touched going out of the square
                y_increment_out = -round(math.cos(angle_of_refraction_out), 5)
                down_face_touched_out = True

            
            if down_face_touched_out:
                x_increment_out = round(math.sin(angle_of_refraction_out), 5) #keeps the same angle if the down face is touched until something else happens going out of the square
                y_increment_out = -round(math.cos(angle_of_refraction_out), 5)


        if (slider_square_x.real_value - 75 <= x <= slider_square_x.real_value + 75) and (slider_square_y.real_value - 75 <= y <= slider_square_y.real_value + 75): #checks if we are inside of square
            square_entered = True

        if square_entered:
            if (x < slider_square_x.real_value - 75 or x > slider_square_x.real_value + 75) or (y < slider_square_y.real_value - 75 or y > slider_square_y.real_value + 75): #checks if laser exited
                square_entered = False
                square_exited = True
                
        if not refraction: #these lines chooses the increment (angle) depending on the situation
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

        if up_face_touched and square_exited: #resets the variables if the up face is touched and the laser exited
            up_face_touched = False

        if down_face_touched and square_exited:
            down_face_touched = False

        if refraction and square_entered: #prints the angle of refraction number if there is one
            angle_of_refraction_in_header = Smallfont.render(str(round(math.degrees(angle_of_refraction_in), 2)), True, white)
            screen.blit(angle_of_refraction_in_header, (screen_width // 2 - 20, screen_height // 10))
        
        angle_of_refraction_in_text = Smallfont.render('Angle de réfraction première collision uniquement', True, white) #prints the angle of refraction text
        screen.blit(angle_of_refraction_in_text, (screen_width // 2 - 220, screen_height // 20))
        
        if not reflexion:
            pygame.draw.line(screen, laser_color, (x, y), (x + 1, y), laser_thickness) #prints the laser


#main loop
done = False
while not done:
    for event in pygame.event.get(): #this loop is used to check if the mouse is clicked, if the sliders are clicked, if the reset button is clicked and if the preset button is clicked
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                for slider in all_sliders:
                    slider.update_grabbed(event, mouse_x, mouse_y) #this loop is used to check if the sliders are clicked

                if reset_button.is_clicked((mouse_x, mouse_y)): #this loop is used to check if the reset button is clicked
                    for slider in all_sliders:
                        slider.value = 0.5
                    slider_RI2.value = 0
                    slider_RI1.value = 0

                if preset1_button.is_clicked((mouse_x, mouse_y)): #this loop is used to check if the preset button is clicked
                    for slider in all_sliders:
                        slider.value = 0.5
                    slider_RI2.value = 0.51
                    slider_RI1.value = 0
                    slider_laser_angle.value = 0.66
                    slider_laser_pos.value = 0.1

        elif event.type == pygame.MOUSEBUTTONUP: #this loop is used to check if the mouse is released 
            for slider in all_sliders:
                slider.update_released(event)

        elif event.type == pygame.MOUSEMOTION: #this loop is used to check if the mouse is moving
            for slider in all_sliders:
                slider.update_motion(event, mouse_x)

    screen.fill(colors(slider_RI1.real_value)) #this fills the screen with the color of the refraction index

    Slider_printer(slider_RI1, slider_RI2, slider_square_x, slider_square_y, slider_laser_pos, slider_laser_angle) #this prints the sliders
    
    for slider in all_sliders:
        slider.blit_header(1, 1)  # Adjust the values as the sliders move

    #this calls the functions created before
    Square_function()
    reset_button.draw()
    preset1_button.draw()
    pygame.display.update()
    pygame.time.Clock().tick(60)
    
pygame.quit()
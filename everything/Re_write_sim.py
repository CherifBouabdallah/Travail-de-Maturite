import pygame
import math

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

class Slider:
    def __init__(self, value, pos_x, pos_y):
        self.value = value
        self.grabbed = False
        self.width = slider_width
        self.height = slider_height
        self.pos_x = pos_x
        self.pos_y = pos_y

    def update_grabbed(self, mouse_x, mouse_y):
        if self.pos_x <= mouse_x <= self.pos_x + self.width and self.pos_y <= mouse_y <= self.pos_y + self.height:
            self.grabbed = True
        
    def update_released(self):
        if event.button == 1:
            self.grabbed = False

    def update_motion(self, mouse_x, mouse_y):
        if self.grabbed:
            mouse_x, mouse_y = event.pos
            self.value = (mouse_x - self.pos_x) / self.width
            self.value = max(0.01, min(self.value, 1))

    def round_result(self):
        self.calculation_value = round(self.value * 2, 2)

    def draw_slider(self):
        pygame.draw.rect(screen, gray, [self.pos_x, self.pos_y, self.width, self.height])
        pygame.draw.rect(screen, white, [self.pos_x + self.value * self.width - 5, self.pos_y, 10, self.height])

    def print_header(self):
        screen.blit(Angle_of_Refraction_Display_Header, (screen_width // 2 - Angle_of_Refraction_Display_Header.get_width() // 2, screen_height // 2.5 - Angle_of_Refraction_Display_Header.get_height() // 2.5))



slider_IR1 = Slider(0.5, (screen_width // 8 - slider_width // 8), (screen_height // 5 - slider_height // 5))

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                slider_IR1.update_grabbed(mouse_x, mouse_y)
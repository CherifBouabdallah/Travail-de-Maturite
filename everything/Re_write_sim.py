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
        self.header = 0
        self.align_x = 0
        self.align_y = 0
        self.start_value = 0

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
            self.value = max(0, min(self.value, 1))

    def round_result(self, multiplyer):
        self.calculation_value = round(self.value * multiplyer, 2)

    def draw_slider(self):
        pygame.draw.rect(screen, gray, [self.pos_x, self.pos_y, self.width, self.height])
        pygame.draw.rect(screen, white, [self.pos_x + self.value * self.width - 5, self.pos_y, 10, self.height])

    def render_header(self, header):
        self.header = font.render(header, True, (255, 255, 255))

    def blit_header(self, align_x, align_y):
        screen.blit(self.header, (screen_width // align_x - self.header.get_width() // align_x, screen_height // align_y - self.header.get_height() // align_y))

'''
class Calculation:
    def __init__(self, ):
'''


slider1 = Slider(0.5, screen_width // 5 - slider_width // 5, screen_height // 2 - slider_width // 2)



mouse_x = 0
mouse_y = 0

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                slider1.update_grabbed(mouse_x, mouse_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            slider1.update_released()

        elif event.type == pygame.MOUSEMOTION:
            slider1.update_motion(mouse_x)

    screen.fill(black)
    slider1.render_header(str(slider1.value))
    slider1.draw_slider()
    slider1.blit_header(5, 2)


    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
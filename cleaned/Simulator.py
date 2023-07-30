import math
import pygame

#A few definitions to make everything easier

Angle_of_Refraction_Degrees = 1
Angle_of_Arrival_Degrees = 1
Refraction_index_1 = 1
Refraction_index_2 = 1
First_Part_of_Calculation = 0
Angle_of_Refraction_Radians = 1
Angle_of_Arrival_Radians = 1

#Create window


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

# Set up the slider

slider_RI1_width = slider_RI2_width = slider_AOA_width = 200
slider_RI1_height = slider_RI2_height = slider_AOA_height = 20
slider_RI1_value = slider_RI2_value = slider_AOA_value = 0.5
slider_RI1_grabbed = slider_RI2_grabbed = slider_AOA_grabbed = False


slider_RI1_x = (screen_width // 8 - slider_RI2_width // 8)
slider_RI1_y = ((screen_height // 5 - slider_RI2_height // 5))
slider_RI2_x = (screen_width // (8/7) - slider_RI2_width // (8/7))
slider_RI2_y = ((screen_height // 5 - slider_RI2_height // 5))
slider_AOA_x = (screen_width // 2 - slider_AOA_width // 2)
slider_AOA_y = ((screen_height // 5 - slider_AOA_height // 5))

Angle_of_Refraction_Display_Header = font.render(("Angle réfracté"), True,  white)
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

    screen.fill(black)

    Refraction_index_2 = round(slider_RI2_value * 2, 2)
    Refraction_index_1 = round(slider_RI1_value * 2, 2)
    Angle_of_Arrival_Degrees = round(slider_AOA_value * 90, 2)

    Refraction_index_2_text = Smallfont.render(str(Refraction_index_2), True, white)
    Refraction_index_1_text = Smallfont.render(str(Refraction_index_1), True, white)
    Angle_of_Arrival_Degrees_text = Smallfont.render(str(Angle_of_Arrival_Degrees), True, white)
    Angle_of_Refraction_Degrees_text = font.render(str(Angle_of_Refraction_Degrees), True, white)

    #Shows things on screen

    pygame.draw.rect(screen, gray, [slider_RI2_x, slider_RI2_y, slider_RI2_width, slider_RI2_height])
    pygame.draw.rect(screen, white, [slider_RI2_x + slider_RI2_value * slider_RI2_width - 5, slider_RI2_y, 10, slider_RI2_height])

    pygame.draw.rect(screen, gray, [slider_RI1_x, slider_RI1_y, slider_RI1_width, slider_RI1_height])
    pygame.draw.rect(screen, white, [slider_RI1_x + slider_RI1_value * slider_RI1_width - 5, slider_RI1_y, 10, slider_RI1_height])

    pygame.draw.rect(screen, gray, [slider_AOA_x, slider_AOA_y, slider_AOA_width, slider_AOA_height])
    pygame.draw.rect(screen, white, [slider_AOA_x + slider_AOA_value * slider_AOA_width - 5, slider_AOA_y, 10, slider_AOA_height])

    screen.blit(Angle_of_Refraction_Display_Header, (screen_width // 2 - Angle_of_Refraction_Display_Header.get_width() // 2, screen_height // 2.5 - Angle_of_Refraction_Display_Header.get_height() // 2.5))
    screen.blit(Angle_of_Arrival_Display_Header, (screen_width // 2 - Angle_of_Arrival_Display_Header.get_width() // 2, screen_height // 10 - Angle_of_Arrival_Display_Header.get_height() // 10))
    screen.blit(Refraction_index_1_Display_Header, (screen_width // 8 - Refraction_index_1_Display_Header.get_width() // 8, screen_height // 10 - Refraction_index_1_Display_Header.get_height() // 10))
    screen.blit(Refraction_index_2_Display_Header, (screen_width // (8/7) - Refraction_index_2_Display_Header.get_width() // (8/7), screen_height // 10 - Refraction_index_2_Display_Header.get_height() // 10))
    

    screen.blit(Refraction_index_2_text, [slider_RI2_x - Refraction_index_2_text.get_width() - 10, slider_RI2_y + slider_RI2_height // 2 - Refraction_index_2_text.get_height() // 2])
    screen.blit(Angle_of_Refraction_Degrees_text, (screen_width // 2 - Refraction_index_2_text.get_width() // 2, screen_height // 2 - Refraction_index_2_text.get_height() // 2))
    screen.blit(Refraction_index_1_text, [slider_RI1_x - Refraction_index_1_text.get_width() - 10, slider_RI1_y + slider_RI1_height // 2 - Refraction_index_1_text.get_height() // 2])
    screen.blit(Angle_of_Arrival_Degrees_text, [slider_AOA_x - Angle_of_Arrival_Degrees_text.get_width() - 10, slider_AOA_y + slider_AOA_height // 2 - Angle_of_Arrival_Degrees_text.get_height() // 2])
   


    First_Part_of_Calculation = ((Refraction_index_1 * math.sin(math.radians(Angle_of_Arrival_Degrees))) / Refraction_index_2)

    if -1 <= First_Part_of_Calculation <= 1:
        Angle_of_Refraction_Radians = math.asin(First_Part_of_Calculation)
        Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
        Angle_of_Refraction_Degrees = round(Angle_of_Refraction_Degrees, 2)
        
    else:
        Angle_of_Refraction_Degrees = 'Reflexion'
   
    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()






# TO ADD : 

# optimization
#1
# the laser
# the transparent objects

# DONE :

# A window with the output angle
# In case of a reflexion !
# # add comas
# go from tkiner to pygame
# show RI and Angle on screen
# A slider to choose angle and RI
# remove the prompt to ask for angles
# fix crash !
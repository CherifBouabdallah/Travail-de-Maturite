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
#test
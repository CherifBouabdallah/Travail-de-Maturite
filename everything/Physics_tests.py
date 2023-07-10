'''

import math

# Define a value for a
a = 0.5

# Compute the sine of a using the sin() function
sine = math.sin(a)
print(f"sin({a}) = {sine}")

# Compute the inverse sine of a using the asin() function
inverse_sine = math.asin(a)
print(f"sin^-1({a}) = {inverse_sine}")


import pygame

# Initialize Pygame
pygame.init()

caption = "Refraction Simulator"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(caption)

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define font and text
font = pygame.font.SysFont("Arial", 72)
text = font.render("Hello, World!", True,  white)

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the screen with black
    screen.fill(black)

    # Draw the text
    screen.blit(text, (800 // 2 - text.get_width() // 2, 600 // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()




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
    Angle_of_Refraction_Degrees = ('Reflexion')


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




'''

import math
import pygame


Angle_of_Arrival_Degrees = input("Donne moi un angle d'arrivée : ")
Angle_of_Arrival_Degrees = float(Angle_of_Arrival_Degrees)

Angle_of_Arrival_Radians = math.radians(Angle_of_Arrival_Degrees)

Refraction_index_1 = input("Donne moi l'indice de réfraction du milieu 1 (air = 1; eau = 1.333; plexiglass = 1.51) : ")
Refraction_index_1 = float(Refraction_index_1)

Refraction_index_2 = input("Donne moi l'indice de réfraction du milieu 2 (air = 1; eau = 1.333; plexiglass = 1.51) : ")
Refraction_index_2 = float(Refraction_index_2)





First_Part_of_Calculation = ((Refraction_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refraction_index_2)

if -1 <= First_Part_of_Calculation <= 1:
    Angle_of_Refraction_Radians = math.asin((Refraction_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refraction_index_2)

    Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
    Angle_of_Refraction_Degrees_Rounded = round(Angle_of_Refraction_Degrees, 2)
else:
    Angle_of_Refraction_Degrees_Rounded = ('Reflexion')
    Angle_of_Refraction_Degrees = ('Reflexion')




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

slider_RI1_width = 200
slider_RI1_height = 20
slider_RI1_x = (screen_width // 8 - slider_RI2_width // 8)
slider_RI1_y = ((screen_height // 5 - slider_RI2_height // 5))
slider_RI1_value = 0.5
slider_RI1_grabbed = False

slider_AOA_width = 200
slider_AOA_height = 20
slider_AOA_x = (screen_width // 2 - slider_AOA_width // 2)
slider_AOA_y = ((screen_height // 5 - slider_AOA_height // 5))
slider_AOA_value = 0.5
slider_AOA_grabbed = False



Angle_of_Refraction_Display = Bigfont.render((str(Angle_of_Refraction_Degrees)), True,  white)
Angle_of_Arrival_Display = font.render((str(Angle_of_Arrival_Degrees)), True,  white)
Refraction_index_1_Display = font.render((str(Refraction_index_1)), True,  white)
Refraction_index_2_Display = font.render((str(Refraction_index_2)), True,  white)

Angle_of_Refraction_Display_Header = font.render((str("Angle réfracté")), True,  white)
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

    if -1 <= First_Part_of_Calculation <= 1:
        Angle_of_Refraction_Radians = math.asin((Refraction_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refraction_index_2)

        Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)
    else:
        Angle_of_Refraction_Degrees = ('Reflexion')

    screen.fill(black)

    Refraction_index_2 = round(slider_RI2_value * 2, 2)
    Refraction_index_1 = round(slider_RI1_value * 2, 2)
    Angle_of_Arrival_Radians = round(slider_AOA_value * 90, 2)
    
    result = round(Angle_of_Refraction_Degrees, 2)

    Refraction_index_2_text = Smallfont.render(str(Refraction_index_2), True, white)
    Refraction_index_1_text = Smallfont.render(str(Refraction_index_1), True, white)
    Angle_of_Arrival_Radians_text = Smallfont.render(str(Angle_of_Arrival_Radians), True, white)
    result_text = font.render(str(result), True, white)

    pygame.draw.rect(screen, gray, [slider_RI2_x, slider_RI2_y, slider_RI2_width, slider_RI2_height])
    pygame.draw.rect(screen, white, [slider_RI2_x + slider_RI2_value * slider_RI2_width - 5, slider_RI2_y, 10, slider_RI2_height])

    pygame.draw.rect(screen, gray, [slider_RI1_x, slider_RI1_y, slider_RI1_width, slider_RI1_height])
    pygame.draw.rect(screen, white, [slider_RI1_x + slider_RI1_value * slider_RI1_width - 5, slider_RI1_y, 10, slider_RI1_height])

    pygame.draw.rect(screen, gray, [slider_AOA_x, slider_AOA_y, slider_AOA_width, slider_AOA_height])
    pygame.draw.rect(screen, white, [slider_AOA_x + slider_AOA_value * slider_AOA_width - 5, slider_AOA_y, 10, slider_AOA_height])


    #Shows things on screen

    screen.blit(Angle_of_Refraction_Display_Header, (screen_width // 2 - Angle_of_Refraction_Display_Header.get_width() // 2, screen_height // 2.5 - Angle_of_Refraction_Display_Header.get_height() // 2.5))
    screen.blit(Angle_of_Arrival_Display_Header, (screen_width // 2 - Angle_of_Arrival_Display_Header.get_width() // 2, screen_height // 10 - Angle_of_Arrival_Display_Header.get_height() // 10))
    screen.blit(Refraction_index_1_Display_Header, (screen_width // 8 - Refraction_index_1_Display_Header.get_width() // 8, screen_height // 10 - Refraction_index_1_Display_Header.get_height() // 10))
    screen.blit(Refraction_index_2_Display_Header, (screen_width // (8/7) - Refraction_index_2_Display_Header.get_width() // (8/7), screen_height // 10 - Refraction_index_2_Display_Header.get_height() // 109))
    

    screen.blit(Refraction_index_2_text, [slider_RI2_x - Refraction_index_2_text.get_width() - 10, slider_RI2_y + slider_RI2_height // 2 - Refraction_index_2_text.get_height() // 2])
    screen.blit(result_text, (screen_width // 2 - Refraction_index_2_Display.get_width() // 2, screen_height // 2 - Refraction_index_2_Display.get_height() // 2))

    screen.blit(Refraction_index_1_text, [slider_RI1_x - Refraction_index_1_text.get_width() - 10, slider_RI1_y + slider_RI1_height // 2 - Refraction_index_1_text.get_height() // 2])
    screen.blit(result_text, (screen_width // 2 - Refraction_index_1_Display.get_width() // 2, screen_height // 2 - Refraction_index_1_Display.get_height() // 2))   

    screen.blit(Angle_of_Arrival_Radians_text, [slider_AOA_x - Angle_of_Arrival_Radians_text.get_width() - 10, slider_AOA_y + slider_AOA_height // 2 - Angle_of_Arrival_Radians_text.get_height() // 2])
    screen.blit(result_text, (screen_width // 2 - Angle_of_Arrival_Display.get_width() // 2, screen_height // 2 - Angle_of_Arrival_Display.get_height() // 2))   
   
   
   
   
   
    pygame.display.update()
    pygame.time.Clock().tick(30)

pygame.quit()











# TO ADD : 

# remove the prompt to ask !
# the laser
# the transparent objects

# DONE :
# A window with the output angle
# In case of a reflexion !
# # add comas
# go from tkiner to pygame
# show RI and Angle on screen
# A slider to choose angle and RI
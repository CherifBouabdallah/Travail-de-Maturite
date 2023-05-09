import math
import pygame

#Asking for things

Angle_of_Arrival_Degrees = input("Donne moi un angle d'arrivée : ")
Angle_of_Arrival_Degrees = float(Angle_of_Arrival_Degrees)

Angle_of_Arrival_Radians = math.radians(Angle_of_Arrival_Degrees)

Refracion_index_1 = input("Donne moi l'indice de réfraction du milieu 1 (air = 1; eau = 1,333; plexiglass = 1,51) : ")
Refracion_index_1 = float(Refracion_index_1)

Refracion_index_2 = input("Donne moi l'indice de réfraction du milieu 2 (air = 1; eau = 1,333; plexiglass = 1,51) : ")
Refracion_index_2 = float(Refracion_index_2)

#The fun part !

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
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(caption)

black = (0, 0, 0)
white = (255, 255, 255)

font = pygame.font.SysFont("Calibri", 72)
text = font.render((str(Angle_of_Refraction_Degrees_Rounded)), True,  white)

# Main Loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(black)

    screen.blit(text, (800 // 2 - text.get_width() // 2, 600 // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.Clock().tick(30)

pygame.quit()



# TO ADD : 

# go from tkiner to pygame
# A slider to choose angle and RI
# the laser
# the transparent objects

# DONE :
# A window with the output angle
# In case of a reflexion !
# # add comas



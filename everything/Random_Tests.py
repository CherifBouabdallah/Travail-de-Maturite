'''
import tkinter as tk

# create a new window
window = tk.Tk()

# set the window size
window.geometry("800x600")

# set the window background color to black
window.configure(bg="black")

# set the font and text
font = ("Arial", 36)
text = "Hello, World!"

# create a label with the text
label = tk.Label(window, text=text, font=font, fg="white", bg="black")

# center the label in the window
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# run the window loop
window.mainloop()


# ask for two numbers with commas
number1_input = input("Enter the first number with commas: ")
number2_input = input("Enter the second number with commas: ")

# remove commas from the input strings
number1_input = number1_input.replace(",", "")
number2_input = number2_input.replace(",", "")

# convert the input strings to floats and perform the calculation
result = float(number1_input) + float(number2_input)

# print the result
print(result)
'''


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
    





#print(((Refracion_index_1 * math.sin(Angle_of_Arrival_Radians)) / Refracion_index_2))

#Create window !

pygame.init()

Black = (0,0,0)
White = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simulator Refraction')
screen.fill(Black)
done = False


'''
while True:
   for event in pygame.event.get():
      screen.fill(Black)
      if event.type == pygame.QUIT:
        font = pygame.font.SysFont("Arial", 36)
    txtsurf = font.render("Hello, World", True, White)
    screen.blit(txtsurf,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
pygame.display.update()
'''

while not done:
   for event in pygame.event.get():
      screen.fill(Black)
      if event.type == pygame.QUIT:
         done = True
      font = pygame.font.SysFont("Arial", 36)
   txtsurf = font.render(str(Angle_of_Refraction_Degrees_Rounded), True, White)
   screen.blit(txtsurf,(400 - txtsurf.get_width() // 2, 300 - txtsurf.get_height() // 2))
   pygame.display.update()

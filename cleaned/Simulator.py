import math

#Asking for things

Angle_of_Arrival_Degrees = input("Donne moi un angle d'arivée : ")
Angle_of_Arrival_Degrees = int(Angle_of_Arrival)
Angle_of_Arrival_Radians = math.radians(Angle_of_Arrival_Degrees)

Refracion_index_1 = input("Donne moi l'indice de réfraction du milieu 1 (air = 1; eau = 1,333; plexiglass = 1,51) : ")
Refracion_index_1 = int(Refracion_index_1)

Refracion_index_2 = input("Donne moi l'indice de réfraction du milieu 2 (air = 1; eau = 1,333; plexiglass = 1,51) : ")
Refracion_index_2 = int(Refracion_index_2)

#The fun part !

Angle_of_Refraction_Radians = math.asin((Refracion_index_1 * math.sin(Angle_of_Arrival)) / Refracion_index_2)
Angle_of_Refraction_Degrees = math.degrees(Angle_of_Refraction_Radians)

print(f"l'angle réfléchi est de : {Angle_of_Refraction_Degrees}")




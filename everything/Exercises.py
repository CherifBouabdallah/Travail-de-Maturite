'''
name = input('Quel est votre prénom:')
print('Bonjour', name, 'avez-vous passé une bonne journée ?')

date = input('Quel est votre année de naissance : ')
date = int(date)
print ('Cette année, vous allez avoir', 2023-date,'ans !')


h = input('Donnez moi la hauteur d\'un cylindre en mètres:')
r = input("Donnez moi le rayon d'un cylindre en mètres:")

h = int(h)
r = int(r)

print('Le volume du cylindre est : ')



q = input('Quel est le nom de notre planète ? : ')
if q == ('terre'):
    print('bien.')
    
elif q == ('Terre'):
    
    print('bien. avec la majuscule en plus :)')
else:
    print('tu est nul')



while True:
    n = input('donne moi un nombre entre 1 et 5 : ')
    n = int(n)
    if 1 <= n <= 5:
        print("bien.")
    else:
        print("c'est mal")

'''


while True:
    a = input('donne moi ton age : ')
    a = int(a)
    if  a <= 18:
        print("tu dois grandir !")
    else:
        print("+18ans")

#test


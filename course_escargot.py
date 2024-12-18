import random, time, sys, os 

os.system('cls') 

MAX_NB_ESC = 5 
MAX_NOM_LENGTH = 20 
FINISH_LINE = 50 

def draw_depard_fin():
    print('DEPART' + (' ' * (FINISH_LINE - len('DEPART')) + 'FIN'))
    print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))

def saut_ligne(length='40'):
    print('\n' * int(length))


print(''' Course d'escargots: @v <-- escargot ''') 

# Boucle tant que pour demander le nombre d'ecargot qui participe à la course 
while True: 
    print('Combien d\'ecargots participant à cette course ?', MAX_NB_ESC) 
    reponseEsc = input('> ')
    if reponseEsc.isdecimal():
        numEscCourse = int(reponseEsc)
        if 1 < numEscCourse <= MAX_NB_ESC:
            break
    print('Entrer un nombre d\'ecargots valide entre 2 et ', MAX_NB_ESC)

# Entrer les noms pour chaque escargot
escNoms = []
for i in range(1, numEscCourse + 1):
    # Boucle tant qu'on rentre un nom valide
    while True:
        print('Entrer le nom de l\'escargot #' + str(i) + ' : ')
        nom = input('> ')
        if len(nom) == 0:
            print('Entrer un nom !')
        elif nom in escNoms:
            print('Choisi un autre nom !')
        else:
            break
    
    escNoms.append(nom)

'''
# Test si le tableau des noms est bien remplis !
print('Les noms d\'escargot sont: ')
for escargot in escNoms:
    print(escargot)
'''

# Affichage de tous les escargots sur la ligne de départ
saut_ligne()
draw_depard_fin()

escProgress = {}
for escNom in escNoms:
    print(escNom[:MAX_NOM_LENGTH])
    print('@v')
    escProgress[escNom] = 0

time.sleep(1.5)

while True:
    # On choisit d'avancer les escargots au hasard
    randEsc = random.randint(1, numEscCourse // 2)
    for i in range(randEsc):
        randEscNom = random.choice(escNoms)
        escProgress[randEscNom] += 1

    if escProgress[randEscNom] == FINISH_LINE:
        print(randEscNom, ' a gagné !')
        sys.exit()

    time.sleep(0.5)

    saut_ligne()
    draw_depard_fin()

    # Afficher les escargots (noms)
    for escNom in escNoms:
        espaces = escProgress[escNom]
        print((' ' * espaces) + escNom[:MAX_NOM_LENGTH])
        print(('.' * escProgress[escNom]) + '@v')

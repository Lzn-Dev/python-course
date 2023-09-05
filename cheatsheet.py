print('\n')

# Création de variables
liste = ['Un', 2, 'TROIS', ['a', 'b']]
string = "Hello World"
entier = 12
virgule = 34.43

print('Comment afficher le type d\'une variable pour inspection')
print('print(type(nomVariable))')
print(liste, type(liste))
print(string, type(string))
print(entier, type(entier))
print(virgule, type(virgule))
# Réaffectation 
string = 34
liste = virgule
entier = [1, 2, 3]
virgule = "not a float anymore"

print('\n')
# ---------------------------------------------------------------#

print('Opérations de bases')
virgule_plus_virgule = 10.2 + 2.3
virgule_moins_entier = 3.0 - 1   # 3.0 est un float, même si la partie décimale est nulle.
entier_fois_entier = 4 * 4
division_d_entiers = 4 / 2
# affichons le résultat et les types
print('Resultat de : 10.2 + 2.3 :')
print(virgule_plus_virgule, type(virgule_plus_virgule))
print('Resultat de : 3.0 - 1 :')
print(virgule_moins_entier, type(virgule_moins_entier))
print('Resultat de 4 * 4 :')
print(entier_fois_entier, type(entier_fois_entier))
print('Resultat de : 4 / 2 :')
print(division_d_entiers, type(division_d_entiers))

print('\n')
# ---------------------------------------------------------------#

print('Concaténation')
chaine_plus_chaine = "Hello" + " " + "World" + "! Génial, non?"
liste_plus_liste = [1, 2, 3] + ["Soleil"] + ["!", "!", "!"]
chaine_plus_nombre = "J'ai acheté " + str(3) + " salades."  

print('Hello + World => ' + chaine_plus_chaine)
print('J\'ai acheté + str(3) + salades => ' + chaine_plus_nombre)
print('[1,2,3] + ["Soleil"] + ["!", "!", "!"] => ' + str(liste_plus_liste))

print('\n')
# ---------------------------------------------------------------#

print('Replication')
trente_tirets = '---' * 10
liste_de_dix_zero = [0] * 10
deux_liste_de_dix_zero = liste_de_dix_zero * 2

print('\'---\' * 10 => ' + trente_tirets)
print('[0] * 10 => ' + str(liste_de_dix_zero))
print('liste_de_dix_zero * 2 => ' + str(deux_liste_de_dix_zero))

print('\n')
# ---------------------------------------------------------------#

print('Longueurs')
liste = [0,1,2,3,4,5,6,7,8,9]
phrase = 'Une phrase'

print('len([0,1,2,3,4,5,6,7,8,9]) => ' + str(len(liste)))
print('len(\'' + phrase + '\') => ' + str(len(phrase)))

print('\n')
# ---------------------------------------------------------------#

print('Formattage de chaines de caractères')
prenom = 'Bernard'
poid = 'gros'
message = f'Bonjour {prenom}, vous êtes {poid}.'
print('f\'Bonjour {prenom}, vous êtes {poid}.\' => ' + message)

print('\n')
# ---------------------------------------------------------------#

print('Les conditions')

print('Votre age : ', end='')
age = input()
print('age = input() => Votre choix.')

if int(age) < 18 : print('if int(age) < 18 : print(\'Sortez d\'ici\')')
elif int(age) > 18 : print('elif int(age) > 18 : print(\'Bienvenue\')')

liste = [1,2,3]
print('liste = ' + str([1,2,3]) + '=> if liste : #mon_code')
print('Le fait que la liste ne soit pas vide return true')

string = 'Pas vide'
print('string = \'' + string + '\' => if string : #mon_code')
print('Le fait que la string ne soit pas vide return true')

print('\n')
# ---------------------------------------------------------------#

print('La méthode print')

print('Pour empêcher le saut de ligne => ', end='')
print('print(\'Mon text\', end=\'\')')

print('\n')
# ---------------------------------------------------------------#

print('Les boucles')

liste = [1,2,3]
print('for item in liste :')
print(' print(item) =>')
print('===> OR <====')
print('for i in range (len(liste))')
print(' print(liste[i])')
for item in liste :
    print(item)

string = 'Une phrase'
for i in range(len(string)) :
    print(string[i], end='')

print('\n')
# ---------------------------------------------------------------#

print('Fonctions')

def addition() :
    print('Choix nombre a => ', end='')
    choix_nombre_a = int(input())
    print('Choix nombre b => ', end='')
    choix_nombre_b = int(input())
    return choix_nombre_a + choix_nombre_b

print(addition())

# Argument optionnel
def multiplication(message_personnalise = "A vos calculettes") :
    print(message_personnalise)
    print('Choix nombre a => ', end='')
    choix_nombre_a = int(input())
    print('Choix nombre b => ', end='')
    choix_nombre_b = int(input())
    return choix_nombre_a * choix_nombre_b

print(multiplication('Hmmm ok.'))

















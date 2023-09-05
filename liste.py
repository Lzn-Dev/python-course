liste = [0,1,2,3,4,5,6,7,8,9]

# 1. Itérator 

# iter(3.0) déclanche une erreur.
# iter ("Chaine de caractère") est itérable.
iterator = iter(liste) # Mon objet est itérable.
next(iterator) # => Le premier élément de ma liste
next(iterator) # => Le second élément de ma liste

# Si on effectue un next(iterator) alors qu'il n'y a plus d'éléments 
# On tombe sur une StopIteration exception

## 2. Boucles

# For basic
for item in liste :
    print(item)

# Les 4 méthodes principales 

## range() Gros avantage => Ne prend presque pas de mémoire
## range() ne créé les éléments qu'a la damande de next()
range_dix = range(10) # Donne un itérable de 0 à 10.
liste_dix = list(range_dix) # Donne une liste [0,1...10]
range_big = range(100000000) # Nécessite très peu de ressource.
liste_big = list(range_big) # Nécessite TROP de ressources 

# Utilisation la plus courante =>
a = 0
for i in range_big :
    a = i

print(a) # => Renvoi 999999999 sans utiliser de rame




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
for item in liste:
    print(item)

# Les 4 méthodes principales 


## 1. range() Gros avantage => Ne prend presque pas de mémoire
## range() ne créé les éléments qu'a la damande de next()
range_dix = range(10) # Donne un itérable de 0 à 10.
liste_dix = list(range_dix) # Donne une liste [0,1...10]
range_big = range(100000) # Nécessite très peu de ressource.
liste_big = list(range_big) # Nécessite TROP de ressources 
range_deux_args = range(10, 100) # 10 ==> 99
range_trois_args = range(10, 20, 2) # 10, 12, 14 ==> 18

# Utilisation la plus courante =>
for i in range_dix:
    a = i


## 2. enumerate() récupére la valeur ET l'index

for idx, obj in enumerate(["a", "b", "c"]):
    print(idx, obj)
# Retourne => (0, 'a') - (1, 'b') - (2, 'c')


## 3. reversed() inverse l'ordre d'une collection en retournant un itérateur

for obj in reversed(['c', 'b', 'a']):
    print(obj)
# Retourne => 'a', 'b', 'c'


## 4. zip() permet d'unir deux listes 
plat = ['blanquette de veaux', 'poulet roti']
prix = [12, 23, 34]
devise = ['euros', 'yens', 'roubles']

for obj in zip(plat, prix, devise):
    print(obj)
# Retourne => ('blanquette de veaux', 12, 'euros') - ('poulet roti', 23) - ('risotto', 7)
for plat, prix, devise in zip(plat, prix, devise):
    print('Le ' + plat + ' est à : ' + str(prix) + ' ' + devise)

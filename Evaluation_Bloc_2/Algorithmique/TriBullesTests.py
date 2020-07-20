import random


def triBulles(tableau):
    """ Procédure implémentant le tri bulles sur la liste passée en paramètre.
    Tri en place."""
    comparaison, echange = 0, 0
    for i in range(len(tableau) - 1, 0, -1):
        for j in range(0, i):
            comparaison += 1
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]
                echange += 1
                
    print("boucle for. comparaisons : ", comparaison, "echanges : ", echange)
                


def triBullesV2(tableau):
    """ Procédure implémentant le tri bulles sur la liste passée en paramètre.
    Tri en place."""
    i = len(tableau) - 1
    comparaison, echange = 0, 0
    while i >= 1:
        for j in range(0, i):
            comparaison += 1
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]
                echange += 1
        i = i - 1
    print("boucle while. comparaisons : ", comparaison, "echanges : ", echange)


def triBullesV3(tableau):
    """ Procédure implémentant le tri bulles sur la liste passée en paramètre.
    Tri en place."""
    i = len(tableau) - 1
    comparaison, echange = 0, 0
    while i >= 1:
        maxi = 0
        for j in range(0, i):
            comparaison += 1
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]
                echange += 1
                maxi = j
            # print(tableau)
        i = maxi
        # print(maxi)
    print("boucle while ++. comparaisons : ", comparaison, "echanges : ", echange)
    
def triCocktail(tableau):
    """ Procédure implémentant le tri bulles sur la liste passée en paramètre.
    Tri en place."""
    sup = len(tableau) - 1
    inf = 0
    comparaison, echange = 0, 0
    while sup > inf:
        # Tri bulle de gauche à droite
        fin = inf - 1
        for i in range(inf, sup):
            comparaison += 1
            if tableau[i] > tableau[i + 1]:
                tableau[i], tableau[i + 1] = tableau[i + 1], tableau[i]
                echange += 1
                fin = i
        sup = fin
        # Tri bulle de droite à gauche
        debut = sup + 1
        for j in range(sup, inf, -1):
            comparaison += 1
            if tableau[j] < tableau[j - 1]:
                tableau[j], tableau[j - 1] = tableau[j - 1], tableau[j]
                echange += 1
                debut = j
        inf = debut
    print("tri cocktail. comparaisons : ", comparaison, "echanges : ", echange)
        
                
def testTri(nb, taille):
    """ Test pour la fonction triBulles()
    Effectue nb tests sur des tableaux générés aléatoirement
    chaque tableau est de longueur taille"""
    compteur1 = 0
    compteur2 = 0
    compteur3 = 0
    compteur4 = 0
    for i in range(nb):
        tableau = [random.randrange(0, 200) for i in range(taille)]
        copie = tableau.copy()
        copie1 = tableau.copy()
        triBulles(copie1)
        if copie1 == sorted(tableau):
            compteur1 += 1
        else:
            print(copie, copie1)
        copie2 = tableau.copy()
        triBullesV2(copie2)
        if copie2 == sorted(tableau):
            compteur2 += 1
        else:
            print(copie, copie2)
        copie3 = tableau.copy()
        triBullesV3(copie3)
        if copie3 == sorted(tableau):
            compteur3 += 1
        else:
            print(copie, copie3)
        copie4 = tableau.copy()
        triCocktail(copie4)
        if copie4 == sorted(tableau):
            compteur4 += 1
        else:
            print(copie, copie3)
    return compteur1, compteur2, compteur3, compteur4

print(testTri(20, 1000))
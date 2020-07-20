import random


def triCocktail(tableau):
    """ Procédure implémentant le tri cocktail sur la liste passée en paramètre.
    Tri en place."""
    sup = len(tableau) - 1
    inf = 0
    borne = -1
    while sup > inf:
        # Tri bulle de gauche à droite
        for i in range(inf, sup):
            if tableau[i] > tableau[i + 1]:
                tableau[i], tableau[i + 1] = tableau[i + 1], tableau[i]
                borne = i
        sup = borne
        # Tri bulle de droite à gauche
        for j in range(sup, inf, -1):
            if tableau[j] < tableau[j - 1]:
                tableau[j], tableau[j - 1] = tableau[j - 1], tableau[j]
                borne = j
        inf = borne
    

def testTri(nb, taille):
    """ Test pour la fonction triCocktail()
    Effectue nb tests sur des tableaux générés aléatoirement
    chaque tableau est de longueur taille"""
    compteur = 0
    for i in range(nb):
        tableau = [random.randrange(0, 200) for i in range(taille)]
        copie = tableau.copy()
        triCocktail(tableau)
        # print("Tableau initial :", copie)
        # print("Tableau trié :", tableau)
        if tableau == sorted(copie):
            compteur += 1
        else:
            print(copie, tableau)
    return compteur


# print(testTri(50, 1000))
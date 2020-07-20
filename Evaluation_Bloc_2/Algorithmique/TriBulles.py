import random


def triBulles(tableau):
    """ Procédure implémentant le tri bulles sur la liste passée en paramètre.
    Tri en place."""
    for i in range(len(tableau) - 1, 0, -1):
        for j in range(0, i):
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]                

        
def testTri(nb, taille):
    """ Test pour la fonction triBulles()
    Effectue nb tests sur des tableaux générés aléatoirement
    chaque tableau est de longueur taille"""
    compteur = 0
    for i in range(nb):
        tableau = [random.randrange(0, 200) for i in range(taille)]
        copie = tableau.copy()
        triBulles(tableau)
        # print("Tableau initial :", copie)
        # print("Tableau trié :", tableau)
        if tableau == sorted(copie):
            compteur += 1
        else:
            print(copie, tableau)
    return compteur


# print(testTri(50, 1000))
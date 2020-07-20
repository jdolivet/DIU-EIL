import random


def triBullesAmeliore(tableau):
    """ Procédure implémentant le tri bulles sur la liste passée en paramètre.
    On arrête les comparaisons lorsque ce n'est plus la peine.
    Tri en place."""
    sup = len(tableau) - 1
    while sup >= 1:
        fin = 0
        for i in range(0, sup):
            if tableau[i] > tableau[i + 1]:
                tableau[i], tableau[i + 1] = tableau[i + 1], tableau[i]
                fin = i
        sup = fin


def testTri(nb, taille):
    """ Test pour la fonction triBullesAmeliore()
    Effectue nb tests sur des tableaux générés aléatoirement
    chaque tableau est de longueur taille"""
    compteur = 0
    for i in range(nb):
        tableau = [random.randrange(0, 200) for i in range(taille)]
        copie = tableau.copy()
        triBullesAmeliore(tableau)
        # print("Tableau initial :", copie)
        # print("Tableau trié :", tableau)
        if tableau == sorted(copie):
            compteur += 1
        else:
            print(copie, tableau)
    return compteur


# print(testTri(50, 1000))
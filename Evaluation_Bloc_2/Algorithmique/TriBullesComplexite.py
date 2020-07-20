import random, time
import pylab as plt


def triBulles(tableau):
    """ Tri bulles sur la liste passée en paramètre.
    Retourne le nombre de comparaisons et d'échanges effectués."""
    comparaisons, echanges = 0, 0
    for i in range(len(tableau) - 1, 0, -1):
        for j in range(0, i):
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]
                echanges += 1
            comparaisons += 1
    return comparaisons, echanges


def triCocktail(tableau):
    """ Tri cocktail sur la liste passée en paramètre.
    Retourne le nombre de comparaisons et d'échanges effectués."""
    comparaisons, echanges = 0, 0
    sup = len(tableau) - 1
    inf = 0
    while sup > inf:
        fin = inf - 1
        for i in range(inf, sup):
            if tableau[i] > tableau[i + 1]:
                tableau[i], tableau[i + 1] = tableau[i + 1], tableau[i]
                echanges += 1
                fin = i
            comparaisons += 1
        sup = fin
        debut = sup + 1
        for j in range(sup, inf, -1):
            if tableau[j] < tableau[j - 1]:
                tableau[j], tableau[j - 1] = tableau[j - 1], tableau[j]
                echanges += 1
                debut = j
            comparaisons += 1
        inf = debut
    return comparaisons, echanges
        
        
def complexiteTri(tri, tailleEchantillon, tailleTableau, nbDouble):
    """ Test la complexité du tri bulles
    On simule un échantillon de tailleEchantillon tableau de taille tailleTableau
    On calcule le nb moyen de comparaisons, d'echanges et le temps moyen du tri.
    Puis on double la taille nbDouble fois et recueille les mêmes informations."""
    # On utilise des tableaux pour les tracés
    tailleTableaux = []
    comparaisons, echanges, durees = [], [], []
    # On créé nbDouble échantillons
    for i in range(nbDouble):
        tailleTableaux.append(tailleTableau)
        sommeComparaisons, sommeEchanges, sommeDurees = 0, 0, 0
        # On créé des échantillons de tailleEchantillon
        for j in range(tailleEchantillon):
            tableau = [random.randrange(0, 20000) for i in range(tailleTableau)]
            start_time = time.perf_counter()
            nbComparaisons, nbEchanges = tri(tableau)
            duree = time.perf_counter() - start_time
            sommeComparaisons += nbComparaisons
            sommeEchanges += nbEchanges
            sommeDurees += duree
        moyComparaisons = sommeComparaisons / tailleEchantillon
        moyEchanges = sommeEchanges / tailleEchantillon
        moyDurees = round(sommeDurees / tailleEchantillon, 8)
        comparaisons.append(moyComparaisons)
        echanges.append(moyEchanges)
        durees.append(moyDurees)
        # impression des résultats
        print("Pour", tailleEchantillon, "tableaux de taille", tailleTableau, ": ")
        print("    nb moyens comparaisons du tri :", moyComparaisons)
        print("    nb moyens échanges du tri :", moyEchanges)
        print("    durée moyenne du tri (en sec) :", moyDurees, '\n')
        tailleTableau *= 2        # On double la taille du tableau
    return tailleTableaux, comparaisons, echanges, durees


def plotComplexite(resultats1, resultats2):
    """ Procédure permettant d'obtenir une représentation graphique
    Comparaisons entre les tris"""
    plt.figure("Comparaison Tris")
    plt.subplot(1, 3, 1)
    plt.title('Comparaisons')
    plt.xlabel("Taille du tableau"), plt.ylabel("Nb de comparaisons")        
    plt.plot(resultats1[0], resultats1[1], 'r', label = "Bubble sort")
    plt.plot(resultats2[0], resultats2[1], 'g', label = "Shaker sort")
    plt.ylim(ymin = 0), plt.xlim(xmin = 0)
    plt.xticks(rotation = 90), plt.legend(loc = 'upper left')
    plt.subplot(1, 3, 2)
    plt.title('Echanges')
    plt.xlabel("Taille du tableau"), plt.ylabel("Nb d'échanges")    
    plt.plot(resultats1[0], resultats1[2], 'r', label = "Bubble sort")
    plt.plot(resultats2[0], resultats2[2], 'g', label = "Shaker sort")
    plt.ylim(ymin = 0), plt.xlim(xmin = 0)
    plt.xticks(rotation = 90), plt.legend(loc = 'upper left')
    plt.subplot(1, 3, 3)
    plt.title('Durées du tri')
    plt.xlabel("Taille du tableau"), plt.ylabel("Durée du tri en sec")    
    plt.plot(resultats1[0], resultats1[3], 'r', label = "Bubble sort")
    plt.plot(resultats2[0], resultats2[3], 'g', label = "Shaker sort")
    plt.ylim(ymin = 0), plt.xlim(xmin = 0)
    plt.xticks(rotation = 90), plt.legend(loc = 'upper left')
    plt.show()
    

# resultatsTriBulles = complexiteTri(triBulles, 100, 1000, 10)
# resultatsTriCocktail = complexiteTri(triCocktail, 100, 1000, 10)
# plotComplexite(resultatsTriBulles, resultatsTriCocktail)
from classePile import *

# Variables globales
operateurs = { '*' : (lambda a, b : a * b), '+' : (lambda a,b : a + b), 
              '/' : (lambda a,b : a / b), '-': (lambda a,b : a - b)}
pileCalcul = Pile()

print('Calculatrice simplifiée')
print('Entrer un nb entier ou un operateur')
print('Pour retourner le resultat : =')

def calcul():
    """Procédure permettant d'effectuer un calcul en Notation Polonaise """
    #il faut vider la pile de calcul, si erreur dans le dernier calc
    while not pileCalcul.est_vide():   
        pileCalcul.depiler()
    pileCalcul.empiler('end')
    while True:
        # on rentre des nbs entiers, ou opérateurs. '=' pour arrêter
        entree = input('Instruction calculatrice : ') 
        if entree == '=':
            break
        elif entree in operateurs:
            pileCalcul.empiler(entree)
        else: # si c'est un nb 
            suivant = pileCalcul.depiler()
            while (suivant != 'end') and (suivant not in operateurs): # si c'est un nb et pas la fin de la pile
                op = pileCalcul.depiler()
                entree = operateurs[op](float(suivant), float(entree))
                suivant = pileCalcul.depiler()
            pileCalcul.empiler(suivant)
            pileCalcul.empiler(entree)
        print('Pile :', pileCalcul)
    final = pileCalcul.depiler()
    print('Résultat :', final)   # pas de return

# parseur simple utilisé pour la séquence du DIU

from classeArbreBinaireMutable import *
from classePile import *

VIDE = NoeudMutable('', NoeudMutable(), NoeudMutable())
OPERATEURS = {'+', '-', '*', '/'}

def analyseSyntaxe(exp):
    """ Entree : string bien parenthésée
    Les operateurs doivent apparaître explicitement.
    Exemples :
        15 * 5 + (2 + 3) doit être ((15*5)+(2+3))
        6(9 + 7) + (7 − 14) doit être ((6*(9+7))+(7-14))
    Autrement dit : autant de couples de parenthèses que d'operateurs.
    Sortie : arbre binaire de la représentation syntaxique de l'expression."""
    # Tests
    # On verifie qu'il y a autant de parenthèses ouvrantes que de fermantes
    assert exp.count('(') == exp.count(')'),\
           "Attention, il faut autant de parenthèses ouvrantes que fermantes"
    # On verifie qu'il y a autant de parenthèses ouvrantes que d'operateurs
    assert exp.count('(') == sum([exp.count(op) for op in OPERATEURS]),\
           "Attention, il faut autant de couples de parenthèses que d'opérateurs"
    
    # Analyse lexicale
    # On fait un traitement pour pouvoir differencier '(', ')', '*', '-', '/', '+' et nbs.
    for car in OPERATEURS:
        exp = exp.replace(car, ' ' + car + ' ')
    for car in {'(', ')'}:
        exp = exp.replace(car, ' ' + car + ' ') 
    liste = exp.split()
    
    # Analyse syntaxique
    # On construit l'arbre mutable
    pile = Pile()
    arbre = VIDE
    pile.empiler(arbre)
    enCours = arbre
    # On parcourt la liste des operandes, operateurs et parentheses
    for elt in liste:
        if elt == '(':
            enCours.insere_gauche('')
            pile.empiler(enCours)
            enCours = enCours.gauche()
        elif elt in OPERATEURS:
            enCours.insere_etiquette(elt)
            enCours.insere_droit('')
            pile.empiler(enCours)
            enCours = enCours.droit()
        elif elt == ')':
            enCours = pile.depiler()
        else:
            enCours.insere_etiquette(int(elt))
            parent = pile.depiler()
            enCours = parent
    # on convertit en un arbre immuable (de la classe Noeud du cours)
    arbreBinaire = copie_immuable(arbre) 
    return arbreBinaire 
    
# tree1 = analyseSyntaxe('(3+(4*5  )     )')
# print(type(tree1))
# print(tree1)
# 
# tree2 = analyseSyntaxe('((6 * (9 + 7)) + (7 - 14))')
# print(tree2)

    
    
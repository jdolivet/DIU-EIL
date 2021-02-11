# Classe arbre binaire mutable (basée sur des listes et non des tuples)
from classeArbreBinaire import *

class NoeudMutable:
    def __init__(self, *args):
        if len(args) == 0:
            self.contenu = None
        else:
            self.contenu = [args[0], args[1], args[2]]# je passe aux listes pour pouvoir modifier

    def etiquette(self):
        return(self.contenu[0])

    def gauche(self):
        return(self.contenu[1])
        
    def droit(self):
        return(self.contenu[2])
    
    def est_vide(self):
        return self.contenu == None
    
    def __repr__(self):
        return "()" if self.est_vide() else '(' + str(self.etiquette()) + str(self.gauche()) + str(self.droit()) + ')'

    # ajout de méthodes
    def insere_etiquette(self, valeur):
        self.contenu[0] = valeur

    def insere_gauche(self, valeur):
        self.contenu[1] = NoeudMutable(valeur, NoeudMutable(), NoeudMutable())
        
    def insere_droit(self, valeur):
        self.contenu[2] = NoeudMutable(valeur, NoeudMutable(), NoeudMutable())
        
        
def copie_immuable(arbre_mutable):
    """ retourne la copie d'un arbre mutable en arbre immuable
    entree : NoeudMutable
    sortie : Noeud"""
    if arbre_mutable.est_vide():
        return Noeud()
    else:
        return Noeud(arbre_mutable.etiquette(),
                     copie_immuable(arbre_mutable.gauche()),
                     copie_immuable(arbre_mutable.droit()))


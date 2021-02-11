import math as m


class Operation:

    def __init__(self, nom, X, M, p):
        """Cree une instance Operation"""
        self.nom = nom
        self.X = X
        self.M = M
        self.p = p
        self.ops = ['x^2', 'sqrt', '10^x', 'e^x', '+', '-', '*', 'y^x', '1/x', 'LOG', 'LN', '/',
                    'CLEAR', 'xy', 'RCL', 'STO', 'ENTER']

    def calcul(self):
        """
        Détermine la méthode opération à appeler en fonction de sa posution dans la lsite self.ops
        :return: un appel à la méthode opération correspondante
        """
        op = self.ops.index(self.nom)
        default = "Erreur"
        return getattr(self, 'operation_' + str(op), lambda: default)()

    def val(self, x):
        """
        :param x: une chaîne de caractères contenant un nombre flottant ou entier.
        :return: renvoie un flottant si la chaîne contient '.' et un entier sinon
        """
        return float(x) if '.' in x else int(x)

    def get_value(self):
        """ Renvoie le string au sommet de la pile, si la variable X est vide"""
        valeur = self.p.depiler() if self.X == '' else self.X
        return valeur

    def formate(self, x):
        """
        :param x: un nombre
        :return: le nombre arrondi à 10 décimales
        """
        return str(round(x, 10))

    def operation_0(self):
        """ Renvoie le carré de l'opérande """
        v1 = self.val(self.get_value())
        self.p.empiler(self.formate(v1 ** 2))
        return ''

    def operation_1(self):
        """ Renvoie la racine carrée de l'opérande"""
        v1 = self.val(self.get_value())
        try:
           resultat = self.formate(m.sqrt(v1))
        except ValueError:
            resultat =  'Math Error'
        self.p.empiler(resultat)
        return ''

    def operation_2(self):
        """ Renvoie 10 à la puissance opérande"""
        v1 = self.val(self.get_value())
        self.p.empiler(self.formate(10 ** v1))
        return ''

    def operation_3(self):
        """ Renvoie l'exponentielle de l'opérande"""
        v1 = self.val(self.get_value())
        self.p.empiler(self.formate(m.e ** v1))
        return ''

    def operation_4(self):
        """ Renvoie la somme des opérandes"""
        v1 = self.val(self.get_value())
        self.X = ''
        v2 = self.val(self.get_value())
        self.p.empiler(self.formate(v1 + v2))
        return ''

    def operation_5(self):
        """ Renvoie la différence entre les opérandes """
        v1 = self.val(self.get_value())
        self.X = ''
        v2 = self.val(self.get_value())
        self.p.empiler(self.formate(v2 - v1))
        return ''

    def operation_6(self):
        """ Renvoie le produit des opérandes """
        v1 = self.val(self.get_value())
        self.X = ''
        v2 = self.val(self.get_value())
        self.p.empiler(self.formate(v1 * v2))
        return ''

    def operation_7(self):
        """ Renvoie l'opérande v2 à l'exposant v1"""
        v1 = self.val(self.get_value())
        self.X = ''
        v2 = self.val(self.get_value())
        self.p.empiler(self.formate(v2 ** v1))
        return ''

    def operation_8(self):
        """ Renvoie l'inverse de l'opérande """
        v1 = self.val(self.get_value())
        try:
            resultat = self.formate(1 / v1)
        except ValueError:
            resultat = 'Math Error'
        self.p.empiler(resultat)
        return ''

    def operation_9(self):
        """ Renvoie le logarithme décimal de l'opérande """
        v1 = self.val(self.get_value())
        try:
            resultat =  self.formate(m.log10(v1))
        except ValueError:
            resultat = 'Math Error'
        self.p.empiler(resultat)
        return ''

    def operation_10(self):
        """ Renvoie le logarithme népérien de l'opérande """
        v1 = self.val(self.get_value())
        try:
            resultat =  self.formate(m.log(v1))
        except ValueError:
            resultat =  'Math Error'
        self.p.empiler(resultat)
        return ''

    def operation_11(self):
        """ Renvoie le quotient des opérandes, la division est entière ou flottante suivant les valeurs """
        x = self.get_value()
        self.X = ''
        y = self.get_value()
        v1, v2 = self.val(x), self.val(y)
        try:
            if self.nom == '/' and '.' not in x and '.' not in y and v2 % v1 == 0:
                resultat = self.formate(v2 // v1)
            else:
                resultat = self.formate(v2 / v1)
        except ZeroDivisionError:
            resultat =  'Math Error'
        self.p.empiler(resultat)
        return ''

    def operation_12(self):
        """Nettoie la pile"""
        self.p.vider_pile()
        return ''

    def operation_13(self):
        """ Echange les deux premiers niveaux de la pile """
        X = self.get_value()
        self.X = ''
        Y = self.get_value()
        self.p.empiler(X)
        self.p.empiler(Y)
        return ''

    def operation_14(self):
        """ Rappelle la valeur se trouvant en mémoire """
        self.p.empiler(self.M)
        return ''

    def operation_15(self):
        """ Stocke la valeur de X dans la mémoire"""
        M = self.get_value()
        self.p.empiler(M)
        return M

    def operation_16(self):
        """Touche ENTER, la chaîne X est entrée dans la pile"""
        self.p.empiler(self.X)
        return ''

from flask import Flask

app = Flask(__name__) # On instancie notre objet Flask (une application)

# On définit le chemin principal
@app.route('/')
# Le comportement souhaité lorsqu'on y accède
def index():
    return "Salut! Tu es au bon endroit!"


# On définit le chemin au travers duquel nous pourrons lancer notre convertisseur
@app.route('/binaire/<int:entier>')
# Le paramètre de conversion() correspond au nombre passé dans l'URL
def conversion(entier):
    """ entier est un nombre entier positif.
    Retourne l'écriture de entier en binaire sur un demi octet.
    Le résultat est une liste de 4 bits.
    1 bit est un entier valant 0 ou 1.
    Le 1e est le bit de poids faible.
    """
    nibble = []
    entree = entier
    for i in range(4):
        bit = entier % 2
        nibble.append(bit)
        entier = entier // 2
    return "La représentation binaire de " + str(entree) +\
           " est " + str(nibble)

#On lance notre application
if __name__ == '__main__':  
        app.run(host = '0.0.0.0', debug = True)
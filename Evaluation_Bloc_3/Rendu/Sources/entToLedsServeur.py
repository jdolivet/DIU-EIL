from flask import Flask
import RPi.GPIO as GPIO

# On paramètres les broches
GPIO.setmode(GPIO.BCM)   
listeBroches = [2, 3, 4, 5]
for broche in listeBroches:
    GPIO.setup(broche, GPIO.OUT) 

# On instancie notre objet Flask (une application)
app = Flask(__name__) 

# On définit le chemin principal
@app.route('/')
# Le comportement souhaité lorsqu'on y accède
def index():
    return "Salut! Tu es au bon endroit!"


# On définit le chemin au travers duquel nous pourrons lancer notre convertisseur
@app.route('/binaire/<int:entier>')
# Le paramètre de conversion() correspond au nombre passé dans l'URL
def conversionLEDs(entier):
    """ entier est un nombre entier positif.
    Retourne l'écriture de entier en binaire sur un demi octet.
    Le résultat est une liste de 4 bits.
    1 bit est un entier valant 0 ou 1.
    Le 1e est le bit de poids faible.
    Déclenche l'affichage des LEDs correspondantes.
    """
    entree = entier
    # On convertit l'entier
    nibble = []
    for i in range(4):
        bit = entier % 2
        nibble.append(bit)
        entier = entier // 2
    # On allume les LEDs correspondantes
    B0, B1, B2, B3 = 2, 3, 4, 5 # On associe les bits aux broches
    listeLEDs = [B0, B1, B2, B3]
    for i in range(4):
        if nibble[i] == 1:
            GPIO.output(listeLEDs[i], GPIO.HIGH)
        else:
            GPIO.output(listeLEDs[i], GPIO.LOW)           
    return "La représentation binaire de " + str(entree) +\
           " est " + str(nibble)

#On lance notre application
if __name__ == '__main__':  
        app.run(host = '0.0.0.0')

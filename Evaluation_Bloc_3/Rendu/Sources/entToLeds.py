import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)   # On choisit le type de numérotation des broches
#Les broches sont des sorties
listeBroches = [2, 3, 4, 5]
for broche in listeBroches:
    GPIO.setup(broche, GPIO.OUT) 

def conversionLEDs(entier):
    """ entier est un nombre entier positif.
    Retourne l'écriture de entier en binaire sur un demi octet.
    Le résultat est une liste de 4 bits.
    1 bit est un entier valant 0 ou 1.
    Le 1e est le bit de poids faible.
    Déclenche l'affichage des LEDs correspondantes.
    """
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
    return nibble
            
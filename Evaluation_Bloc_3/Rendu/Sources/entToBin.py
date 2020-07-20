def conversion(entier):
    """ entier est un nombre entier positif.
    Retourne l'écriture de entier en binaire sur un demi octet.
    Le résultat est une liste de 4 bits.
    1 bit est un entier valant 0 ou 1.
    Le 1e est le bit de poids faible.
    """
    nibble = []
    for i in range(4):
        bit = entier % 2
        nibble.append(bit)
        entier = entier // 2
    return nibble

        
def testConversion():
    """ Quelques tests sur la fonction conversion()"""
    assert conversion(0) == [0, 0, 0, 0]
    assert conversion(5) == [1, 0, 1, 0]
    assert conversion(15) == [1, 1, 1, 1]
    assert conversion(16) == [0, 0, 0, 0]

testConversion()
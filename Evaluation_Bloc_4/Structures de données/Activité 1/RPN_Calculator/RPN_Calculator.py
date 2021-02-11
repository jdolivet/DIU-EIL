import tkinter as tk
import Pile
import Operations


""" Le dictionnaire TOUCHES contient les coordonnées des
différentes touches de la calculatrice """
TOUCHES = {'OFF': {'x1': 326, 'y1': 608, 'x2': 377, 'y2': 658},
           '+/-': {'x1': 18, 'y1': 606, 'x2': 71, 'y2': 657},
           '0': {'x1': 89, 'y1': 606, 'x2': 141, 'y2': 657},
           '.': {'x1': 157, 'y1': 606, 'x2': 212, 'y2': 657},
           '1': {'x1': 18, 'y1': 540, 'x2': 71, 'y2': 591},
           '2': {'x1': 89, 'y1': 540, 'x2': 141, 'y2': 591},
           '3': {'x1': 157, 'y1': 540, 'x2': 212, 'y2': 591},
           '4': {'x1': 18, 'y1': 474, 'x2': 71, 'y2': 524},
           '5': {'x1': 89, 'y1': 474, 'x2': 141, 'y2': 524},
           '6': {'x1': 157, 'y1': 474, 'x2': 212, 'y2': 524},
           '7': {'x1': 18, 'y1': 408, 'x2': 71, 'y2': 458},
           '8': {'x1': 89, 'y1': 408, 'x2': 141, 'y2': 458},
           '9': {'x1': 157, 'y1': 408, 'x2': 212, 'y2': 458},
           '+': {'x1': 245, 'y1': 474, 'x2': 289, 'y2': 524},
           '*': {'x1': 245, 'y1': 540, 'x2': 289, 'y2': 591},
           '-': {'x1': 322, 'y1': 474, 'x2': 376, 'y2': 524},
           '/': {'x1': 322, 'y1': 540, 'x2': 376, 'y2': 591},
           'ENTER': {'x1': 240, 'y1': 409, 'x2': 384, 'y2': 455},
           'CLEAR': {'x1': 24, 'y1': 343, 'x2': 79, 'y2': 394},
           'xy': {'x1': 245, 'y1': 343, 'x2': 299, 'y2': 394},
           '<-': {'x1': 319, 'y1': 343, 'x2': 372, 'y2': 394},
           'x^2': {'x1': 24, 'y1': 281, 'x2': 79, 'y2': 332},
           'sqrt': {'x1': 24, 'y1': 212, 'x2': 79, 'y2': 261},
           'y^x': {'x1': 98, 'y1': 281, 'x2': 152, 'y2': 332},
           '1/x': {'x1': 98, 'y1': 212, 'x2': 152, 'y2': 261},
           'LOG': {'x1': 171, 'y1': 281, 'x2': 225, 'y2': 332},
           '10^x': {'x1': 171, 'y1': 212, 'x2': 225, 'y2': 261},
           'LN': {'x1': 245, 'y1': 281, 'x2': 299, 'y2': 332},
           'e^x': {'x1': 245, 'y1': 212, 'x2': 299, 'y2': 261},
           'RCL': {'x1': 319, 'y1': 281, 'x2': 372, 'y2': 332},
           'STO': {'x1': 319, 'y1': 212, 'x2': 372, 'y2': 261}
           }


def clic_mouse(event):
    """Détecte les clics de la souris dans la calcukatrice"""
    global pile
    for t in TOUCHES:
        x1 = TOUCHES[t]['x1']
        x2 = TOUCHES[t]['x2']
        y1 = TOUCHES[t]['y1']
        y2 = TOUCHES[t]['y2']
        if x1 < event.x < x2 and y1 < event.y < y2:
            touche_pressee(t, pile)
            break


def val(x):
    return float(x) if '.' in x else int(x)


def touche_pressee(t, p):
    """
    :param t: nom de la touche pressée dans le dictionnaire TOUCHES
    :param p: pile de la calculatrice
    :return:
    """

    global enter, X, M
    if not p.est_vide():
        sommet = p.depiler()
        if sommet != 'Math Error':
            p.empiler(sommet)
        else:
            p.vider_pile()
            X = '0'
    if t in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}:
        if enter or X == '0':
            enter = False
            X = ''
        if t == '.' and X == '':
            X = '0.'
        elif t != '.' or (t == '.' and '.' not in X):
            X += t
    elif t == '<-':
        X = X[:-1] if len(X) > 1 else '0'
        if X[-1] == '.':
            X = X[:-1]
    elif t == '+/-':
        if X == '':
            X = p.depiler()
            p.empiler(str(- val(X)))
            X = ''
        else:
            X = str(-val(X))
    elif t == 'OFF':
        quit()
    else:
        enter = True
        X = Operations.Operation(t, X, M, p).calcul()
        if X != '':
            M = X
            X = ''
    if X == '':
        X = p.depiler()
        p.empiler(X)
    ecran.config(text=X)
    if enter:
        X = ''


root = tk.Tk()
root.title("RPN Calculator")
root.geometry('400x677+50+25')

calculatrice = tk.PhotoImage(file="CalcRPN.png")

canevas = tk.Canvas(root, width=400, height=677)
canevas.create_image(0, 0, anchor=tk.NW, image=calculatrice)
canevas.bind('<Button-1>', clic_mouse)
canevas.pack()

ecran = tk.Label(canevas, text="0", font='Verdana 30', bg='#CBC366', justify='right')
ecran.pack()
canevas.create_window(355, 119, window=ecran, anchor=tk.E)

pile = Pile.Pile()

X = '0'   # La valeur en cours d'entrée
M = '0'   # L'unique mémoire de cette calculatrice
enter = False  # Indique si la dernière touche pressée est ENTER ou une opération

root.mainloop()

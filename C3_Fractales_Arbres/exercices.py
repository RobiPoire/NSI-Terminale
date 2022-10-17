"""
Les fractales et les arbres
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implementation des fractales et des arbres avec turtle
"""

__author__ = "HabibLebsir, devnationfrance, RobiPoire"

from turtle import *
from math import *


# Partie A

# A.4.1
def carre(longueur: int) -> None:
    """Dessine un carré avec ses diagonales de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du carré
    """
    for i in range(4):
        forward(longueur)
        left(90)
    left(45)
    forward(sqrt(2*longueur**2))
    left(135)
    forward(longueur)
    left(135)
    forward(sqrt(2*longueur**2))


# A.4.2
def triangle(longueur: int) -> None:
    """Dessine un triangle de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
    """
    for i in range(3):
        forward(longueur)
        left(120)


# A.4.3
def figure_triangle(longueur: int) -> None:
    """Dessine un triangle de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
    """
    for i in range(3):
        triangle(longueur)
        left(120)


# A.4.3
def triforce(longueur: int) -> None:
    """Dessine une triforce de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
    """
    for i in range(2):
        triangle(longueur)
        forward(longueur)
    left(120)
    forward(longueur)
    triangle(longueur)


# A.4.4 a
def triangle_rectangle(longueur: int) -> None:
    """Dessine un triangle rectangle de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
    """
    for i in range(2):
        forward(longueur)
        left(90)
    left(45)
    forward(sqrt(2*longueur**2))
    left(135)


# A.4.4 b
def figure_triangles_rectangle(longueur: int, repetitions: int) -> None:
    """Dessine un triangle rectangle de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
        repetitions (int): le nombre de répétitions
    """
    for i in range(1, repetitions):
        triangle_rectangle(longueur*i)


# Partie B

# B.2
def trace(chaine: str, longueur: int, angle: int) -> None:
    """Trace une figure

    Args:
        chaine (str): Les chaines à suivre
        longueur (int): La longueur des figures
        angle (int): L'angle des figures
    """
    for i in chaine:
        if i == "A":
            forward(longueur)
        elif i == "+":
            left(angle)
        elif i == "-":
            right(angle)


# Partie C

# C.2
def deplacement(s: str, motif: str, repetitions: int) -> str:
    """ Crée une nouvelle chaîne de caractères en appliquant le motif à la chaîne s

    Args:
        s (str): La chaîne de caractères à modifier
        motif (str): Le motif à appliquer
        repetitions (int): Le nombre de répétitions

    Returns:
        str: La nouvelle chaîne de caractères
    """
    for i in range(repetitions):
        s = s.replace("A", motif)
    return s


# C.3
def flocon_koch(longueur: int, repetitions: int) -> None:
    """Dessine un flocon de Koch

    Args:
        longueur (int): La longueur du triangle
        repetitions (int): Le nombre de répétitions
    """
    chaines = "A--A--A"
    chaines = deplacement(chaines, "A+A--A+A", repetitions)
    trace(chaines, longueur, 60)


# C.4
def courbe_quadratique_Koch_type_deux(longueur: int, repetitions: int) -> None:
    """Dessine une courbe quadratique de Koch

    Args:
        longueur (int): La longueur du triangle
        repetitions (int): Le nombre de répétitions
    """
    chaines = "A+A+A+A"
    chaines = deplacement(chaines, "A-A+A+AA-A-A+A", repetitions)
    trace(chaines, longueur, 90)

# Partie D


def triangle_sierpinsky(longueur: int, repetitions: int) -> None:
    """Dessine un triangle de Sierpinsky

    Args:
        longueur (int): La longueur du triangle
        repetitions (int): Le nombre de répétitions
    """
    left(180)  # On tourne la tortue pour que le triangle soit orienté vers le haut
    chaines = "A--A--A"
    chaines = deplacement(chaines, "A-A+A+A-A", repetitions)
    trace(chaines, longueur, 120)
    # On trace le grand triangle autour :
    left(60)
    forward(longueur*(2**repetitions))
    for i in range(2):
        left(120)
        forward(longueur*(2**repetitions)*2)
    left(120)
    forward(longueur*(2**repetitions))

# Partie E

# E.1 a


def empiler(pile: list) -> None:
    """Empile une figure

    Args:
        pile (list): La pile de figures
    """
    pile.append([heading(), position()])


# E.1 a
def depiler(pile: list) -> None:
    """Dépile une figure

    Args:
        pile (list): La pile de figures
    """
    penup()
    angle, coordonnees = pile.pop()
    goto(coordonnees)
    setheading(angle)
    pendown()


# E.1 b
def trace2(chaine: str, longueur: int, angle: int) -> None:
    """Trace une figure en utilisant la pile

    Args:
        chaine (str): La chaîne de caractères à suivre
        longueur (int): La longueur des figures
        angle (int): L'angle des figures
    """
    pile = []
    for i in chaine:
        if i == "A":
            forward(longueur)
        elif i == "+":
            left(angle)
        elif i == "-":
            right(angle)
        elif i == "[":
            empiler(pile)
        elif i == "]":
            depiler(pile)


# E.1 c
def arbre_simple(longueur: int, repetitions: int) -> None:
    """Dessine un arbre simple

    Args:
        longueur (int): La longueur du triangle
        repetitions (int): Le nombre de répétitions
    """
    chaines = "A"
    chaines = deplacement(chaines, "A[+A][-A]", repetitions)
    trace2(chaines, longueur, 30)


# E.2
def plante_longiligne(longueur: int, repetitions: int) -> None:
    """Dessine une plante longiligne

    Args:
        longueur (int): La longueur du triangle
        repetitions (int): Le nombre de répétitions
    """
    left(90)
    chaines = "A"
    chaines = deplacement(chaines, "A[+A]A[-A]A", repetitions)
    trace2(chaines, longueur, 25)

# E.3


def buisson_type_aneth(longueur: int, repetitions: int) -> None:
    """Dessine un buisson type aneth

    Args:
        longueur (int): La longueur du triangle
        repetitions (int): Le nombre de répétitions
    """
    left(90)
    chaines = "A"
    chaines = deplacement(chaines, "AA+[+A-A-A]-[-A+A+A]", repetitions)
    trace2(chaines, longueur, 20)


# Exemple d'utilisation
if __name__ == "__main__":
    speed(0)  # On met la vitesse de la tortue au maximum
   # carre(10)
   # triangle(10)
   # figure_triangle(10)
   # triangle_rectangle(10)
   # figure_triangles_rectangle(10, 4)
   # trace("A--A--A", 10, 60)
   # deplacement("A--A--A", "A+A--A+A", 2)
   # flocon_koch(5, 3)
   # courbe_quadratique_Koch_type_deux(5, 3)
   # triangle_sierpinsky(5, 3)
   # arbre_simple(5, 4)
   # plante_longiligne(5, 4)
   # buisson_type_aneth(5, 4)
    mainloop()  # Pour eviter des bugs avec turtle

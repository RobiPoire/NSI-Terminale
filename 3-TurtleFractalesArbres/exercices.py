"""
Les fractales et les arbres
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implementation des fractales et des arbres avec turtle
"""

__author__ = "HabibLebsir, devnationfrance, RobiPoire"

from turtle import *
from math import *

# Partie A


def triangle(longueur: int) -> None:
    """Dessine un triangle de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
    """
    for i in range(3):
        forward(longueur)
        left(120)


def carre(longueur: int) -> None:
    """Dessine un carré de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du carré
    """
    for i in range(4):
        forward(longueur)
        left(90)


def rectangle(longueur: int, height: int) -> None:
    """Dessine un rectangle de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du rectangle
        height (int): la hauteur du rectangle
    """
    for i in range(2):
        forward(longueur)
        left(90)
        forward(height)
        left(90)


def figure_triangle(longueur: int) -> None:
    """Dessine un triangle de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
    """
    for i in range(3):
        triangle(longueur)
        left(120)


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


def trirect(longueur: int, repetitions: int) -> None:
    """Dessine un triangle rectangle de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
        repetitions (int): le nombre de répétitions
    """
    for i in range(1, repetitions):
        triangle_rectangle(longueur*i)


def etoile(longueur: int) -> None:
    """Dessine une étoile de la longueur donnée

    Args:
        longueur (int): la longueur des côtés de l'étoile
    """
    for i in range(5):  # Une étoile à 5 branches
        forward(longueur)
        right(144)

# Partie B


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


def flocon_koch(longueur: int, repetitions: int) -> None:
    """Dessine un flocon de Koch

    Args:
        longueur (int): La longueur du triangle
        repetitions (int): Le nombre de répétitions
    """
    chaines = "A--A--A"
    chaines = deplacement(chaines, "A+A--A+A", repetitions)
    trace(chaines, longueur, 60)


def courbe_quadratique_Koch_type_deux(longueur: int, repetitions: int) -> None:
    """Dessine une courbe quadratique de Koch

    Args:
        longueur (int): La longueur du triangle
        repetitions (int): Le nombre de répétitions
    """
    chaines = "A+A+A+A"
    chaines = deplacement(chaines, "A-A+A+AA-A-A+A", repetitions)
    trace(chaines, longueur, 90)

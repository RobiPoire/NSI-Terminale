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

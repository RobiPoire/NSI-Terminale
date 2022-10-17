"""
Recursivité - Les figures fractales 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Les figures fractales implémentées 
"""

__author__ = "RobiPoire, HabibLebsir"      

from turtle import *


def flocon_koch(longueur: int, repetitions: int) -> None:
    """Dessine un flocon de Koch de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
        repetitions (int): le nombre de répétitions
    """
    if repetitions == 0:
        forward(longueur)
    else:
        flocon_koch(longueur / 3, repetitions - 1)
        left(60)
        flocon_koch(longueur / 3, repetitions - 1)
        right(120)
        flocon_koch(longueur / 3, repetitions - 1)
        left(60)
        flocon_koch(longueur / 3, repetitions - 1)


def triangle_sierpinsky(longueur: int, repetitions: int) -> None:
    """Dessine un triangle de Sierpinsky de la longueur donnée

    Args:
        longueur (int): la longueur des côtés du triangle
        repetitions (int): le nombre de répétitions
    """
    if repetitions == 0:
        for i in range(3):
            forward(longueur)
            left(120)
    else:
        triangle_sierpinsky(longueur / 2, repetitions - 1)
        forward(longueur / 2)
        triangle_sierpinsky(longueur / 2, repetitions - 1)
        backward(longueur / 2)
        left(60)
        forward(longueur / 2)
        right(60)
        triangle_sierpinsky(longueur / 2, repetitions - 1)
        left(60)
        backward(longueur / 2)
        right(60)


# Exemple d'utilisation
if __name__ == "__main__":
    speed(0)
    # flocon_koch(300, 4)
    # for i in range(3):
        # flocon_koch(300, 4)
        # right(120)
    mainloop()

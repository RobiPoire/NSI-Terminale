"""
La récurssivité - Exercice 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Etude d'une fonction récursive.
"""

__author__ = "RobiPoire"


def f(a, b):
    if (b == 1):
        return a
    return a + f(a, b-1)


# 1) 12

# 2) La valeur retournée est la somme de a et de b fois a

# 3) Le cas de base est b = 1

# 4) Le programme s'arrête quand b = 1

# 5) La complexité est linéaire


# Dédicasse à copilot qui a fait le travail à ma place :p

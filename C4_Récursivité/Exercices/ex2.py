"""
La récurssivité - Exercice 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fonction mystère 2.
"""

__author__ = "RobiPoire"


def mystere2(L):
    if len(L) == 1:
        return L[0]
    if L[0] < L[1]:
        L.pop(1)
    else:
        L.pop(0)
    return mystere2(L)

# Le but de la fonction est de garder le plus grand entier de la fiste L en supprimant les autres éléments de la liste
# L La fonction retoume le plus grand entier de la liste L La fonction est récursive.

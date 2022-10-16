"""
La récurssivité - Exercice 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fonction mystère 1.
"""

__author__ = "RobiPoire"


def mystere(L, M=[]):
    if not L:
        return M
    a = L.pop(0)
    if a not in M:
        M. append(a)
    return mystere(L, M)

# Le but de la fonction est de retourner une liste des éléments qui sont dans L mais pas dans M.

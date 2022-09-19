"""
Les piles - Exercice Bonus 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implémenter en Python les opérations classiques sur les piles à l'aide d'un tableau que l'on
"simulera" à l'aide d'une liste. On supposera que le tableau a une taille fixe, par exemple 10.
"""

__author__ = "RobiPoire"


# Importation des fonctions de l'exercice 2 sur les piles dans le dossier parent
import sys
sys.path.append("..")
import Piles_Ex2 as Piles


# Taille de la pile maximale
Piles.n = 6


def hauteur_pile(P: list) -> int:
    """Renvoie la hauteur de la pile

    Args:
        P (list): La pile

    Returns:
        int: La hauteur de la pile
    """
    Q = Piles.CREER_PILE_VIDE()
    hauteur = 0
    while not (Piles.EST_VIDE(P)):
        hauteur += 1
        x = Piles.DEPILER(P)
        Piles.EMPILER(Q, x)
    while not (Piles.EST_VIDE(Q)):
        x = Piles.DEPILER(Q)
        Piles.EMPILER(P, x)
    return hauteur


def max_pile(P: list, i: int) -> int:
    """Renvoie la position du plus grand élément de la pile P parmi les i premiers éléments

    Args:
        P (list): La pile
        i (int): La position de l'élément à comparer

    Raises:
        IndexError: Si la pile n'a pas assez d'éléments
        IndexError: Si i est inférieur à 1

    Returns:
        int: La position du plus grand élément de la pile P parmi les i premiers éléments
    """
    if i > hauteur_pile(P):
        raise IndexError("La pile n'a pas assez d'éléments")
    if i < 1:
        raise IndexError("La position de départ doit être supérieur à 0")
    Q = Piles.CREER_PILE_VIDE()
    max = 0
    pos = 0
    for j in range(i):
        x = Piles.DEPILER(P)
        Piles.EMPILER(Q, x)
        if x > max:
            max = x
            pos = j + 1
    while not (Piles.EST_VIDE(Q)):
        x = Piles.DEPILER(Q)
        Piles.EMPILER(P, x)
    return pos


def retourner(P: list, j: int) -> None:
    """Inverse l'ordre des j premiers éléments de la pile P

    Args:
        P (list): La pile
        j (int): Le nombre d'éléments à inverser

    Raises:
        IndexError: Si la pile n'a pas assez d'éléments
        IndexError: Si j est inférieur à 1
    """
    if j > hauteur_pile(P):
        raise IndexError("La pile n'a pas assez d'éléments")
    if j < 1:
        raise IndexError("Il faut au moins 1 élément pour inverser")
    Q = Piles.CREER_PILE_VIDE()
    R = Piles.CREER_PILE_VIDE()
    for i in range(j):
        Piles.EMPILER(Q, Piles.DEPILER(P))
    while not (Piles.EST_VIDE(Q)):
        Piles.EMPILER(R, Piles.DEPILER(Q))
    while not (Piles.EST_VIDE(R)):
        Piles.EMPILER(P, Piles.DEPILER(R))


def tri_crepes(P: list) -> None:
    """Tri les crepes de la pile P

    Args:
        P (list): La pile

    Raises:
        IndexError: Si la pile est vide
    """
    if hauteur_pile(P) < 2:
        raise IndexError("Il faut au moins 2 crépes pour trier")
    h = hauteur_pile(P)
    for i in range(h):
        pos = max_pile(P, h-i)
        retourner(P, pos)
        retourner(P, h-i)


#! Exemple d'utilisation
# Se lance uniquement si le fichier est exécuté
if __name__ == "__main__":

    # Test de la fonction hauteur_pile
    P = [5, 8, 5, 2, 4, 0, 0]
    print(hauteur_pile(P))
    print(P)

    # Test de la fonction max_pile
    print(max_pile(P, 2))
    print(P)

    # Test de la fonction retourner
    retourner(P, 3)
    print(P)

    # Test de la fonction tri_crepes
    P = [6, 8, 5, 12, 14, 7, 0]
    tri_crepes(P)
    print(P)

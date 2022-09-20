"""
Les piles - Exercice Bonus 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implémenter en Python les opérations classiques sur les piles à l'aide d'un tableau que l'on
"simulera" à l'aide d'une liste. On supposera que le tableau a une taille fixe, par exemple 10.
"""

__author__ = "RobiPoire"


import ex2 as Piles


# Taille de la pile maximale
Piles.N = 6


def hauteur_pile(pile: list) -> int:
    """Renvoie la hauteur de la pile

    Args:
        pile (list): La pile

    Returns:
        int: La hauteur de la pile
    """
    pile_temp = Piles.creer_pile_vide()
    hauteur = 0
    while not (Piles.est_vide(pile)):
        hauteur += 1
        element = Piles.depiler(pile)
        Piles.empiler(pile_temp, element)
    while not (Piles.est_vide(pile_temp)):
        element = Piles.depiler(pile_temp)
        Piles.empiler(pile, element)
    return hauteur


def max_pile(pile: list, indice: int) -> int:
    """Renvoie la position de l'élément le plus grand de la pile

    Args:
        pile (list): La pile
        indice (int): L'indice maximum à prendre en compte

    Raises:
        IndexError: Si la pile est vide
        IndexError: Si l'indice est inférieur à 1

    Returns:
        int: La position de l'élément le plus grand de la pile
    """
    if indice > hauteur_pile(pile):
        raise IndexError("La pile n'a pas assez d'éléments")
    if indice < 1:
        raise IndexError("La position de départ doit être supérieur à 0")
    pile_temp = Piles.creer_pile_vide()
    maximum = 0
    position = 0
    for i in range(indice):
        element = Piles.depiler(pile)
        Piles.empiler(pile_temp, element)
        if element > maximum:
            maximum = element
            position = i + 1
    while not (Piles.est_vide(pile_temp)):
        element = Piles.depiler(pile_temp)
        Piles.empiler(pile, element)
    return position


def retourner(pile: list, j: int) -> None:
    """Retourne les j premières crêpes de la pile

    Args:
        pile (list): La pile
        j (int): Le nombre de crêpes à retourner

    Raises:
        IndexError: Si la pile est vide
        IndexError: Si j est inférieur à 1
    """
    if j > hauteur_pile(pile):
        raise IndexError("La pile n'a pas assez d'éléments")
    if j < 1:
        raise IndexError("Il faut au moins 1 élément pour inverser")
    pile_temp = Piles.creer_pile_vide()
    pile_temp_2 = Piles.creer_pile_vide()
    for i in range(j):
        Piles.empiler(pile_temp, Piles.depiler(pile))
    while not (Piles.est_vide(pile_temp)):
        Piles.empiler(pile_temp_2, Piles.depiler(pile_temp))
    while not (Piles.est_vide(pile_temp_2)):
        Piles.empiler(pile, Piles.depiler(pile_temp_2))


def tri_crepes(pile: list) -> None:
    """Tri les crêpes de la pile

    Args:
        pile (list): La pile

    Raises:
        IndexError: Si la pile est vide
    """
    if hauteur_pile(pile) < 2:
        raise IndexError("Il faut au moins 2 crépes pour trier")
    hauteur = hauteur_pile(pile)
    for i in range(hauteur):
        position = max_pile(pile, hauteur-i)
        retourner(pile, position)
        retourner(pile, hauteur-i)


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

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

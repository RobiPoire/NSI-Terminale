"""
Les piles - Exercice 6 Question 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implémenter en Python les opérations classiques sur les piles à l'aide d'un tableau que l'on
"simulera" à l'aide d'une liste. On supposera que le tableau a une taille fixe, par exemple 10.
"""

__author__ = "RobiPoire"


import ex2 as Pile


# Taille maximale des piles
Pile.N = 6


def hauteur_pile(pile: list) -> int:
    """Renvoie la hauteur de la pile

    Args:
        pile (list): La pile

    Returns:
        int: La hauteur de la pile
    """
    pile_temp = Pile.creer_pile_vide()  # On crée une pile temporaire
    hauteur = 0  # On initialise la hauteur à 0
    while not (Pile.est_vide(pile)):  # Tant que la pile n'est pas vide
        hauteur += 1
        # On dépile l'élément en le stockant dans une variable
        element = Pile.depiler(pile)
        # On ré-empile l'élément dans la pile temporaire
        Pile.empiler(pile_temp, element)
    # Tant que la pile temporaire n'est pas vide on ré-empile les éléments dans la pile de base
    while not (Pile.est_vide(pile_temp)):
        element = Pile.depiler(pile_temp)
        Pile.empiler(pile, element)
    # retourne la hauteur de la pile (sans modifier la pile de base)
    return hauteur


def max_pile(pile: list, indice: int) -> int:
    """Renvoie la position de l'élément le plus grand de la pile jusqu'à l'indice

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
    pile_temp = Pile.creer_pile_vide()  # On crée une pile temporaire
    maximum = 0
    position = 0
    for i in range(indice):  # On parcourt la pile jusqu'à l'indice
        element = Pile.depiler(pile)  # On dépile l'élément
        # On empile l'élément dans la pile temporaire
        Pile.empiler(pile_temp, element)
        if element > maximum:
            maximum = element
            position = i + 1
    # Tant que la pile temporaire n'est pas vide, on ré-empile les éléments dans la pile de base
    while not (Pile.est_vide(pile_temp)):
        element = Pile.depiler(pile_temp)
        Pile.empiler(pile, element)
    return position  # On retourne la position le plus grand de la pile jusqu'à l'indice


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
    pile_temp = Pile.creer_pile_vide()  # On crée une pile temporaire
    pile_temp_2 = Pile.creer_pile_vide()  # On crée une deuxième pile temporaire
    for i in range(j):  # On parcourt la pile jusqu'à j
        # On dépile et on empile dans la pile temporaire
        Pile.empiler(pile_temp, Pile.depiler(pile))
    while not (Pile.est_vide(pile_temp)):  # Tant que la pile temporaire n'est pas vide
        # On dépile et on empile dans la deuxième pile temporaire
        Pile.empiler(pile_temp_2, Pile.depiler(pile_temp))
    # Tant que la deuxième pile temporaire n'est pas vide
    while not (Pile.est_vide(pile_temp_2)):
        # On dépile et on empile dans la pile de base
        Pile.empiler(pile, Pile.depiler(pile_temp_2))


def tri_crepes(pile: list) -> None:
    """Tri les crêpes de la pile

    Args:
        pile (list): La pile

    Raises:
        IndexError: Si la pile est vide
    """
    if hauteur_pile(pile) < 2:  # Si la pile a moins de 2 éléments on ne peut pas trier
        raise IndexError("Il faut au moins 2 crépes pour trier")
    hauteur = hauteur_pile(pile)  # On récupère la hauteur de la pile
    for i in range(hauteur):  # On parcourt toute la pile
        # On récupère la position de l'élément le plus grand
        position = max_pile(pile, hauteur-i)
        # On retourne les éléments jusqu'à la position
        retourner(pile, position)
        # On retourne les éléments jusqu'à la hauteur-i
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

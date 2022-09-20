"""
Les piles - Exercice 2
~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait pile implémentées en Python
"""

__author__ = "RobiPoire"

# La taille maximum de la pile
N = 4


def creer_pile_vide() -> list:
    """Crée une pile vide de taille N

    Returns:
        list: Une pile vide de taille N
    """
    return [1]+[0]*(N)


def empiler(pile: list, element: object) -> None:
    """Empile un élément dans la pile

    Args:
        pile (list): La pile
        element (object): L'élément à empiler

    Raises:
        IndexError: Si la pile est pleine
    """
    if est_pleine(pile):
        raise IndexError("Pile pleine")
    pile[pile[0]] = element
    pile[0] += 1


def depiler(pile: list) -> object:
    """Dépile un élément de la pile

    Args:
        pile (list): La pile

    Raises:
        IndexError: Si la pile est vide

    Returns:
        object: L'élément dépiler
    """
    if est_vide(pile):
        raise IndexError("Pile vide")
    sommet = pile[pile[0]-1]
    pile[0] -= 1
    return sommet


def est_vide(pile: list) -> bool:
    """Vérifie si la pile est vide

    Args:
        pile (list): La pile

    Returns:
        bool: True si la pile est vide, False sinon
    """
    return pile[0] == 1


def est_pleine(pile: list) -> bool:
    """Vérifie si la pile est pleine

    Args:
        pile (list): La pile

    Returns:
        bool: True si la pile est pleine, False sinon
    """
    return pile[0] == N+1


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # Création d'une pile vide
    P = creer_pile_vide()

    # Empiler des éléments
    print(f"P= {P}")
    empiler(P, 3)
    print(f"P= {P}")
    empiler(P, 2)
    print(f"P= {P}")

    # Dépiler un élément
    N = depiler(P)
    print(f"N= {N}")
    print(f"P= {P}")

    # Empiler des éléments
    empiler(P, 5)
    print(f"P= {P}")
    empiler(P, 7)
    print(f"P= {P}")
    empiler(P, 9)
    print(f"P= {P}")

    # Dépiler un élément
    N = depiler(P)
    print(f"N= {N}")
    print(f"P= {P}")

"""
Les piles - Exercice 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Proposer une implémentation des opérations classiques de la pile à l'aide des méthodes .pop() 
et .append() du type liste de Python.
"""

__author__ = "RobiPoire"


def CREER_PILE_VIDE() -> list:
    """Crée une pile vide

    Returns:
        list: Une pile vide
    """
    return [0]


def EMPILER(P: list, e: object) -> None:
    """Empile un élément

    Args:
        P (list): La pile
        e (object): L'élément à empiler

    Raises:
        IndexError: Si la pile est pleine
    """
    P[0] += 1
    P.append(e)


def DEPILER(P: list) -> object:
    """Dépile un élément

    Args:
        P (list): La pile

    Raises:
        IndexError: Si la pile est vide

    Returns:
        object: L'élément dépiler
    """
    if EST_VIDE(P):
        raise IndexError("Pile vide")
    P[0] -= 1
    return P.pop()


def EST_VIDE(P: list) -> bool:
    """Vérifie si la pile est vide

    Args:
        P (list): La pile

    Returns:
        bool: True si la pile est vide, False sinon
    """
    return P[0] <= 0


#! Exemple d'utilisation
# Se lance uniquement si le fichier est exécuté
if __name__ == "__main__":

    # Ici la pile n'a pas de taille maximale

    # Création d'une pile vide
    P = CREER_PILE_VIDE()

    # Empiler des éléments
    print(f"P= {P}")
    EMPILER(P, 3)
    print(f"P= {P}")
    EMPILER(P, 2)
    print(f"P= {P}")

    # Dépiler un élément
    N = DEPILER(P)
    print(f"N= {N}")
    print(f"P= {P}")

    # Empiler des éléments
    EMPILER(P, 5)
    print(f"P= {P}")
    EMPILER(P, 7)
    print(f"P= {P}")
    EMPILER(P, 9)
    print(f"P= {P}")

    # Dépiler un élément
    N = DEPILER(P)
    print(f"N= {N}")
    print(f"P= {P}")

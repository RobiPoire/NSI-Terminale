"""
Les piles - Exercice 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implémenter en Python les opérations classiques sur les piles à l'aide d'un tableau que l'on
"simulera" à l'aide d'une liste. On supposera que le tableau a une taille fixe, par exemple 10.
"""

__author__ = "RobiPoire"

# La taille maximum de la pile
n = 4


def CREER_PILE_VIDE() -> list:
    """Crée une pile vide de taille n

    Returns:
        list: Une pile vide de taille n
    """
    return [1]+[0]*(n)


def EMPILER(P: list, e: object) -> None:
    """Empile un élément

    Args:
        P (list): La pile
        e (object): L'élément à empiler

    Raises:
        IndexError: Si la pile est pleine
    """
    if EST_PLEINE(P):
        raise IndexError("Pile pleine")
    P[P[0]] = e
    P[0] += 1


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
    sommet = P[P[0]-1]
    P[0] -= 1
    return sommet


def EST_VIDE(P: list) -> bool:
    """Vérifie si la pile est vide

    Args:
        P (list): La pile

    Returns:
        bool: True si la pile est vide, False sinon
    """
    return P[0] == 1


def EST_PLEINE(P: list) -> bool:
    """Vérifie si la pile est pleine

    Args:
        P (list): La pile

    Returns:
        bool: True si la pile est pleine, False sinon
    """
    return P[0] == n+1


#! Exemple d'utilisation
# Se lance uniquement si le fichier est exécuté
if __name__ == "__main__":
    
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

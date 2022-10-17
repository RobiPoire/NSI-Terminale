"""
La récurssivité - Rendu de monnaie
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Algorithme de rendu de monnaie.
"""

__author__ = "RobiPoire"


def rendu_monnaie(somme: int, i: int = 0, pieces: list = [100, 50, 20, 10, 5, 2, 1]) -> list:
    """Retourne la liste des pièces à rendre

    Args:
        somme (int): La somme à rendre
        i (int, optional): L'indice de la pièce. 0 par défaut.
        pieces (list, optional): La liste des pièces. [100, 50, 20, 10, 5, 2, 1] par défaut.

    Returns:
        list: La liste des pièces à rendre
    """
    if somme == 0:
        return []
    if somme >= pieces[i]:
        return [pieces[i]] + rendu_monnaie(somme - pieces[i], i, pieces)
    return rendu_monnaie(somme, i + 1, pieces)


if __name__ == "__main__":
    print(rendu_monnaie(123))
    print(rendu_monnaie(1812))

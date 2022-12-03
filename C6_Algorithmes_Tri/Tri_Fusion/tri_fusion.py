"""
Tri Fusion
~~~~~~~~~~
Le tri fusion est un algorithme de tri qui consiste à diviser la liste à trier en deux
"""

__author__ = "RobiPoire"


def interclassement(liste1: list, liste2: list) -> list:
    """Fonction qui interclasse deux listes triées en une seule liste triée

    Args:
        liste1 (list): première liste triée
        liste2 (list): deuxième liste triée

    Returns:
        list: liste triée
    """
    if liste1 == []:
        return liste2
    elif liste2 == []:
        return liste1
    elif liste1[0] <= liste2[0]:
        return [liste1[0]] + interclassement(liste1[1:], liste2)
    else:
        return [liste2[0]] + interclassement(liste1, liste2[1:])


def tri_fusion(liste: list) -> list:
    """Fonction qui trie une liste par la méthode du tri fusion

    Args:
        liste (list): liste à trier

    Returns:
        list: liste triée
    """
    if len(liste) <= 1:
        return liste
    else:
        milieu = len(liste) // 2
        return interclassement(tri_fusion(liste[:milieu]), tri_fusion(liste[milieu:]))


def complexite_tri_fusion(n: int) -> int:
    """Fonction qui calcule la complexité du tri fusion

    Args:
        n (int): taille de la liste à trier

    Returns:
        int: complexité du tri fusion
    """
    if n <= 1:
        return 0
    else:
        milieu = n // 2
        return complexite_tri_fusion(milieu) + complexite_tri_fusion(n - milieu) + n


if __name__ == "__main__":
    print(interclassement([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
    print(tri_fusion([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))
    print(complexite_tri_fusion(10))
    # Complexité en O(n log n)

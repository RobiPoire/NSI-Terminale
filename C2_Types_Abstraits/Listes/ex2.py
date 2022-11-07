"""
Les listes - Exercice 2
~~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait liste implémentées en Python
"""

__author__ = "RobiPoire & LythoPsycho"

from typing import Any


# La taille maximum de la liste
N = 5


def creer_liste_vide() -> list:
    """Crée une liste vide de taille N

    Raises:
        ValueError: Si N est inférieur à 1

    Returns:
        list: Une liste vide de taille N
    """
    if N < 1:
        raise ValueError("n doit être supérieur à 0")
    # On crée une liste de taille N+1 avec la longueur de la liste en index 0
    return [0] * (N + 1)


def inserer(liste: list, element: Any, index: int) -> None:
    """Insère un élément à l'index donné dans la liste

    Args:
        liste (list): La liste
        element (Any): L'élément à insérer
        index (int): L'index où insérer l'élément

    Raises:
        IndexError: Si la liste est pleine
        IndexError: Si l'index est inférieur à 1
    """
    if index == 0:
        raise IndexError(  # On ne peut pas modifier la longueur de la liste
            "L'index 0 est réservé pour la longueur de la liste"
        )
    if est_plein(liste):  # On ne peut pas insérer dans une liste pleine
        raise IndexError("Liste pleine")
    liste[0] += 1
    # Tout ce qui est après l'index i = tout ce qui est après l'index i-1 + [0]
    for i in range(longueur(liste), index, -1):
        liste[i] = liste[i - 1]
    liste[index] = element


def supprimer(liste: list, index: int) -> None:
    """Supprime un élément à l'index donné dans la liste

    Args:
        liste (list): La liste
        index (int): L'index où supprimer l'élément

    Raises:
        IndexError: Si l'index est inférieur à 1
        IndexError: Si la liste est vide
    """
    if index == 0:
        raise IndexError(  # On ne peut pas modifier la longueur de la liste
            "L'index 0 est réservé pour la longueur de la liste"
        )
    if est_vide(liste):  # On ne peut pas supprimer dans une liste vide
        raise IndexError("Liste vide")
    liste[0] -= 1
    # Tout ce qui est après l'index i = tout ce qui est après l'index i+1 + [0]
    for i in range(index, longueur(liste) + 1):
        liste[i] = liste[i + 1]
    liste[liste[0] + 1] = 0


def rechercher(liste: list, element: Any) -> int:
    """Recherche un élément dans la liste

    Args:
        liste (list): La liste
        element (Any): L'élément à rechercher

    Raises:
        ValueError: Si l'élément n'est pas dans la liste

    Returns:
        int: L'index de l'élément
    """
    index = 0
    for i in range(1, len(liste)):
        index += 1
        if lire(liste, i) == element:
            return index
    # Si rien n'a été trouvé, l'élément n'est pas dans la liste
    raise ValueError("L'élément n'est pas dans la liste")


def lire(liste: list, index: int) -> Any:
    """Lit un élément à l'index donné dans la liste

    Args:
        liste (list): La liste
        index (int): L'index où lire l'élément

    Raises:
        IndexError: Si l'index est inférieur à 1

    Returns:
        Any: L'élément à l'index donné
    """
    if index == 0:  # L'index 0 est réservé pour la longueur de la liste
        raise IndexError("L'index 0 est est réservé pour la longueur de la liste")
    return liste[index]


def modifier(liste: list, element: Any, index: int) -> None:
    """Modifie un élément à l'index donné dans la liste

    Args:
        liste (list): La liste
        element (Any): L'élément à modifier
        index (int): L'index où modifier l'élément

    Raises:
        IndexError: Si l'index est inférieur à 1
    """
    if index == 0:  # L'index 0 est réservé pour la longueur de la liste
        raise IndexError("L'index 0 est est réservé pour la longueur de la liste")
    liste[index] = element


def longueur(liste: list) -> int:
    """Retourne la longueur de la liste

    Args:
        liste (list): La liste

    Returns:
        int: La longueur de la liste
    """
    return liste[0]


def est_vide(liste: list) -> bool:
    """Retourne si la liste est vide

    Args:
        liste (list): La liste

    Returns:
        bool: True si la liste est vide, False sinon
    """
    return liste[0] <= 0


def est_plein(liste: list) -> bool:
    """Retourne si la liste est pleine

    Args:
        liste (list): La liste

    Returns:
        bool: True si la liste est pleine, False sinon
    """
    return liste[0] >= N


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # Création de la liste
    L1 = creer_liste_vide()

    # Insertion d'éléments
    inserer(L1, 1, 1)
    print(f"INSERER(L1, 1, 1) -> {L1}")
    inserer(L1, 2, 2)
    print(f"INSERER(L1, 2, 2) -> {L1}")
    inserer(L1, 3, 3)
    print(f"INSERER(L1, 3, 3) -> {L1}")
    inserer(L1, 8, 1)
    print(f"INSERER(L1, 8, 1) -> {L1}")
    inserer(L1, 12, 5)
    print(f"INSERER(L1, 8, 1) -> {L1}")

    # Modification d'éléments
    modifier(L1, 6, 1)
    print(f"MODIFIER(L1, 6, 1) -> {L1}")

    # Lecture d'éléments
    print(f"LIRE(L1, 1) -> {lire(L1, 1)}")

    # Suppression d'éléments
    supprimer(L1, 1)
    print(f"SUPPRIMER(L1, 1) -> {L1}")

    # Recherche d'éléments
    print(f"RECHERCHER(L1, 2) -> {rechercher(L1, 2)}")

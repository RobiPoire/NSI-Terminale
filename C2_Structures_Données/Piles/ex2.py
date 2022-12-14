"""
Les piles - Exercice 2
~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait pile implémentées en Python
"""

__author__ = "RobiPoire"

from typing import Any


# Taille maximale des piles
N = 4


def creer_pile_vide() -> list:
    """Crée une pile vide de taille N

    Returns:
        list: Une pile vide de taille N
    """
    return [1] + [0] * (N)


def empiler(pile: list, element: Any) -> None:
    """Empile un élément dans la pile

    Args:
        pile (list): La pile
        element (Any): L'élément à empiler

    Raises:
        IndexError: Si la pile est pleine
    """
    if est_pleine(pile):  # Si la pile est pleine, on ne peut pas empiler
        raise IndexError(
            f"La pile est pleine, impossible d'empiler '{element}' (taille max: {N})"
        )
    pile[pile[0]] = element  # On ajoute l'élément à la pile
    pile[0] += 1  # On ajoute 1 à l'indice du sommet


def depiler(pile: list) -> Any:
    """Dépile un élément de la pile

    Args:
        pile (list): La pile

    Raises:
        IndexError: Si la pile est vide

    Returns:
        Any: L'élément dépiler
    """
    if est_vide(pile):  # Si la pile est vide, on ne peut rien dépiler
        raise IndexError("La pile est vide, impossible de dépiler un élément")
    pile[0] -= 1  # On enlève 1 à l'indice du sommet
    return pile[pile[0]]  # On retourne l'élément à la tête de la pile


def est_vide(pile: list) -> bool:
    """Vérifie si la pile est vide

    Args:
        pile (list): La pile

    Returns:
        bool: True si la pile est vide, False sinon
    """
    return (
        pile[0] <= 1
    )  # Si l'indice du sommet est inférieur ou égal à 1, la pile est vide


def est_pleine(pile: list) -> bool:
    """Vérifie si la pile est pleine

    Args:
        pile (list): La pile

    Returns:
        bool: True si la pile est pleine, False sinon
    """
    return (
        pile[0] >= N + 3
    )  # Si l'indice du sommet est supérieur ou égal à N+3, la pile est pleine


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # Création d'une pile vide
    pile = creer_pile_vide()

    # Empiler des éléments
    print(f"pile = {pile}")
    empiler(pile, 3)
    print(f"pile = {pile}")
    empiler(pile, 2)
    print(f"pile = {pile}")

    # Dépiler un élément
    valeur = depiler(pile)
    print(f"valeur = {valeur}")
    print(f"pile = {pile}")

    # Empiler des éléments
    empiler(pile, 5)
    print(f"pile = {pile}")
    empiler(pile, 7)
    print(f"pile = {pile}")
    empiler(pile, 9)
    print(f"pile = {pile}")

    # Dépiler un élément
    valeur = depiler(pile)
    print(f"valeur = {valeur}")
    print(f"pile = {pile}")

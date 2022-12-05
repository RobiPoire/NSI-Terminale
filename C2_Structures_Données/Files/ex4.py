"""
Les files - Exercice 4
~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait file implémentées en Python 
avec les méthodes .pop() et .append() du type liste de Python
"""


__author__ = "RobiPoire"

from typing import Any

# La taille maximum de la file
N = 7


def creer_file_vide() -> list:
    """Crée une file vide

    Returns:
        list: Une file vide
    """
    # On créer juste une liste python vide
    return []


def enfiler(file: list, element: Any):
    """Enfile un élément dans la file

    Args:
        file (list): La file
        element (Any): L'élément à enfiler

    Raises:
        IndexError: Si la file est pleine
    """
    if est_pleine(file):  # Si la file est pleine, on ne peut rien enfiler
        raise IndexError(
            f"La file est pleine, impossible d'enfiler '{element}' (taille max: {N})"
        )
    # On ajoute l'élément à la fin de la file
    file.append(element)


def defiler(file: list) -> Any:
    """Défile un élément de la file

    Args:
        file (list): La file

    Raises:
        IndexError: Si la file est vide

    Returns:
        Any: L'élément défilé
    """
    if est_vide(file):  # Si la file est vide, on ne peut rien défiler
        raise IndexError("La file est vide, impossible de défiler un élément")
    # on enlève le premier élément de la file et on le retourne
    return file.pop(0)


def est_vide(file: list) -> bool:
    """Vérifie si la file est vide

    Args:
        file (list): La file

    Returns:
        bool: True si la file est vide, False sinon
    """
    # On vérifie si la file est vide en vérifiant si sa taille est égale à 0
    return len(file) == 0


def est_pleine(file: list) -> bool:
    """Vérifie si la file est pleine

    Args:
        file (list): La file

    Returns:
        bool: True si la file est pleine, False sinon
    """
    # On vérifie si la file est pleine en vérifiant si sa taille est supérieur ou égale à N
    return len(file) >= N


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # Création de la file
    file = creer_file_vide()

    # Enfiler des éléments
    print(f"file = {file}")
    enfiler(file, 21)
    print(f"file = {file}")
    enfiler(file, 22)
    print(f"file = {file}")
    enfiler(file, 23)
    print(f"file = {file}")
    enfiler(file, 24)
    print(f"file = {file}")
    enfiler(file, 25)
    print(f"file = {file}")
    enfiler(file, 26)
    print(f"file = {file}")

    # Défiler un élément
    element = defiler(file)
    print(f"element = {element}")
    print(f"file = {file}")

    # Enfiler des éléments
    enfiler(file, 27)
    print(f"file = {file}")
    enfiler(file, 28)
    print(f"file = {file}")

    # Défiler un élément
    element = defiler(file)
    print(f"element = {element}")
    print(f"file = {file}")

    # Enfiler un élément
    enfiler(file, 29)
    print(f"file = {file}")

    # Défiler un élément x7
    for i in range(7):
        element = defiler(file)
        print(f"element = {element}")
        print(f"file = {file}")

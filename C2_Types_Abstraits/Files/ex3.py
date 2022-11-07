"""
Les files - Exercice 3
~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait file implémentées en Python
"""

__author__ = "RobiPoire"


from typing import Any

# La taille maximum de la file
N = 7


def creer_file_vide() -> list:
    """Crée une file vide de taille N

    Returns:
        list: Une file vide
    """
    # On crée une file avec une tête, une queue, une taille et N cases pour les éléments
    return [3, 3, 0] + [0] * N


def enfiler(file: list, element: Any) -> None:
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
    # On ajoute l'élément à la queue de la file
    file[file[1]] = element
    # On ajoute 1 à la taille de la file
    file[2] += 1
    # On ajoute 1 à l'indice de la tête sauf si la queue est à la fin de la file (on la remet à 3)
    file[1] = 3 if file[1] == N + 2 else file[1] + 1


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
    # On récupère l'élément à la tête de la file
    element = file[file[0]]
    # On retire 1 à la tête de la file sauf si la tête est à la fin de la file (on la remet à 3)
    file[0] = 3 if file[0] == N + 2 else file[0] + 1
    # On retire 1 à la taille de la file
    file[2] -= 1
    # On retourne l'élément défilé
    return element


def est_vide(file: list) -> bool:
    """Vérifie si la file est vide

    Args:
        file (list): La file

    Returns:
        bool: True si la file est vide, False sinon
    """
    # On vérifie si la taille de la file est inférieur ou égale à 0
    return file[2] <= 0


def est_pleine(file: list) -> bool:
    """Vérifie si la file est pleine

    Args:
        file (list): La file

    Returns:
        bool: True si la file est pleine, False sinon
    """
    # On vérifie si la taille de la file est supérieur ou égale à N
    return file[2] >= N


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
    enfiler(file, 29)
    print(f"file = {file}")

    # Défiler un élément
    element = defiler(file)
    print(f"element = {element}")
    print(f"file = {file}")

    # Enfiler un élément
    enfiler(file, 26)
    print(f"file = {file}")

    # Défiler un élément x7
    for i in range(7):
        element = defiler(file)
        print(f"element = {element}")
        print(f"file = {file}")

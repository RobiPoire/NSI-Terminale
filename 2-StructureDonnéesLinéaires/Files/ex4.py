"""
Les files - Exercice 4
~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait file implémentées en Python 
avec les méthodes .pop() et .append() du type liste de Python
"""


__author__ = "RobiPoire"

# La taille maximum de la file
N = 4


def creer_file_vide() -> list:
    """Crée une file vide

    Returns:
        list: Une file vide
    """
    return []


def enfiler(file: list, element: object):
    """Enfile un élément dans la file

    Args:
        file (list): La file
        element (object): L'élément à enfiler

    Raises:
        IndexError: Si la file est pleine
    """
    if est_pleine(file):
        raise IndexError("La file est pleine")
    file.append(element)


def defiler(file: list) -> object:
    """Défile un élément de la file

    Args:
        file (list): La file

    Raises:
        IndexError: Si la file est vide

    Returns:
        object: L'élément défilé
    """
    if est_vide(file):
        raise IndexError("La file est vide")
    return file.pop(0)


def est_vide(file: list) -> bool:
    """Vérifie si la file est vide

    Args:
        file (list): La file

    Returns:
        bool: True si la file est vide, False sinon
    """
    return len(file) == 0


def est_pleine(file: list) -> bool:
    """Vérifie si la file est pleine

    Args:
        file (list): La file

    Returns:
        bool: True si la file est pleine, False sinon
    """
    return len(file) == N


#! Exemple d'utilisation
# Se lance uniquement si le fichier est exécuté
if __name__ == "__main__":

    # Création de la file
    file = creer_file_vide()

    # Enfiler des éléments
    print(f"F = {file}")
    enfiler(file, 21)
    print(f"F = {file}")
    enfiler(file, 22)
    print(f"F = {file}")
    enfiler(file, 23)
    print(f"F = {file}")

    # Défiler un élément
    element = defiler(file)
    print(f"N = {element}")
    print(f"F = {file}")

    # Enfiler des éléments
    enfiler(file, 24)
    print(f"F = {file}")
    enfiler(file, 25)
    print(f"F = {file}")

    # Défiler un élément
    element = defiler(file)
    print(f"N = {element}")
    print(f"F = {file}")

    # Enfiler un élément
    enfiler(file, 26)
    print(f"F = {file}")

    # Défiler un élément
    element = defiler(file)
    print(f"N = {element}")
    print(f"F = {file}")

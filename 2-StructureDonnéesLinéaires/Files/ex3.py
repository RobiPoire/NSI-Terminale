"""
Les files - Exercice 3
~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait file implémentées en Python
"""

__author__ = "RobiPoire"

# La taille maximum de la file
N = 4


def creer_file_vide() -> list:
    """Crée une file vide de taille N

    Returns:
        list: Une file vide
    """    
    return [3, 3, 0]+[0]*N


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
    # Si la queue dépasse la taille du tableau, on la ramène au début du tableau en décalant la tête
    if file[1] == N + 3:
        file[0] = 3
        file[1] = file[2]+3
        for i in range(file[2]):
            file[i+3] = file[i+4]
    file[2] += 1
    file[file[1]] = element
    file[1] += 1


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
    else:
        element = file[file[0]]
        file[file[0]] = 0
        file[2] -= 1
        file[0] += 1
        return element


def est_vide(file: list) -> bool:
    """Vérifie si la file est vide

    Args:
        file (list): La file

    Returns:
        bool: True si la file est vide, False sinon
    """
    return file[2] == 0


def est_pleine(file: list) -> bool:
    """Vérifie si la file est pleine

    Args:
        file (list): La file

    Returns:
        bool: True si la file est pleine, False sinon
    """
    return file[2] == N


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

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

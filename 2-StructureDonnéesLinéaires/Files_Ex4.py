"""
Les files - Exercice 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Proposer une implémentation des opérations classiques de la file à l'aide des méthodes .pop() 
et .append() du type liste de Python. Une file vide sera représentée par la liste vide. On pourra 
se donner arbitrairement une taille maximale pour la file, initialisée dans une variable globale, 
par exemple MAX = 10. 
On rappelle que, si F est une liste Python, L.pop(0) retourne l'élément d'indice 0 de F et le 
supprime de la liste. 
"""


__author__ = "RobiPoire"

# La taille maximum de la file
MAX = 4


def CREER_FILE_VIDE() -> list:
    """Crée une file vide

    Returns:
        list: Une file vide
    """
    return []


def ENFILER(F: list, e: object):
    """Enfile un élément dans une file

    Args:
        F (list): La file dans laquelle on veut enfiler l'élément
        e (object): L'élément à enfiler
    """
    if EST_PLEINE(F):
        raise IndexError("La file est pleine")
    F.append(e)


def DEFILER(F: list) -> object:
    """Défile un élément d'une file

    Args:
        F (list): La file dans laquelle on veut défiler l'élément

    Returns:
        object: L'élément défilé
    """
    if EST_VIDE(F):
        raise IndexError("La file est vide")
    return F.pop(0)


def EST_VIDE(F: list) -> bool:
    """Vérifie si une file est vide

    Args:
        F (list): La file à vérifier

    Returns:
        bool: True si la file est vide, False sinon
    """
    return len(F) == 0


def EST_PLEINE(F: list) -> bool:
    """Vérifie si une file est pleine

    Args:
        F (list): La file à vérifier

    Returns:
        bool: True si la file est pleine, False sinon
    """
    return len(F) == MAX


#! Exemple d'utilisation
# Se lance uniquement si le fichier est exécuté
if __name__ == "__main__":

    # Création de la file
    F = CREER_FILE_VIDE()

    # Enfiler des éléments
    print(f"F = {F}")
    ENFILER(F, 21)
    print(f"F = {F}")
    ENFILER(F, 22)
    print(f"F = {F}")
    ENFILER(F, 23)
    print(f"F = {F}")

    # Défiler un élément
    N = DEFILER(F)
    print(f"N = {N}")
    print(f"F = {F}")

    # Enfiler des éléments
    ENFILER(F, 24)
    print(f"F = {F}")
    ENFILER(F, 25)
    print(f"F = {F}")

    # Défiler un élément
    N = DEFILER(F)
    print(f"N = {N}")
    print(f"F = {F}")

    # Enfiler un élément
    ENFILER(F, 26)
    print(f"F = {F}")

    # Défiler un élément
    N = DEFILER(F)
    print(f"N = {N}")
    print(f"F = {F}")

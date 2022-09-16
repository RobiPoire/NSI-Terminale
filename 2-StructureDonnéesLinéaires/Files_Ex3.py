"""
Les files - Exercice 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implémenter en Python les opérations classiques sur les files à l'aide d'un tableau que l'on 
"simulera" à l'aide d'une liste. On supposera que le tableau a une taille fixe, par exemple 10. 
On gèrera ce tableau de façon circulaire : dès que les indices de tête ou de queue dépassent la 
longueur du tableau, ils repartent au début du tableau.
"""

__author__ = "RobiPoire"

# La taille maximum de la file
n = 4


def CREER_FILE_VIDE() -> list:
    """Crée une file vide de taille n

    Returns:
        list: Une file vide
    """
    return [3, 3, 0]+[0]*n


def ENFILER(F: list, e: object):
    """Enfile un élément dans une file

    Args:
        F (list): La file dans laquelle on veut enfiler l'élément
        e (object): L'élément à enfiler
    """
    if EST_PLEINE(F):
        raise IndexError("La file est pleine")
    # Si la queue dépasse la taille du tableau, on la ramène au début du tableau en décalant la tête
    if F[1] == n + 3:
        F[0] = 3
        F[1] = F[2]+3
        for i in range(F[2]):
            F[i+3] = F[i+4]
    F[2] += 1
    F[F[1]] = e
    F[1] += 1


def DEFILER(F: list) -> object:
    """Défile un élément d'une file

    Args:
        F (list): La file dans laquelle on veut défiler l'élément

    Returns:
        object: L'élément défilé
    """
    if EST_VIDE(F):
        raise IndexError("La file est vide")
    else:
        e = F[F[0]]
        F[F[0]] = 0
        F[2] -= 1
        F[0] += 1
        return e


def EST_VIDE(F: list) -> bool:
    """Vérifie si une file est vide

    Args:
        F (list): La file à vérifier

    Returns:
        bool: True si la file est vide, False sinon
    """
    return F[2] == 0


def EST_PLEINE(F: list) -> bool:
    """Vérifie si une file est pleine

    Args:
        F (list): La file à vérifier

    Returns:
        bool: True si la file est pleine, False sinon
    """
    return F[2] == n


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

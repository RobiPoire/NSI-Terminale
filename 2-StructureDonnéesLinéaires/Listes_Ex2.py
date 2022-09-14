"""
Les listes - Exercice 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implémenter en Python chaque fonction du type abstrait Liste.
"""
__author__ = "RobiPoire"


def CREER_LISTE_VIDE() -> list:
    """Crée une liste vide de taille n

    Raises:
        ValueError: Si n est inférieur à 1

    Returns:
        list : Une liste vide de taille n
    """
    if n == 0:
        raise ValueError("n doit être supérieur ou égale à 2")
    return [0] * (n+1)


def INSERER(L: list, e: object, i: int) -> None:
    """Insère un élément à l'index i

    Args:
        L (list): La liste
        e (NoneType): L'élément à insérer
        i (int): L'index où insérer l'élément

    Raises:
        IndexError: Si la liste est pleine
        IndexError: Si l'index est inférieur à 1 ou supérieur à la longueur de la liste
    """
    if i == 0:
        raise IndexError(
            "L'index 0 est est réservé pour la longueur de la liste")
    if EST_PLEIN(L):
        raise IndexError("Liste pleine")
    L[0] += 1
    # Tout ce qui est après l'index i = [e] + tout ce qui est après l'index i
    L[i:] = [e] + L[i:-1]


def SUPPRIMER(L: list, i: int) -> None:
    """Supprime un élément à l'index i

    Args:
        L (list): La liste
        i (int): L'index où supprimer l'élément

    Raises:
        IndexError: Si la liste est vide
        IndexError: Si l'index est inférieur à 1 ou supérieur à la longueur de la liste
    """
    if i == 0:
        raise IndexError(
            "L'index 0 est est réservé pour la longueur de la liste")
    if EST_VIDE(L):
        raise IndexError("Liste vide")
    L[0] -= 1
    # Tout ce qui est après l'index i = tout ce qui est après l'index i+1 + [0]
    L[i:] = L[i+1:] + [0]


def RECHERCHER(L: list, e: object) -> int:
    """Recherche un élément dans la liste

    Args:
        L (list): La liste
        e (object): L'élément à rechercher

    Raises:
        ValueError: Si l'élément n'est pas dans la liste

    Returns:
        int: L'index de l'élément recherché
    """
    i = 0
    for x in L[1:]:
        i += 1
        if x == e:
            return i
    raise ValueError("L'élément n'est pas dans la liste")


def LIRE(L: list, i: int) -> object:
    """Lit un élément à l'index i

    Args:
        L (list): La liste
        i (int): L'index où lire l'élément

    Raises:
        IndexError: Si l'index est inférieur à 1 ou supérieur à la longueur de la liste

    Returns:
        NoneType: L'élément à l'index i
    """
    if i == 0:
        raise IndexError(
            "L'index 0 est est réservé pour la longueur de la liste")
    return L[i]


def MODIFIER(L: list, e: object, i: int) -> None:
    """Modifie un élément à l'index i

    Args:
        L (list): La liste
        e (object): L'élément à modifier
        i (int): L'index où modifier l'élément

    Raises:
        IndexError: Si l'index est inférieur à 1 ou supérieur à la longueur de la liste
    """
    if i == 0:
        raise IndexError(
            "L'index 0 est est réservé pour la longueur de la liste")
    L[i] = e


def LONGUEUR(L: list) -> int:
    """Retourne la longueur de la liste

    Args:
        L (list): La liste

    Returns:
        int: La longueur de la liste
    """
    return L[0]


def EST_VIDE(L: list) -> bool:
    """Retourne si la liste est vide

    Args:
        L (list): La liste

    Returns:
        bool: Si la liste est vide ou non 
    """
    if L[0] == 0:
        return True


def EST_PLEIN(L: list) -> bool:
    """Retourne si la liste est pleine

    Args:
        L (list): La liste

    Returns:
        bool: Si la liste est pleine ou non
    """
    if L[0] == n:
        return True

#! Exemple d'utilisation


# Longueur des listes (en comptant l'index 0)
n = 5

# Création de la liste
L1 = CREER_LISTE_VIDE()

# Insertion d'éléments
INSERER(L1, 1, 1)
print(f"INSERER(L1, 1, 1) -> {L1}")
INSERER(L1, 2, 2)
print(f"INSERER(L1, 1, 1) -> {L1}")
INSERER(L1, 3, 3)
print(f"INSERER(L1, 1, 1) -> {L1}")
INSERER(L1, 8, 1)
print(f"INSERER(L1, 8, 1) -> {L1}")

# Modification d'éléments
MODIFIER(L1, 6, 1)
print(f"MODIFIER(L1, 6, 1) -> {L1}")

# Lecture d'éléments
print(f"LIRE(L1, 1) -> {LIRE(L1, 1)}")

# Suppression d'éléments
SUPPRIMER(L1, 1)
print(f"SUPPRIMER(L1, 1) -> {L1}")

# Recherche d'éléments
print(f"RECHERCHER(L1, 2) -> {RECHERCHER(L1, 2)}")

"""
Résultat :
>>> INSERER(L1, 1, 1) -> [1, 1, 0, 0, 0, 0]
>>> INSERER(L1, 1, 1) -> [2, 1, 2, 0, 0, 0]
>>> INSERER(L1, 1, 1) -> [3, 1, 2, 3, 0, 0]
>>> INSERER(L1, 8, 1) -> [4, 8, 1, 2, 3, 0]
>>> MODIFIER(L1, 6, 1) -> [4, 6, 1, 2, 3, 0]
>>> LIRE(L1, 1) -> 6
>>> SUPPRIMER(L1, 1) -> [3, 1, 2, 3, 0, 0]
>>> RECHERCHER(L1, 2) -> 2
"""

"""
Les dictionnaires - Exercice 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait dictionnaire implémentées en Python
"""

__auhtor__ = "RobiPoire"


N = 25


def creer_dictionnaire() -> tuple:
    """
    Créer un dictionnaire vide
    """
    return ([0] * N, [0] * N)


def hachage(cle: str) -> int:
    """ Hachage d'une clé en un entier entre 0 et N-1

    Args:
        cle (str): la clé à hacher

    Returns:
        int: la clé hachée
    """
    somme = 0
    for i in cle:
        somme += ord(i)
    return somme % N


def ajouter(dictionnaire: tuple, cle: str, valeur: object) -> None:
    """ Ajoute une valeur à un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé
        valeur (object): la valeur
    """
    cles, valeurs = dictionnaire
    cles[hachage(cle)] = cle
    valeurs[hachage(cle)] = valeur


def supprimer(dictionnaire: tuple, cle: str) -> None:
    """ Supprime une valeur d'un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé
    """
    cles, valeurs = dictionnaire
    cles[hachage(cle)] = 0
    valeurs[hachage(cle)] = 0


def lire(dictionnaire: tuple, cle: str) -> object:
    """ Lit une valeur d'un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé

    Returns:
        object: la valeur
    """
    valeurs = dictionnaire[1]
    return valeurs[hachage(cle)]


def modifier(dictionnaire: tuple, cle: str, valeur: object) -> None:
    """ Modifie une valeur d'un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé
        valeur (object): la valeur
    """
    ajouter(dictionnaire, cle, valeur)


def rechercher(dictionnaire: tuple, valeur: object) -> str | None:
    """ Recherche une clé à partir d'une valeur

    Args:
        dictionnaire (tuple): le dictionnaire
        valeur (object): la valeur

    Returns:
        str: la clé
    """
    cles, valeurs = dictionnaire
    for i in range(N):
        if valeurs[i] == valeur:
            return cles[i]
    return None 


dico = creer_dictionnaire()
ajouter(dico, "aaa", 42)
ajouter(dico, "ffff", 43)
ajouter(dico, "tttt", 44)
print(lire(dico, "aaa"))

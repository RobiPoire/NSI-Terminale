"""
Les dictionnaires - Exercice 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait dictionnaire implémentées en Python
"""

__auhtor__ = "RobiPoire"


from typing import Any


N = 25


def creer_dictionnaire() -> tuple:
    """
    Créer un dictionnaire vide
    """
    return ([0] * N, [0] * N)


def hachage(cle: str) -> int:
    """Hachage d'une clé en un entier entre 0 et N-1

    Args:
        cle (str): la clé à hacher

    Returns:
        int: la clé hachée
    """
    somme = 0
    for i in cle:
        somme += ord(i)
    return somme % N


def ajouter(dictionnaire: tuple, cle: str, valeur: Any) -> None:
    """Ajoute une valeur à un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé
        valeur (Any): la valeur
    """
    cles, valeurs = dictionnaire
    cles[hachage(cle)] = cle
    valeurs[hachage(cle)] = valeur


def supprimer(dictionnaire: tuple, cle: str) -> None:
    """Supprime une valeur d'un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé
    """
    cles, valeurs = dictionnaire
    cles[hachage(cle)] = 0
    valeurs[hachage(cle)] = 0


def lire(dictionnaire: tuple, cle: str) -> Any:
    """Lit une valeur d'un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé

    Returns:
        Any: la valeur
    """
    valeurs = dictionnaire[1]
    return valeurs[hachage(cle)]


def modifier(dictionnaire: tuple, cle: str, valeur: Any) -> None:
    """Modifie une valeur d'un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé
        valeur (Any): la valeur
    """
    cles, valeurs = dictionnaire
    if cles[hachage(cle)] == cle:
        valeurs[hachage(cle)] = valeur
    else:
        raise ValueError(f"L'élément {cle} n'existe pas")


def rechercher(dictionnaire: tuple, valeur: Any) -> str | None:
    """Recherche une clé à partir d'une valeur

    Args:
        dictionnaire (tuple): le dictionnaire
        valeur (Any): la valeur

    Returns:
        str: la clé
    """
    cles, valeurs = dictionnaire
    for i in range(N):
        if valeurs[i] == valeur:
            return cles[i]
    return None


if __name__ == "__main__":
    dico = creer_dictionnaire()
    ajouter(dico, "Habib", "01 23 45 67 89")
    ajouter(dico, "Mohamed", "02 34 56 78 90")
    ajouter(dico, "Karim", "03 45 67 89 01")
    ajouter(dico, "Mehdi", "04 56 78 90 12")
    ajouter(dico, "Fatima", "05 67 89 01 23")
    ajouter(dico, "Sara", "07 89 01 23 45")
    modifier(dico, "Habib", "09 01 23 45 67")
    supprimer(dico, "Mohamed")
    print(dico)
    print(lire(dico, "Habib"))
    rechercher(dico, "09 01 23 45 67")

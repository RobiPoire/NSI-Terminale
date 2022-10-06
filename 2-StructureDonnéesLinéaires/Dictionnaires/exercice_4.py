"""
Les dictionnaires - Exercice 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait dictionnaire implémentées en Python 
(avec la gestion des collisions avec la méthode du chainage linéaire)
"""

__auhtor__ = "RobiPoire"


N = 25


def creer_dictionnaire() -> tuple:
    """Crée un dictionnaire vide de taille N

    Returns:
        tuple: le dictionnaire
    """
    valeurs = [0] * N
    cles = [0] * N
    return (cles, valeurs)


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


def est_vide(dictionnaire: tuple) -> bool:
    """ Vérifie si un dictionnaire est vide

    Args:
        dictionnaire (tuple): le dictionnaire

    Returns:
        bool: True si vide, False sinon
    """
    cles = dictionnaire[0]
    for i in range(N):
        if cles[i] != 0:
            return False
    return True


def est_plein(dictionnaire: tuple) -> bool:
    """ Vérifie si un dictionnaire est plein

    Args:
        dictionnaire (tuple): le dictionnaire

    Returns:
        bool: True si plein, False sinon
    """
    cles = dictionnaire[0]
    for i in range(N):
        if cles[i] == 0:
            return False
    return True


def ajouter(dictionnaire: tuple, cle: str, valeur: object) -> None:
    """Ajoute une valeur à un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé
        valeur (object): la valeur
    """
    if est_plein(dictionnaire):
        raise Exception("Le dictionnaire est plein")
    cles, valeurs = dictionnaire
    if cles[hachage(cle)] == 0:
        cles[hachage(cle)] = cle
        valeurs[hachage(cle)] = valeur
    else:
        for i in range(N):
            if cles[i] == 0:
                cles[i] = cle
                valeurs[i] = valeur
                break


def supprimer(dictionnaire: tuple, cle: str) -> None:
    """Supprime une valeur d'un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé
    """
    cles, valeurs = dictionnaire
    if cles[hachage(cle)] == cle:
        cles[hachage(cle)] = 0
        valeurs[hachage(cle)] = 0
    else:
        for i in range(N):
            if cles[i] == cle:
                cles[i] = 0
                valeurs[i] = 0
                break


def lire(dictionnaire: tuple, cle: str) -> object | None:
    """ Lit une valeur d'un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé

    Returns:
        object: la valeur
    """
    cles, valeurs = dictionnaire
    if cles[hachage(cle)] == cle:
        return valeurs[hachage(cle)]
    else:
        for i in range(N):
            if cles[i] == cle:
                return valeurs[i]
        return None


def modifier(dictionnaire: tuple, cle: str, valeur: object) -> None:
    """ Modifie une valeur d'un dictionnaire

    Args:
        dictionnaire (tuple): le dictionnaire
        cle (str): la clé
        valeur (object): la valeur
    """
    cles, valeurs = dictionnaire
    if cles[hachage(cle)] == cle:
        valeurs[hachage(cle)] = valeur
    else:
        for i in range(N):
            if cles[i] == cle:
                valeurs[i] = valeur
                break


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


if __name__ == "__main__":
    dico = creer_dictionnaire()
    ajouter(dico, "Habib", "01 23 45 67 89")
    ajouter(dico, "Mohamed", "02 34 56 78 90")
    ajouter(dico, "Karim", "03 45 67 89 01")
    ajouter(dico, "Mehdi", "04 56 78 90 12")
    ajouter(dico, "Fatima", "05 67 89 01 23")
    ajouter(dico, "Sara", "07 89 01 23 45")
    ajouter(dico, "Lina ", "08 90 12 34 56")
    modifier(dico, "Habib", "09 01 23 45 67")
    supprimer(dico, "Mohamed")
    print(dico)
    print(lire(dico, "Habib"))
    rechercher(dico, "09 01 23 45 67")

"""
Les dictionnaires - Exercice 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Les fonctions du type astrait dictionnaire implémentées en Python 
(avec la gestion des collisions avec la méthode du chainage linéaire)
"""

__auhtor__ = "RobiPoire, HabibLebsir, LukasGontard"


N = 25


def creer_dictionnaire() -> tuple:
    """
    Il crée un tuple de deux listes, chacune de longueur N, et renvoie le tuple
    
    Returns:
      Un tuple de deux listes.
    """
    valeurs = [0] * N
    cles = [0] * N
    return (cles, valeurs)


def hachage(cle: str) -> int:
    """
    Il additionne les valeurs ASCII des caractères de la chaîne et renvoie le reste de la division de
    cette somme par la taille de la table
    
    Args:
      cle (str): chaîne
    
    Returns:
      Somme des valeurs ordinales des caractères de la chaîne modulo N.
    """
    somme = 0
    for i in cle:
        somme += ord(i)
    return somme % N


def est_vide(dictionnaire: tuple) -> bool:
    """
    Il renvoie True si le dictionnaire est vide, et False sinon
    
    Args:
      dictionnaire (tuple): tuple
    
    Returns:
      une valeur booléenne.
    """
    cles = dictionnaire[0]
    for i in range(N):
        if cles[i] != 0:
            return False
    return True


def est_plein(dictionnaire: tuple) -> bool:
    """
    Elle renvoie True si toutes les clés du dictionnaire sont différentes de zéro, et False sinon.
    
    Args:
      dictionnaire (tuple): tuple
    
    Returns:
      Un tuple de deux listes.
    """
    cles = dictionnaire[0]
    for i in range(N):
        if cles[i] == 0:
            return False
    return True


def ajouter(dictionnaire: tuple, cle: str, valeur: object) -> None:
    """
    Il ajoute une paire clé-valeur au dictionnaire
    
    Args:
      dictionnaire (tuple): tuple
      cle (str): chaîne
      valeur (object): la valeur que vous voulez ajouter au dictionnaire
    """
    if est_plein(dictionnaire):
        raise Exception("Le dictionnaire est plein")
    cles, valeurs = dictionnaire
    if cles[hachage(cle)] == 0:
        cles[hachage(cle)] = cle
        valeurs[hachage(cle)] = valeur
    else:
        i = 0
        while(i < N and cles[i] != 0):
            if cles[i] == cle:
                cles[i] = cle
                valeurs[i] = valeur
            else:
                i+=1

def supprimer(dictionnaire: tuple, cle: str) -> None:
    """
    Si la clé est dans le premier emplacement, supprimez-la, sinon, recherchez-la et supprimez-la
    
    Args:
      dictionnaire (tuple): tuple
      cle (str): la clé à supprimer
    """
    cles, valeurs = dictionnaire
    if cles[hachage(cle)] == cle:
        cles[hachage(cle)] = 0
        valeurs[hachage(cle)] = 0
    else:
        i = 0
        while(i < N and cles[i] != cle):
            if cles[i] == cle:
                cles[i] = 0
                valeurs[i] = 0
            else:
                i+=1


def lire(dictionnaire: tuple, cle: str) -> object | None:
    """
    Il renvoie la valeur associée à la clé 'cle' dans le dictionnaire 'dictionnaire' s'il existe, et
    'None' sinon
    
    Args:
      dictionnaire (tuple): tuple
      cle (str): la clé à chercher
    
    Returns:
      La valeur associée à la clé.
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
    """
    Il prend un tuple de deux listes, une clé et une valeur, et modifie la valeur dans la deuxième liste
    à l'index de la clé dans la première liste
    
    Args:
      dictionnaire (tuple): tuple
      cle (str): la clé à modifier
      valeur (object): la valeur que vous souhaitez modifier
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
    """
    Il renvoie la clé associée à la valeur donnée dans le dictionnaire donné, ou None si la valeur n'est
    pas dans le dictionnaire
    
    Args:
      dictionnaire (tuple): tuple
      valeur (object): la valeur pour laquelle vous voulez trouver la clé
    
    Returns:
      Clé associée à la valeur.
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

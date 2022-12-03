"""
TD Majoritaire
~~~~~~~~~~~~~~
Réponses aux questions du TD Majoritaire=
"""

__author__ = "RobiPoire"

import random
import time
import matplotlib.pyplot as plt


def recherche_majoritaire(E: list) -> any:
    """Renvoie l'élément majoritaire de la liste E, ou None si il n'y en a pas.

    Args:
        E (list): liste d'éléments

    Returns:
        any: élément majoritaire de la liste E, ou None si il n'y en a pas
    """
    if len(E) == 1:
        return E[0]
    else:
        E1 = E[:len(E)//2]
        E2 = E[len(E)//2:]
        x1 = recherche_majoritaire(E1)
        x2 = recherche_majoritaire(E2)
        if x1 == x2:
            return x1
        else:
            if E.count(x1) > len(E)//2:
                return x1
            elif E.count(x2) > len(E)//2:
                return x2
            else:
                return None


def majoritaire(i: int, j: int) -> any:
    """Renvoie l'élément majoritaire de la liste E, ou None si il n'y en a pas.

    Args:
        i (int): indice de début
        j (int): indice de fin

    Returns:
        any: élément majoritaire de la liste E, ou None si il n'y en a pas
    """
    if i == j:
        return (E[i], 1)
    else:
        milieu = int((i+j)/2)
        taille = j-i+1
        (x, cx) = majoritaire(i, milieu)
        (y, cy) = majoritaire(milieu+1, j)
        if x == y:
            return (x, cx+cy)
        if cx != 0:
            cx = cx + occ(x, milieu+1, j)
        if cy != 0:
            cy = cy + occ(y, i, milieu)
        if cx > taille//2:
            return (x, cx)
        elif cy > taille//2:
            return (y, cy)
        else:
            return (None, 0)


def occ(x: any, i: int, j: int) -> int:
    """Renvoie le nombre d'occurences de l'élément x dans la liste E[i:j].

    Args:
        x (any): élément
        i (int): indice de début
        j (int): indice de fin

    Returns:
        int: nombre d'occurences de l'élément x dans la liste E[i:j]
    """
    cpt = 0
    for k in range(i, j+1):
        if E[k] == x:
            cpt = cpt + 1
    return cpt


def efficacite_fonctions(n: int, fonction: any) -> float:
    """Renvoie le temps d'execution de la fonction en argument.

    Args:
        n (int): taille de la liste
        fonction (any): fonction

    Returns:
        float: temps d'execution de la fonction en argument
    """
    global E
    # Avoir une liste de "filles" et de "garçons" de taille n, aléatoirement mélangés
    nombre_filles = random.randint(0, n)
    nombre_garcons = n - nombre_filles
    # Melangé aléatoirement
    E = ["F"] * nombre_filles + ["G"] * nombre_garcons
    random.shuffle(E)
    # Recherche majoritaire
    temps_debut = time.time()
    if fonction == recherche_majoritaire:
        recherche_majoritaire(E)
    else:
        majoritaire(0, len(E)-1)
    temps_fin = time.time()
    temps_execution = temps_fin - temps_debut
    return round(temps_execution, 6)


def liste_temps_execution(n_max: int, fonction: any) -> list:
    """Renvoie une liste des temps d'execution de la fonction en argument.

    Args:
        n_max (int): taille maximale de la liste
        fonction (any): fonction

    Returns:
        list: liste des temps d'execution de la fonction en argument
    """
    liste_temps_execution = []
    for n in range(1, n_max+1, n_max//100):
        temps_execution = efficacite_fonctions(n, fonction)
        liste_temps_execution.append(temps_execution)
    return liste_temps_execution


def matplot_liste(liste1: list, liste2: list, x_max: int) -> None:
    """Affiche les listes en argument dans un graphique.

    Args:
        liste1 (list): liste 1
        liste2 (list): liste 2
        x_max (int): taille maximale de la liste
    """
    x = range(1, x_max+1, x_max//100)
    y1 = liste1
    y2 = liste2
    plt.plot(x, y1, label="recherche_majoritaire")
    plt.plot(x, y2, label="majoritaire")
    plt.xlabel("n")
    plt.ylabel("temps d'execution")
    plt.title(
        "Comparaison des temps d'execution des fonctions recherche_majoritaire et majoritaire")
    plt.legend()
    plt.show()


def matplot_temps_execution(n_max: int) -> None:
    """Affiche les temps d'execution des fonctions recherche_majoritaire et majoritaire dans un graphique.

    Args:
        n_max (int): taille maximale de la liste
    """
    liste1 = liste_temps_execution(n_max, recherche_majoritaire)
    liste2 = liste_temps_execution(n_max, majoritaire)
    matplot_liste(liste1, liste2, n_max)


if __name__ == "__main__":
    # Affichage des temps d'execution des fonctions recherche_majoritaire et majoritaire
    # avec des listes de taille 1 à 1000
    matplot_temps_execution(1000)

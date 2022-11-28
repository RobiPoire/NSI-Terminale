import random
import time
import matplotlib.pyplot as plt


def recherche_majoritaire(E: list) -> any:
    """renvoie un élément majoritaire de E ou None si E ne contient pas d'élément majoritaire"""
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


def majoritaire(i, j):
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


def occ(x, i, j):
    cpt = 0
    for k in range(i, j+1):
        if E[k] == x:
            cpt = cpt + 1
    return cpt


def efficacite_fonctions(n, fonction):
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


def liste_temps_execution(n_max, fonction):
    liste_temps_execution = []
    for n in range(1, n_max+1, n_max//100):
        temps_execution = efficacite_fonctions(n, fonction)
        liste_temps_execution.append(temps_execution)
    return liste_temps_execution


def matplot_liste(liste1, liste2, x_max):
    # Liste1 = liste des temps d'execution de la fonction recherche_majoritaire
    # Liste2 = liste des temps d'execution de la fonction majoritaire
    # x = l'indice des listes
    # y = les valeurs des listes
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


def matplot_temps_execution(n_max):
    liste1 = liste_temps_execution(n_max, recherche_majoritaire)
    liste2 = liste_temps_execution(n_max, majoritaire)
    matplot_liste(liste1, liste2, n_max)


matplot_temps_execution(1000)

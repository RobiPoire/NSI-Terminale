"""
Hanoi Project - Analyse de la complexité
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fichier contenant les fonctions pour l'analyse de la complexité
"""

__author__ = "RobiPoire"


# Importation des modules nécessaires
from time import time
from hanoi_console import hanoi_instructions
import matplotlib.pyplot as plt


def hanoi_resolution_time(disc_number: int) -> float:
    """Renvoie le temps d'exécution de la fonction hanoi pour un nombre de disque donné.

    Args:
        disc_number (int): Nombre de disque.

    Returns:
        float: Temps d'exécution de la fonction hanoi pour un nombre de disque donné.
    """
    # On récupère l'heure de début
    start_time = time()

    # On exécute la fonction hanoi, sans afficher les instructions
    # (ici on s'intéresse que au temps d'exécution)
    hanoi_instructions(disc_number, "A", "B", "C", False)

    # On récupère l'heure de fin
    end_time = time()

    # On calcule le temps d'exécution
    total_time = round(end_time - start_time, 4)

    # On retourne le temps d'exécution
    return total_time


def resolution_time_graph(times_list: list) -> None:
    """Affiche un graphique du temps d'exécution en fonction du nombre de disque.

    Args:
        times_list (list): Liste des temps d'exécution.
    """
    # On ajoute les temps d'exécution au graphique
    plt.plot(times_list)

    # On affiche le nom de l'axe des abscisses
    plt.xlabel("Nombre de disque")

    # On affiche le nom de l'axe des ordonnées
    plt.ylabel("Temps d'exécution (s)")

    # On affiche le graphique
    plt.show()


def hanoi_graph(disc_number: int) -> None:
    """Affiche un graphique du temps d'exécution en fonction du nombre de disque.

    Args:
        disc_number (int): Nombre de disque.
    """
    # On initialise la liste des temps d'exécution
    times_list = []

    # Pour chaque nombre de disque :
    for i in range(1, disc_number):
        # On ajoute le temps d'exécution à la liste
        times_list.append(hanoi_resolution_time(i))

    # Afficher le nombre d'étapes pour le nombre de disque donné
    print(
        f"Nombre d'étapes pour {disc_number} disque(s) : {2**disc_number - 1}")

    # On affiche le graphique du temps d'exécution
    resolution_time_graph(times_list)

# Equation de la complexité de la fonction hanoi : 2T(n-1) + 1
# T = temps d'exécution
# n = nombre de disque

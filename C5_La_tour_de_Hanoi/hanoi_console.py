"""
Hanoi Project - Fonctions Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fichier contenant les fonctions pour l'affichage de la tour de Hanoi dans la console.
"""

__author__ = "RobiPoire, HabibLebsir, devnatiofrance"


# Importations des types (pour les annotations)
from typing import Any, Union
# Importations des fonctions pour hanoi_display
from display_tools import *


def hanoi_instructions(
    discs_number: int,
    start: str,
    middle: str,
    arrival: str,
    enable_print: bool = True
) -> None:
    """Résoud le problème de la tour de Hanoi, en affichant tout les déplacements à effectuer si enable_print est True.

    Args:
        discs_number (int): Nombre de disques à déplacer.
        start (str): Nom de la tour de départ.
        middle (str): Nom de la tour intermédiaire.
        arrival (str): Nom de la tour d'arrivée.
        enable_print (bool, optional): Si True, affiche les instructions. True par défaut.
    """
    if discs_number == 1:
        if enable_print:  # Si enable_print est à True, on affiche les instructions
            # On affiche l'instruction à effectuer
            print(
                f"Déplacer le disque du pilier {start} vers le pilier {arrival}")
    else:
        hanoi_instructions(discs_number - 1, start,
                           arrival, middle, enable_print)
        hanoi_instructions(1, start, middle, arrival, enable_print)
        hanoi_instructions(discs_number - 1, middle,
                           start, arrival, enable_print)


def hanoi_resolution(
    style: int,  # Compris entre 2 et 4 (inclus)
    discs_number: int,
    pillars: Union[dict, None] = None,
    start: str = "A",
    middle: str = "B",
    arrival: str = "C",
) -> None:
    """Résoud le problème de la tour de Hanoi, en affichant les déplacements à effectuer
    avec la fonction affichage_hanoi, et le style choisi par l'utilisateur.

    Args:
        discs_number (int): Nombre de disques à déplacer.
        pillars (Union[dict, None], optional): Dictionnaire contenant les piliers. None par défaut.
        start (str, optional): Nom de la tour de départ. "A" par défaut.
        middle (str, optional): Nom de la tour intermédiaire. "B" par défaut.
        arrival (str, optional): Nom de la tour d'arrivée. "C" par défaut.
    """
    # On précise qu'on utilise la variable globale ITERATION_NUMBER (pour pouvoir la modifier)
    global ITERATION_NUMBER

    if (pillars is None):  # Si la liste des piliers est vide, on l'initialise avec les disques de départ
        pillars = {"A": [i for i in range(discs_number, 0, -1)]}
        pillars["B"] = []
        pillars["C"] = []
        # On met le nombre d'itérations à 0
        ITERATION_NUMBER = 0
        # On affiche l'état des piliers
        print(hanoi_display(style, pillars["A"], pillars["B"], pillars["C"]))

    if discs_number == 1:
        pillars[arrival].append(pillars[start].pop())  # On déplace le disque
        # On affiche l'état des piliers
        print(hanoi_display(style, pillars["A"], pillars["B"], pillars["C"]))

    # On déplace les n-1 disques de la tour de départ vers la tour intermédiaire (avec la récursivité)
    else:
        hanoi_resolution(style, discs_number - 1,
                         pillars, start, arrival, middle)
        hanoi_resolution(style, 1, pillars, start, middle, arrival)
        hanoi_resolution(style, discs_number - 1,
                         pillars, middle, start, arrival)


def hanoi_display(
    style: int,  # Compris entre 2 et 4 (inclus)
    start_pillar: list,
    middle_pillar: list,
    arrival_pillar: list,
) -> Any:
    """Affiche l'état des piliers, selon le style choisi.

    Args:
        style (int): Style d'affichage choisi.
        start_pillar (list): Liste des disques de la tour de départ.
        middle_pillar (list): Liste des disques sur la tour intermédiaire.
        arrival_pillar (list): Liste des disques sur la tour d'arrivée.

    Raises:
        ValueError: Si le style choisi n'est pas compris entre 2 et 4 (inclus).

    Returns:
        Any: Retourne l'affichage selon le style choisi.
    """
    global ITERATION_NUMBER

    if (style == 2):  # La  représentation sous la forme d'une liste de chaque pilier de la tour
        return f"{start_pillar}\n{middle_pillar}\n{arrival_pillar}\n______________________"

    elif style == 3 or style == 4:  # La représentation sous forme de disques avec le caractère █
        # Combiner les listes des piliers en une seule liste, si un etage est vide, mettre un 0
        # Exemple : [3,2,1], [6,4], [5] -> [[3,2,1], [6,4,0], [5,0,0]]
        pillars = combine_pillars(start_pillar, middle_pillar, arrival_pillar)

        # Changer la taille des disques pour qu'ils soient tous impairs (pour que le centre soit toujours au milieu)
        # Changer le chiffre par le caractère ▮, selon la taille du disque
        pillars = square_discs(pillars)

        # La représentation "graphique" en console, à l'horizontale (avec le caractère ▮) :
        if style == 3:
            display = horizontal_pillars_display(pillars, ITERATION_NUMBER)
        elif style == 4:
            display = vertical_pillars_display(pillars, ITERATION_NUMBER)

    else:  # Si le style choisi n'est pas compris entre 2 et 4 (inclus)
        raise ValueError("Le style est incorrect")  # On lève une erreur

    # On incrémente le nombre d'itérations
    ITERATION_NUMBER += 1
    return display

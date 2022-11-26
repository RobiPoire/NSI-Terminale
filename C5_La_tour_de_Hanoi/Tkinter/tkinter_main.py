"""
Hanoi Project - Tkinter main file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fichier principal pour l'interface graphique de la tour de Hanoi.
"""

__author__ = "RobiPoire, HabibLebsir, devnatiofrance"

# Importation des modules
from tkinter import *
from .frame import Frame, Discs
from .discs import Disc


def hanoi_instructions(discs_number: int, start: str, middle: str, arrival: str) -> None:
    """Résoud le problème de la tour de Hanoi, en affichant tout les déplacements à effectuer.

    Args:
        discs_number (int): Nombre de disques à déplacer.
        start (str): Nom de la tour de départ.
        middle (str): Nom de la tour intermédiaire.
        arrival (str): Nom de la tour d'arrivée.
    """
    global liste_itterations

    if discs_number == 1:
        # Mettre le déplacement dans la liste des itterations
        liste_itterations.append((start, arrival))
    else:
        hanoi_instructions(discs_number - 1, start,
                           arrival, middle)
        hanoi_instructions(1, start, middle, arrival)
        hanoi_instructions(discs_number - 1, middle,
                           start, arrival)


def calcul_hanoi(move: str):
    """
    Résoud la tour de hanoï à l'aide des instructions données par la fonction hanoi_instructions.

    Args:
        move (str): Déplacement à effectuer.
    """

    # Utilisation des variables globales
    global liste_itterations
    global index_itterations
    global start
    global middle
    global arrival

    # Si le déplacement est en avant
    if move == "forward" and index_itterations < len(liste_itterations):
        # Implémenter le déplacement dans la variable action et augmener l'index
        action = liste_itterations[index_itterations]
        index_itterations += 1

        # Déplacer le disque dans la liste correspondante
        if action[0] == "A" and action[1] == "B":
            # Déplacer le disque de la tour start vers la tour middle
            middle.insert(0, start.pop(0))
        elif action[0] == "A" and action[1] == "C":
            # Déplacer le disque de la tour start vers la tour arrival
            arrival.insert(0, start.pop(0))
        elif action[0] == "B" and action[1] == "A":
            # Déplacer le disque de la tour middle vers la tour start
            start.insert(0, middle.pop(0))
        elif action[0] == "B" and action[1] == "C":
            # Déplacer le disque de la tour middle vers la tour arrival
            arrival.insert(0, middle.pop(0))
        elif action[0] == "C" and action[1] == "A":
            # Déplacer le disque de la tour arrival vers la tour start
            start.insert(0, arrival.pop(0))
        elif action[0] == "C" and action[1] == "B":
            # Déplacer le disque de la tour arrival vers la tour middle
            middle.insert(0, arrival.pop(0))

    # Si le déplacement est en arrière
    elif move == "backward" and index_itterations > 0:
        # Implémenter le déplacement dans la variable action et diminuer l'index
        index_itterations -= 1
        action = liste_itterations[index_itterations]

        if action[0] == "A" and action[1] == "B":
            # Déplacer le disque de la tour middle vers la tour start
            start.insert(0, middle.pop(0))
        elif action[0] == "A" and action[1] == "C":
            # Déplacer le disque de la tour arrival vers la tour start
            start.insert(0, arrival.pop(0))
        elif action[0] == "B" and action[1] == "A":
            # Déplacer le disque de la tour start vers la tour middle
            middle.insert(0, start.pop(0))
        elif action[0] == "B" and action[1] == "C":
            # Déplacer le disque de la tour arrival vers la tour middle
            middle.insert(0, arrival.pop(0))
        elif action[0] == "C" and action[1] == "A":
            # Déplacer le disque de la tour start vers la tour arrival
            arrival.insert(0, start.pop(0))
        elif action[0] == "C" and action[1] == "B":
            # Déplacer le disque de la tour middle vers la tour arrival
            arrival.insert(0, middle.pop(0))


def main(discs_numbers: int) -> None:
    global liste_itterations
    global index_itterations
    global canva
    global start
    global middle
    global arrival
    # Création de la fenêtre
    window = Frame((1280, 720), "Tour Hanoï", "black")
    window.create()

    # Création du canva
    canva = window.createCanvas((1280, 720), "white")

    for i in range(discs_numbers - 1, -1, -1):
        Discs.append(Disc(discs_numbers, i + 1, 0, i,
                          i + 1, Discs, window.canvas))

    # Création des listes pour les tours
    start = []
    middle = []
    arrival = []

    for i in range(discs_numbers):
        start.append(i + 1)

    # Création de la liste des itterations
    liste_itterations = []
    index_itterations = 0

    # Appel de la fonction hanoi_instructions
    hanoi_instructions(discs_numbers, "A", "B", "C")

    print("Pour déplacer un disque, appuyer sur les flèches gauche (pour revenir en arrière) ou droite (pour avancer)")

    # Boucle principale
    try:
        while (window.isRunning):
            # Rafraichissement de la fenêtre
            window.frame.update()
            window.changeSize()

            # Déplacer le disque en "avant"
            if not window.forward:
                calcul_hanoi("forward")
                window.forward = True

            # Déplacer le disque en "arrière"
            if not window.backward:
                calcul_hanoi("backward")
                window.backward = True

            # Afficher les disques
            if not window.pause:
                for disc in Discs:
                    if disc.name in start:
                        disc.move(start, "A")
                    elif disc.name in middle:
                        disc.move(middle, "B")
                    elif disc.name in arrival:
                        disc.move(arrival, "C")
                    disc.drawDisc()
                window.pause = True

            # Vérification si la touche "Right" ou "Left" est enfoncée
            window.frame.bind('<Right>', window.clavier_right)
            window.frame.bind('<Left>', window.clavier_left)

        window.frame.mainloop()
    except:
        return None

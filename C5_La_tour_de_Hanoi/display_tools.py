"""
Hanoi project - Outils d'affichage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fichier contenant les fonctions utilisé pour la fonction hanoi_display
"""

__author__ = "RobiPoire, HabibLebsir, devnatiofrance"


def maximum(integer_list: list) -> int:
    """Renvoie le nombre le plus grand d'une liste.

    Args:
        integer_list (list): Liste d'entiers.

    Returns:
        int: Nombre le plus grand de la liste.
    """
    # Initialisation du nombre le plus grand
    max = integer_list[0]

    for number in integer_list:  # Pour chaque nombre dans integer_list
        # Si le nombre est supérieur ou égal au nombre le plus grand
        if number >= max:
            # On le remplace
            max = number

    # On retourne le nombre le plus grand
    return max


def combine_pillars(start_pillar: list, middle_pillar: list, arrival_pillar: list) -> list:
    """Combine les piliers dans une liste, et rajoute des
        zéros pour que les piliers aient la même longueur.

    Args:
        start_pillar (list): Liste des disques de la tour de départ.
        middle_pillar (list): Liste des disques de la tour intermédiaire.
        arrival_pillar (list): Liste des disques de la tour d'arrivée.

    Returns:
        list: Liste des piliers.
    """
    # On fait une liste des piliers pour pouvoir les traiter plus facilement
    pillars = list([list(start_pillar), list(
        middle_pillar), list(arrival_pillar)])

    # On récupère la largeur maximale des piliers
    max_length = maximum([len(i) for i in pillars])

    # On ajoute des 0 dans les emplacements vides des piliers pour que tous les piliers aient la même longueur
    for pillar in range(3):  # Pour chaque piliers
        # Tant que la longueur du piliers est inférieur à la longueur maximale
        while len(pillars[pillar]) < max_length:
            # On ajoute un 0
            pillars[pillar].append(0)

    return pillars  # On retourne la liste des piliers, avec les 0 ajoutés


def square_discs(pillars: list) -> list:
    """Transforme la taille des disques avec le caractère █ pour l'affichage.

    Args:
        pillars (list): Liste des piliers.

    Returns:
        list: Liste des piliers avec les disques transformés.
    """
    for pillar in range(3):  # Pour chaque piliers
        for disc in range(len(pillars[pillar])):  # Pour chaque disque
            # On remplace par des carrés selon la taille du disque
            pillars[pillar][disc] = "▮" * (pillars[pillar][disc] * 2 - 1)

    # On retourne la liste des piliers, avec les disques remplacés par des carrés
    return pillars


def disc_centering(pillars: list) -> list:
    """Centre les disques dans les piliers.

    Args:
        pillars (list): Liste des piliers.

    Returns:
        list: Liste des piliers avec les disques centrés.
    """
    # On récupère la largeur maximale des piliers en utilisant la largeur des disques
    # les plus en dessous car c'est forcément là où il y aura le disque le plus grand
    max_width = maximum([len(i[0]) for i in pillars])

    for pillar in range(3):  # Pour chaque piliers
        for disc in range(len(pillars[pillar])):
            # On centre le disque (avec la fonction center de la classe str)
            pillars[pillar][disc] = centering(pillars[pillar][disc], max_width)

    # On retourne la liste des piliers, avec les disques centrés
    return pillars


def centering(disc: str, width: int) -> str:
    """Centre un disque dans un piliers.

    Args:
        disc (str): Disque à centrer.
        width (int): Largeur du piliers.

    Returns:
        str: Disque centré.
    """
    # Si le disc est vide, on retourne la largeur du piliers avec des espaces
    if disc == "":
        return " " * width

    # On récupère la longueur du disque
    disc_length = len(disc)

    # On récupère la différence entre la largeur du piliers et la longueur du disque
    difference = width - disc_length

    # On ajoute des espaces au début et à la fin du disque pour le centrer et on retourne le disque
    disc = " " * (difference // 2) + disc + " " * (difference // 2)
    return disc


def horizontal_pillars_display(pillars: list, iteration_number: int) -> str:
    """Affiche les piliers horizontalement

    Args:
        pillars (list): Liste des piliers.
        iteration_number (int): Nombre d'itération.

    Returns:
        str: L'affichage des piliers.
    """
    display = ""  # Initialisation de l'affichage

    for pillar in pillars:  # Pour chaque piliers
        for disc in pillar:  # Pour chaque disque
            # On ajoute le disque et un espace
            display += f"{disc} "
            # On ajoute un retour à la ligne
        display += "\n"

    # Suppression du dernier saut de ligne
    display = display[:-1]

    # On récupère le nombre d'itération pour l'affichage
    interations_display = f"Itération N°{iteration_number}"

    # On ajoute des tirets pour séparer les étapes selon la largeur maximale des piliers
    dashes = "_" * (maximum([len(i) for i in pillars]) * 3 + 3)

    # On retourne l'affichage final
    return f"{interations_display}\n{display}\n{dashes}"

def vertical_pillars_display(pillars: list, iteration_number: int) -> str:
    """Affiche les piliers verticalement

    Args:
        pillars (list): Liste des piliers.
        iteration_number (int): Nombre d'itération.

    Returns:
        str: L'affichage des piliers.
    """
    display = ""  # Initialisation de l'affichage

    # On récupère la longueur maximale des piliers
    max_length = maximum([len(i) for i in pillars])

    pillars = disc_centering(pillars)  # On centre les disques

    for i in range(max_length, 0, -1):  # Pour chaque ligne (de la plus haute à la plus basse)
        # On ajoute les disques de chaque piliers, séparés par des espaces
        display += f"\n{pillars[0][i-1]} {pillars[1][i-1]} {pillars[2][i-1]}"

    # On récupère le nombre d'itération pour l'affichage
    interations_display = f"Itération N°{iteration_number}"

    # On récupère la largeur maximale des piliers en utilisant la largeur des disques
    # les plus en dessous car c'est forcément là où il y aura le disque le plus grand
    max_width = maximum([len(i[0]) for i in pillars])

    # On ajoute des tirets selon la largeur maximale des piliers (pour séparer les étapes)
    dashes = "_" * (max_width * 3 + 3)

    # On retourne l'affichage final
    return f"{interations_display}{display}\n{dashes}"
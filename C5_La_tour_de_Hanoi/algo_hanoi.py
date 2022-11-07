"""
Algorithme de la tour de Hanoi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Voici la fonction récursive qui permet de résoudre le problème de la tour de Hanoi.
"""

__author__ = "RobiPoire"


def hanoi(discs_number: int, start: str, middle: str, arrival: str) -> None:
    """Résoud le problème de la tour de Hanoi, en affichant les déplacements à effectuer.

    Args:
        discs_number (int): Nombre de disques à déplacer.
        start (str): Nom de la tour de départ.
        middle (str): Nom de la tour intermédiaire.
        arrival (str): Nom de la tour d'arrivée.
    """
    if discs_number == 1:
        print(f"Déplacer le disque de la pile {start} vers la pile {arrival}")
    else:
        hanoi(discs_number - 1, start, arrival, middle)
        hanoi(1, start, middle, arrival)
        hanoi(discs_number - 1, middle, start, arrival)


hanoi(4, "A", "B", "C")

# Il commence à galérer à partir de 25 disques environ

# Je pense qu'à partir de 29-32 c'est finito

"""
Hanoi Project - Fichier principal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fichier principal du projet de la tour de Hanoi.
Fichier a exécuter pour lancer le programme.
"""

__author__ = "RobiPoire, HabibLebsir, devnatiofrance"


# Importation des fonctions de hanoi.py & de complexity.py
from hanoi_console import *
from complexity import hanoi_graph


def question(question: str, min: int, max: int, error_message: str) -> str:
    """Fonction qui permet de poser une question à l'utilisateur, et de vérifier

    Args:
        question (str): Question à poser à l'utilisateur.
        min (int): Valeur minimale de la réponse.
        max (int): Valeur maximale de la réponse.
        error_message (str): Message d'erreur à afficher si la réponse n'est pas valide.

    Returns:
        str: Réponse de l'utilisateur.
    """
    while True:  # Boucle infinie (tant que la réponse n'est pas valide)
        try:  # On essaie de convertir la réponse en int
            result = int(input(question))
            if result < min or result > max:  # Si la réponse n'est pas comprise entre min et max
                raise ValueError  # On lève une erreur
            return result  # Si la réponse est valide, on la retourne

        # Si la réponse n'est pas valide (pas un int, ou pas comprise entre min et max)
        except ValueError:
            # On affiche le message d'erreur et on recommence
            print(error_message)


# Programme principal, s'exécute uniquement si le fichier est exécuté
if __name__ == "__main__":
    # Boucle infinie (tant que l'utilisateur ne veut pas quitter)
    while True:
        # Affichage du menu principal
        print("Bienvenue dans le programme de la tour de Hanoi !")
        print("Que voulez-vous faire ?")
        print("1. Résoudre le problème de la tour de Hanoi")
        print("2. Voir le graphique de la complexité de l'algorithme")
        print("3. Quitter le programme")
        # On demande à l'utilisateur ce qu'il veut faire
        choice = question("Votre choix : ", 1, 3,
                          "Veuillez entrer un nombre entre 1 et 3.")

        if choice == 1:  # Si l'utilisateur veut résoudre le problème de la tour de Hanoi
            # Choix du nombre de disques par l'utilisateur
            discs_number = question("Combien de disques voulez-vous déplacer ? ",
                                    1, 64, "Veuillez entrer un nombre compris entre 1 et 64.")

            # Affichage des différentes styles d'affichage
            print("Dans quel style voulez-vous afficher le résultat ?")
            print("1 - En une liste avec toutes les étapes")
            print(
                "2 - Avec une représentation sous la forme d'une liste de chaque pilier de la tour")
            print('3 - Avec une représentation "graphique" en console, à l\'horizontale')
            print('4 - Avec une représentation "graphique" en console, à la verticale')

            # Choix du style d'affichage du résultat par l'utilisateur
            style = question("Votre choix : ", 1, 4,
                             "Veuillez entrer un nombre compris entre 1 et 4.")

            # On appelle la bonne fonction hanoi avec les paramètres choisis par l'utilisateur
            if style == 1:
                hanoi_instructions(discs_number, "A", "B", "C")
            else:
                hanoi_resolution(style, discs_number)

        elif choice == 2:
            # Si l'utilisateur veut voir le graphique de la complexité de l'algorithme
            # On demande à l'utilisateur le nombre de disques maximum
            max_discs = question("Combien de disques voulez-vous déplacer au maximum ? ",
                                 1, 64, "Veuillez entrer un nombre compris entre 1 et 64.")

            # On affiche le graphique
            hanoi_graph(max_discs)

        elif choice == 3:
            # Si l'utilisateur veut quitter le programme
            print("Au revoir !")
            exit(0)  # On quitte le programme, ce qui arrête la boucle infinie

        # On demande à l'utilisateur s'il veut recommencer
        input("FIN de la tâche, veuillez appuyer sur entrée pour recommencer")

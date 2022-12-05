"""
Les files - Exercice 5
~~~~~~~~~~~~~~~~~~~~~~~
Convertit une expression infixée en une expression postfixée
Puis calcule le résultat de l'expression postfixée
"""

__author__ = "RobiPoire"

from sys import path

path.append("..")

from Piles.ex5 import calcul
from Piles.ex4 import sommet
import Piles.ex2 as Pile
import Files.ex3 as File

# # Taille maximale des piles et files
File.N = 50
Pile.N = 50


def conversion(expression: str) -> str:
    """Convertit une expression infixée en une expression postfixée

    Args:
        expression (str): L'expression infixée

    Returns:
        str: L'expression postfixée
    """
    file_expression = (
        File.creer_file_vide()
    )  # On crée une file vide pour stocker l'expression postfixée
    # On crée une pile vide pour stocker les opérateurs
    pile_operateurs = Pile.creer_pile_vide()
    # On prend chaque caractère de l'expression
    for caractere in expression:
        # Si c'est un début de parenthèse, on l'empile
        if caractere == "(":
            Pile.empiler(pile_operateurs, caractere)  # On empile le caractère
        elif caractere == ")":
            while sommet(pile_operateurs) != "(":
                # On ajoute un espace pour séparer les éléments
                File.enfiler(file_expression, " ")
                # On dépile l'opérateur et on l'enfile
                File.enfiler(file_expression, Pile.depiler(pile_operateurs))
            Pile.depiler(pile_operateurs)  # On dépile la parenthèse
        elif caractere in "+-*/":  # Si c'est un opérateur
            Pile.empiler(pile_operateurs, caractere)  # On l'empile
        else:  # Si c'est un nombre ou un espace
            File.enfiler(file_expression, caractere)  # On l'enfile
    # Tant qu'il reste des opérateurs dans la pile
    while not Pile.est_vide(pile_operateurs):
        # On ajoute un espace pour séparer les éléments
        File.enfiler(file_expression, " ")
        # On dépile l'opérateur et on l'enfile
        File.enfiler(file_expression, Pile.depiler(pile_operateurs))
    # On crée une chaîne de caractères vide pour stocker l'expression postfixée
    expression_postfixee = ""
    # Tant qu'il reste des éléments dans la file
    while not File.est_vide(file_expression):
        # On défile l'élément et on l'ajoute à l'expression postfixée
        expression_postfixee += File.defiler(file_expression)
    # Si il y a des espaces doubles on les remplace par des espaces simples
    if "  " in expression_postfixee:
        expression_postfixee = expression_postfixee.replace("  ", " ")
    return expression_postfixee  # On retourne l'expression postfixée


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # L'expression infixée à convertir
    expression = "7 * ((13 + 22 - 15) / 5)"

    # Conversion de l'expression infixée en une expression postfixée
    expression_postfixee = conversion(expression)
    print(expression_postfixee)

    # Calcul de l'expression postfixée
    print(calcul(expression_postfixee))

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


def conversion(expression: str) -> str:
    """Convertit une expression infixée en une expression postfixée

    Args:
        expression (str): L'expression infixée

    Returns:
        str: L'expression postfixée
    """
    file_expression = []
    pile_operateurs = []
    for caractere in expression:
        if caractere == "(":
            pile_operateurs.append(caractere)
        elif caractere == ")":
            while pile_operateurs[-1] != "(":
                file_expression.append(" ")
                file_expression.append(pile_operateurs.pop())
            pile_operateurs.pop()
        elif caractere in "+-*/":
            pile_operateurs.append(caractere)
        else:
            file_expression.append(caractere)
    while pile_operateurs:
        file_expression.append(" ")
        file_expression.append(pile_operateurs.pop())
    file_expression = "".join(file_expression)
    if "  " in file_expression:
        file_expression = file_expression.replace("  ", " ")
    return file_expression


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # L'expression infixée à convertir
    expression = "7 * (((13 + 22) - 15) / 5)"

    # Conversion de l'expression infixée en une expression postfixée
    expression_postfixee = conversion(expression)
    print(expression_postfixee)

    # Calcul de l'expression postfixée
    print(calcul(expression_postfixee))

"""
Les piles - Exercice 5
~~~~~~~~~~~~~~~~~~~~~~~
Calcule une expression arithmétique exprimée en NPI (notation polonaise inversée).
"""

__author__ = "RobiPoire"

try :
    from ex2 import *
except ImportError: # Pour l'exercice 5 sur la partie sur les files
    from .ex2 import *


def calcul(expression: str) -> float:
    """Calcule une expression arithmétique exprimée en NPI (notation polonaise inversée)

    Args:
        expression (str): L'expression à calculer

    Returns:
        float: Le résultat du calcul
    """
    pile = creer_pile_vide()
    for element in expression.split():
        if element == "+":
            empiler(pile, depiler(pile) + depiler(pile))
        elif element == "-":
            empiler(pile, - depiler(pile) + depiler(pile))
        elif element == "*":
            empiler(pile, depiler(pile) * depiler(pile))
        elif element == "/":
            empiler(pile, 1 / depiler(pile) * depiler(pile))
        else:
            empiler(pile, float(element))
    return depiler(pile)


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # Test 1 : 5+3 = 8
    print(calcul("5 3 +"))

    # Test 2 : 3*((4+5)-6) = 9
    print(calcul("3 4 5 + 6 - *"))

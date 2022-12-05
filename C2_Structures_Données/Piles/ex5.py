"""
Les piles - Exercice 5
~~~~~~~~~~~~~~~~~~~~~~~
Calcule une expression arithmétique exprimée en NPI (notation polonaise inversée).
"""

__author__ = "RobiPoire"

# On importe les fonctions sur les piles
try:
    import ex2 as Pile
except ImportError:  # Pour pouvoir importer les fonctions pour l'exercice 5 sur les files
    import Piles.ex2 as Pile

# Taille maximale des piles
Pile.N = 6


def calcul(expression: str) -> float:
    """Calcule une expression arithmétique exprimée en NPI (notation polonaise inversée)

    Args:
        expression (str): L'expression à calculer

    Returns:
        float: Le résultat du calcul
    """
    pile = Pile.creer_pile_vide()  # On crée une pile vide
    for element in expression.split():  # On parcourt chaque élément de l'expression
        if element == "+":
            Pile.empiler(pile, Pile.depiler(pile) + Pile.depiler(pile))  # x + y
        elif element == "-":
            Pile.empiler(
                pile, -Pile.depiler(pile) + Pile.depiler(pile)
            )  # x - y = - y + x
        elif element == "*":
            Pile.empiler(pile, Pile.depiler(pile) * Pile.depiler(pile))  # x * y
        elif element == "/":
            Pile.empiler(
                pile, 1 / Pile.depiler(pile) * Pile.depiler(pile)
            )  # x / y = 1 / y * x
        else:  # Si l'élément n'est pas un opérateur, on l'empile
            Pile.empiler(pile, float(element))  # On empile l'élément
    # On retourne le résultat du calcul arrondi à 4 décimales
    return round(Pile.depiler(pile), 4)


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # Test 1 : 5+3 = 8
    print(calcul("5 3 +"))

    # Test 2 : 3*((4+5)-6) = 9
    print(calcul("3 4 5 + 6 - *"))

    # Test 3 : 3*(4/5)-6 = -3.6
    print(calcul("3 4 5 / * 6 -"))

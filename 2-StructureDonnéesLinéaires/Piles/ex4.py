"""
Les piles - Exercice 4
~~~~~~~~~~~~~~~~~~~~~~~
Vérifier si une expression est correctement parenthésée
"""

__author__ = "RobiPoire"

# On importe les fonctions de l'exercice 2
from ex2 import *


def sommet(pile: list) -> object:
    """Retourne le sommet de la pile sans le dépiler

    Args:
        pile (list): La pile

    Raises:
        IndexError: Si la pile est vide

    Returns:
        object: Le sommet de la pile
    """
    if est_vide(pile):
        raise IndexError("Pile vide")
    sommet = depiler(pile)
    empiler(pile, sommet)
    return sommet


def est_bien_parenthesee(expression: str) -> bool:
    """Vérifie si une expression est correctement parenthésée

    Args:
        expression (str): L'expression à vérifier

    Returns:
        bool: True si l'expression est correctement parenthésée, False sinon
    """
    pile = creer_pile_vide()
    for caractere in expression:
        if caractere == "(" or caractere == "[":
            empiler(pile, caractere)
        elif caractere == ")" or caractere == "]":
            # Si la pile est vide, on a plus de parenthèses ouvrantes que fermantes :
            if est_vide(pile):
                return False
            # Si la parenthèse fermante ne correspond pas à la parenthèse ouvrante :
            else:
                if caractere == ")" and sommet(pile) == "(":
                    depiler(pile)
                elif caractere == "]" and sommet(pile) == "[":
                    depiler(pile)
                else:
                    return False
    # Si la pile est vide, on a forcement autant de parenthèses ouvrantes que fermantes
    # sinon, on a plus de parenthèses ouvrantes que fermantes
    return est_vide(pile)


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # Test 1 : False
    print(est_bien_parenthesee("[3 + (5 - 7] * 3)"))

    # Test 2 : True
    print(est_bien_parenthesee("[3 + 5] - (7 * 3)"))

"""
Les piles - Exercice 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Une expression (algébrique ou arithmétique) est correctement parenthésée si d'une part, le 
nombre de parenthèses et crochets, ouvrants et fermants, est le même et si d'autre part les 
correspondances ne se croisent pas. 

Par exemple, l'expression "[3 + (5 - 7] * 3)" n'est pas correctement parenthésée car la 
parenthèse fermante ne peut pas venir après le crochet fermant. 

1. Ecrire un algorithme qui s'aide d'une pile pour contrôler le bon parenthésage d'une 
expression. 

2. Ecrire en Python une fonction Est_bien_Parenthesee(E) qui renvoie True si l'expression E 
est correctement parenthésée, et False dans le cas contraire.
"""

__author__ = "RobiPoire"


def Est_bien_Parenthesee(E: str) -> bool:
    """Vérifie si une expression est correctement parenthésée

    Args:
        E (str): L'expression à vérifier

    Returns:
        bool: True si l'expression est correctement parenthésée, False sinon
    """
    P = []
    for i in E:
        if i == "(" or i == "[":
            P.append(i)
        elif i == ")" or i == "]":
            # Si la pile est vide, on a plus de parenthèses ouvrantes que fermantes
            if len(P) == 0:
                return False
            # Si la parenthèse fermante ne correspond pas à la parenthèse ouvrante
            else:
                if i == ")" and P[-1] == "(":
                    P.pop()
                elif i == "]" and P[-1] == "[":
                    P.pop()
                else:
                    return False
    # Si la pile est vide, on a forcement autant de parenthèses ouvrantes que fermantes
    if len(P) == 0:
        return True
    # Sinon, on a plus de parenthèses ouvrantes que fermantes
    else:
        return False


#! Exemple d'utilisation
# Se lance uniquement si le fichier est exécuté
if __name__ == "__main__":

    # Test 1 : False
    print(Est_bien_Parenthesee("[3 + (5 - 7] * 3)"))

    # Test 2 : True
    print(Est_bien_Parenthesee("[3 + 5] - (7 * 3)"))

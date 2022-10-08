"""
Les piles - Exercice 4
~~~~~~~~~~~~~~~~~~~~~~~
Vérifier si une expression est correctement parenthésée
"""

__author__ = "RobiPoire"

# On importe les fonctions sur les piles
try:
    import ex2 as Pile
except ImportError:  # Pour pouvoir importer les fonctions pour l'exercice 5 sur les files
    import Piles.ex2 as Pile

# Taille maximale des piles
Pile.N = 6


def sommet(pile: list) -> object:
    """Retourne le sommet de la pile sans la dépiler

    Args:
        pile (list): La pile

    Raises:
        IndexError: Si la pile est vide

    Returns:
        object: Le sommet de la pile
    """
    if Pile.est_vide(pile):  # Si la pile est vide, on ne peut pas retourner le sommet
        raise IndexError("La pile est vide, impossible de dépiler un élément")
    # On récupère le sommet de la pile en le dépillant
    sommet = Pile.depiler(pile)
    Pile.empiler(pile, sommet)  # On réempile le sommet de la pile
    return sommet  # On retourne le sommet de la pile


def est_bien_parenthesee(expression: str) -> bool:
    """Vérifie si une expression est correctement parenthésée

    Args:
        expression (str): L'expression à vérifier

    Returns:
        bool: True si l'expression est correctement parenthésée, False sinon
    """
    pile = Pile.creer_pile_vide()
    for caractere in expression:
        if caractere == "(" or caractere == "[":
            Pile.empiler(pile, caractere)
        elif caractere == ")" or caractere == "]":
            # Si la pile est vide, on a plus de parenthèses fermantes que ouvrantes :
            if Pile.est_vide(pile):
                return False
            # Si la parenthèse fermante ne correspond pas à la parenthèse ouvrante :
            else:
                # Si la parenthèse ronde fermante correspond à la dernière parenthèse ronde ouvrante :
                if caractere == ")" and sommet(pile) == "(":
                    Pile.depiler(pile)
                # Si la parenthèse carré fermante correspond à la dernière parenthèse carré ouvrante :
                elif caractere == "]" and sommet(pile) == "[":
                    Pile.depiler(pile)
                # Sinon c'est que la parenthèse fermante ne correspond pas à la parenthèse ouvrante :
                else:
                    return False
    # Si la pile est vide, on a forcement autant de parenthèses ouvrantes que fermantes
    # Sinon on a plus de parenthèses ouvrantes que fermantes
    return Pile.est_vide(pile)


# Exemple d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté

    # Test 1 : False
    print(est_bien_parenthesee("[3 + (5 - 7] * 3)"))

    # Test 2 : True
    print(est_bien_parenthesee("[3 + 5] - (7 * 3)"))

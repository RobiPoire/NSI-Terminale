"""
Les piles - Exercice Bonus 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Vérifier si le code HTML est correctement balisé
"""

__author__ = "RobiPoire"

import ex2 as Piles

def verif_balise(html: str) -> bool:
    """Vérifie si les balises sont bien sous la forme <balise>

    Args:
        html (str): Le code html

    Returns:
        bool: True si le code html est correctement balisé, False sinon
    """
    P = Piles.CREER_PILE_VIDE()
    for i in range(len(html)):
        if html[i] == "<":
            Piles.EMPILER(P, html[i])
        elif html[i] == ">":
            if Piles.EST_VIDE(P):
                return False
            Piles.DEPILER(P)
    return Piles.EST_VIDE(P)

def texte_correctement_balisé(texte: str) -> bool:
    if verif_balise(texte) == False:
        raise ValueError("Le texte a des balises mal formées")
    P = Piles.CREER_PILE_VIDE()


print(verif_balise("<p><htmltexte</p></html>"))
print(texte_correctement_balisé("<html><p>texte</p></html>"))

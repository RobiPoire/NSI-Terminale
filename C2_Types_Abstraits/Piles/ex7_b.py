"""
Les piles - Exercice 7 Partie B
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Vérifier si le code HTML est correctement balisé
"""

__author__ = "RobiPoire"

# importation des foncitons sur les piles
import ex2 as Pile

# Taille maximale de la pile
Pile.N = 20


def ignore_balises_non_voulues(html: str) -> str:
    """Ignore les balises non voulues

    Args:
        html (str): Le code HTML

    Returns:
        str: Le code HTML sans les balises non voulues
    """
    non_voulues = ["<br>", "<hr>", "<img>", "<!DOCTYPE html>", "<!--", "-->"]
    # On supprime les balises non voulues
    for balise in non_voulues:
        html = html.replace(balise, "")
    return html  # on retourne le code HTML sans les balises non voulues


def verif_balise_html(html: str) -> bool:
    """Vérifie si le code HTML est correctement balisé

    Args:
        html (str): Le code HTML

    Returns:
        bool: True si le code HTML est correctement balisé, False sinon
    """
    html = ignore_balises_non_voulues(html)  # On ignore les balises non voulues
    pile = Pile.creer_pile_vide()  # On crée une pile vide
    for i in range(len(html)):  # On parcourt le code HTML
        if html[i] == "<" and html[i + 1] != "/":  # Si on trouve une balise ouvrante
            nom_balise_ouvrante = ""
            i += 1
            while html[i] != ">":  # On récupère le nom de la balise ouvrante
                nom_balise_ouvrante += html[i]
                i += 1
            # On empile le nom de la balise ouvrante
            Pile.empiler(pile, nom_balise_ouvrante)
        elif html[i] == "<" and html[i + 1] == "/":  # Si on trouve une balise fermante
            # Si la pile est vide, on a plus de balises fermantes que ouvrantes
            if Pile.est_vide(pile):
                return False
            nom_balise_fermante = ""
            i += 2
            while html[i] != ">":  # On récupère le nom de la balise fermante
                nom_balise_fermante += html[i]
                i += 1
            sommet = Pile.depiler(pile)  # On dépile le sommet de la pile
            if (
                sommet != nom_balise_fermante
            ):  # On vérifie si le nom de la balise fermante correspond au nom de la balise ouvrante
                return False  # Si ce n'est pas le cas, le code HTML n'est pas correctement balisé
    # Si la pile est vide, le code HTML est correctement balisé sinon cela signifie qu'il y a plus de balises ouvrantes que fermantes
    return Pile.est_vide(pile)


# Exemple d'utilisation :
if __name__ == "__main__":

    # Test de verif_balise_html avec un code HTML correctement balisé
    print(
        verif_balise_html(
            "<html><head><title>Titre</title></head><body><h1>Titre</h1><p>Paragraphe<br>Paragraphe</p></body></html>"
        )
    )

    # Test de verif_balise_html avec un code HTML mal balisé
    print(
        verif_balise_html(
            "<html><head><title>Titre</title></head><body>Titre</h1><p>Paragraphe</body></html>"
        )
    )

    # Test de verif_balise_html avec un code HTML mal balisé (balise fermante manquante)
    print(
        verif_balise_html(
            "<html><head><title>Titre</title</head><body><h1>Titre</h1><p>Paragraphe<br>Paragraphe</p></body></html>"
        )
    )

    # Test de verif_balise_html avec un code HTML mal balisé (balise ouvrante manquante)
    print(
        verif_balise_html(
            "html><head><title>Titre</title></head><body><h1>Titre</h1><p>Paragraphe<br>Paragraphe</p></body></html>"
        )
    )

    # Test de verif_balise_html avec une page HTML
    with open("ex7_b_site.html", "r") as page:
        html = page.read()  # On lit le code HTML de la page HTML dans une variable
    # On vérifie si le code HTML est correctement balisé
    print(verif_balise_html(html))

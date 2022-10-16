"""
La récurssivité - Exercice 7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Comptage d'un caractère dans une chaîne.
"""

__author__ = "RobiPoire"


def compteur(chaine: str, caractere: str) -> int:
    """Retourne le nombre de fois que l'on peut compter le caractère caractere dans la chaine chaine

    Args:
        chaine (str): La chaine
        caractere (str): Le caractère

    Returns:
        int: Le nombre de fois que l'on peut compter le caractère caractere dans la chaine chaine
    """
    if len(chaine) == 0:
        return 0
    if chaine[0] == caractere:
        return 1 + compteur(chaine[1:], caractere)
    return compteur(chaine[1:], caractere)


# Exemples d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté
    print(compteur("abracadabra", "a"))
    print(compteur("bonjour", "b"))

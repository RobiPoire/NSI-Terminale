"""
La récurssivité - Exercice 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Nombre d'adhérents d'une association.
"""

__author__ = "RobiPoire"


def nombre(n: int) -> int:
    """Retourne le nombre théorique d'adhérents n années après 2019

    Args:
        n (int): Le nombre d'années

    Returns:
        int: Le nombre théorique d'adhérents n années après 2019
    """
    if n == 0:
        return 2000
    return nombre(n-1) * 0.95 + 200


def adherants_theorique(annees: int) -> None:
    """Affiche le nombre théorique d'adhérents au cours des années

    Args:
        annees (int): Le nombre d'années
    """
    for annee in range(annees):
        print(f"Année {annee+1}: {round(nombre(annee))}")


# Exemples d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté
    adherants_theorique(20)

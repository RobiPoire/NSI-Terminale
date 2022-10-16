"""
La récurssivité - Exercice 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Calcul du PGCD, le plus grand diviseur commun.
"""

__author__ = "RobiPoire"


def pgcd(a: int, b: int) -> int:
    """Retourne le plus grand diviseur commun de a et b

    Args:
        a (int): Le premier nombre
        b (int): Le deuxième nombre

    Returns:
        int: Le plus grand diviseur commun de a et b
    """
    if b == 0:
        return a
    return pgcd(b, a % b)


# Exemples d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté
    print(pgcd(20, 24))
    print(pgcd(24, 20))
    print(pgcd(24, 0))
    print(pgcd(0, 24))
    print(pgcd(0, 0))
    print(pgcd(24, 24))
    print(pgcd(24, 25))
    print(pgcd(25, 24))
    print(pgcd(25, 25))

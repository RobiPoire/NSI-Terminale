"""
La récurssivité - Exercice 5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Exercice sur la division euclidienne.
"""

__author__ = "HabibLebsir, devnatiofrance, RobiPoire"


def division(dividende: int, diviseur: int, quotient: int = 0) -> tuple:
    """ Fonction qui calcule le quotient et le reste de la division euclidienne

    Args:
        dividende (int): Le dividende
        diviseur (int): Le diviseur
        quotient (int, optional): Le quotient. 0 par défaut.

    Returns:
        tuple: Le quotient et le reste de la division euclidienne
    """
    if dividende < diviseur:
        return quotient, dividende
    return division(dividende - diviseur, diviseur, quotient + 1)


# Exemples d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté
    print(division(10, 3))
    print(division(20, 2))

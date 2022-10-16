"""
La récurssivité - Exercice 8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Etude de la fonction binomial récursive.
"""

__author__ = "RobiPoire"


# 1)
def binomial(n: int, k: int) -> int:
    """Retourne le coefficient binomial de n et k

    Args:
        n (int): Le nombre de lignes
        k (int): Le nombre de colonnes

    Returns:
        int: Le coefficient binomial de n et k
    """
    if k == 0 or k == n:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)


# 2) 155117520, Je pense que c'est très inefficace car il y a beaucoup de calculs inutiles


# 3)
def binomial_memo(n: int, k: int, memo: dict = {}) -> int:
    """Retourne le coefficient binomial de n et k

    Args:
        n (int): Le nombre de lignes
        k (int): Le nombre de colonnes
        memo (dict, optional): Le dictionnaire de memoisation. {} par défaut.

    Returns:
        int: Le coefficient binomial de n et k
    """
    if k == 0 or k == n:
        return 1
    if (n, k) in memo:
        return memo[(n, k)]
    memo[(n, k)] = binomial_memo(n - 1, k - 1, memo) + \
        binomial_memo(n - 1, k, memo)
    return memo[(n, k)]


# Exemples d'utilisation
if __name__ == "__main__":  # Se lance uniquement si le fichier est exécuté
    print(binomial(30, 15))
    print(binomial_memo(30, 15))

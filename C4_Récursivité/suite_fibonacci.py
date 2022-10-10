"""
Recursivité - La suite de Fibonacci 
~~~~~~~~~~~~~~~~~~~~~~~
Implémentation de la suite de Fibonacci avec et sans mémorisation
"""

__author__ = "HabibLebsir, RobiPoire"

import sys
sys.setrecursionlimit(1000000000)  # Augmentation de la limite de récursivité


def fibo(n: int) -> int:
    """Calcul de la suite de Fibonacci

    Args:
        n (int): le nombre de la suite de Fibonacci

    Returns:
        int: le nombre de la suite de Fibonacci
    """
    if n > 1:
        return fibo(n - 1) + fibo(n - 2)
    return n


def fibo_memo(n: int, memo: dict = {}) -> int:
    """Calcul de la suite de Fibonacci avec mémorisation

    Args:
        n (int): le nombre de la suite de Fibonacci
        memo (dict): le dictionnaire de mémorisation

    Returns:
        int: le nombre de la suite de Fibonacci
    """
    if n in memo:
        return memo[n]
    elif n > 1:
        memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
        return memo[n]
    else:
        return n


# Exemples d'utilisation
if __name__ == "__main__":
    print(fibo(30))
    print(fibo_memo(30))

"""
Recursivité - La suite de Fibonacci 
~~~~~~~~~~~~~~~~~~~~~~~
Implémentation de la suite de Fibonacci avec et sans mémorisation
"""

__author__ = "HabibLebsir, RobiPoire"

import sys
from time import perf_counter
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


def fibo_itteration(n: int) -> int:
    """Calcul de la suite de Fibonacci avec itération

    Args:
        n (int): le nombre de la suite de Fibonacci

    Returns:
        int: le nombre de la suite de Fibonacci
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


# Exemples d'utilisation
if __name__ == "__main__":
    debut = perf_counter()
    print(fibo(35))
    fin = perf_counter()
    print(f"Temps d'exécution: {fin - debut} secondes de fibo")
    debut = perf_counter()  
    print(fibo_memo(35))
    fin = perf_counter()
    print(f"Temps d'exécution: {fin - debut} secondes de fibo_memo")
    debut = perf_counter()
    print(fibo_itteration(35))
    fin = perf_counter()
    print(f"Temps d'exécution: {round(fin - debut)} secondes de fibo_itteration")

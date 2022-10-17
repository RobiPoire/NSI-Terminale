"""
Recursivité - La suite de Fibonacci 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implémentation de la suite de Fibonacci avec 3 méthodes différentes:
"""

__author__ = "RobiPoire"

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


def fibo_memo(n: int) -> int:
    """Calcul de la suite de Fibonacci avec mémorisation

    Args:
        n (int): le nombre de la suite de Fibonacci

    Returns:
        int: le nombre de la suite de Fibonacci
    """
    memo = {0: 0, 1: 1}

    def fibo(n) -> int:
        if n not in memo:
            memo[n] = fibo(n - 1) + fibo(n - 2)
        return memo[n]

    return fibo(n)


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
    nombre_de_fibonacci = 39
    debut = perf_counter()
    print(fibo(nombre_de_fibonacci))
    fin = perf_counter()
    print(f"Temps d'exécution: {fin - debut} secondes de fibo")
    debut = perf_counter()
    print(fibo_memo(nombre_de_fibonacci))
    fin = perf_counter()
    print(f"Temps d'exécution: {fin - debut} secondes de fibo_memo")
    debut = perf_counter()
    print(fibo_itteration(nombre_de_fibonacci))
    fin = perf_counter()
    print(
        f"Temps d'exécution: {round(fin - debut)} secondes de fibo_itteration")

# TODO: #5 Faire les courbes de temps d'exécution

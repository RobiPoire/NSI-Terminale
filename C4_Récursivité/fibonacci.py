import sys
sys.setrecursionlimit(1000000000)

def fibo(number: int) -> int:
    """
    Il renvoie le résultat de la suite de Fibonacci
    
    Args:
      number (int):  Le nombre de la suite
    
    Returns:
      Le résultat de la suite
    """
    if number > 1:
        return fibo(number - 1) + fibo(number - 2)
    return number
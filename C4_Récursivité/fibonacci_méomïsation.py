import sys
sys.setrecursionlimit(1000000000)

def fibo_memo(number: int, memo: dict) -> int:
    if number in memo:
        return memo[number]
    elif number > 1:
        memo[number] = fibo_memo(number - 1, memo) + fibo_memo(number - 2, memo)
        return memo[number]
    else:
        return number

print(fibo_memo(1000, {}))
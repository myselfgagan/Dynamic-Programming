def fib(n, memo = {}):          # added memo to store the values to reuse them
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(5))
print(fib(100))
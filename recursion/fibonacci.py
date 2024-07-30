def fibonacci(n):
    assert n>= 0  and int(n) == n, "It should be an integer!"   # unconditional case
    if n in [0,1]:                          # base case
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)     #recursive case
print(fibonacci(5))
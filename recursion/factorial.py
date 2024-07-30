def factorial(n):
    assert n>=0 and int(n) == n , 'The Number Must be positive integer Only!'
    if n in [0,1]:              # the base case
        return 1
    else:
        return n*factorial(n-1)   #recursive case
print(factorial(3))
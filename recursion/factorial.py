def factorial(n):
    if n in [0,1]:              # the base case
        return 1
    else:
        return n*factorial(n-1)   #recursive case
print(factorial(3))
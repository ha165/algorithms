# How to convert a number from decimal tp binary
def decimalbinary(n):
    if n == 0:            #base case
        return 0
    else:
        return n%2 + 10 * decimalbinary(int(n/2))     #recursive case

print(decimalbinary(10))
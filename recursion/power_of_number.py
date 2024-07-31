#How to calculate power of a number using recursion
def power(base,exp):
    return base * power(base,exp-1)   #recursive case

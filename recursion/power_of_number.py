#How to calculate power of a number using recursion
def power(base,exp):
    #unconditional case
    assert exp>=0 and int(exp) == exp, "The exponent must be positive integer Only!"
    #base case
    if exp == 0:
        return 1
    if exp == 1:
        return base;
    
    #recursive case
    return base * power(base,exp-1)   
print(power(2,4))
#How to calculate power of a number using recursion
def power(base,exp):
    
    #base case
    if exp == 0:
        return 1
    if exp == 1:
        return base;
    
    #recursive case
    return base * power(base,exp-1)   
print(power(2,4))
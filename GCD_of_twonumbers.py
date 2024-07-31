# How to find GCD(greatest common divisor) of two numbers using recursion?
def gcd(a,b):
    #unintentional case
    
    #base case
    if b == 0:
        return a
    else:
        # recursive case 
        return gcd(b,a%b)
print(gcd(48,18))
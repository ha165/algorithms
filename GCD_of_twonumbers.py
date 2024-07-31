# How to find GCD(greatest common divisor) of two numbers using recursion?
def gcd(a,b):
    #unintentional case
    assert int(a) == a and int(b) == b,'The number must be Integer'
    if a<0:
        a = -1 * a
    if b<0:
        b = -1 * b
    #base case
    if b == 0:
        return a
    else:
        # recursive case 
        return gcd(b,a%b)
print(gcd(48,18))
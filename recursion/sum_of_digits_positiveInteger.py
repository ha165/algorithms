# How to find the sum of digits of positive integer number using recursion
def sumofDigits(n):
    assert n>0 and int(n) == 0, 'The number must be an a positive inteer!'    #unconditional case
    if n == 0:                                           # CASE BASE
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))        # RECURSIVE CASE
print(sumofDigits(15))
# How to find the sum of digits of positive integer number using recursion
def sumofDigits(n):
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))
print(sumofDigits(15))
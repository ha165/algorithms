# Implement a recursive function to check if a string is a palindrome.

def is_palindrome(string):
    # base case
    if len(string) <= 1 :
        return True
    # check if the first and last characters are same
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])     #recursiv case
print(is_palindrome('racecar'))
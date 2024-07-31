def reverse_string(s):
    # Base case: if the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    
    # Recursive case: concatenate the last character with the reversed substring
    return s[-1] + reverse_string(s[:-1])
import re

# Approach 2
def valid_palindrome(s: str) -> bool:
    # Remove all special characters, punctuation, and spaces
    modified_string = re.sub(r'[^\w]', '', s)

    # Convert the whole string to lowercase
    modified_string = modified_string.lower()

    # Initialize palindrome to True
    palindrome = True

    # Length of the modified string
    n = len(modified_string)

    # Check if the string is a palindrome
    for i in range(n // 2):
        if modified_string[i] != modified_string[n - i - 1]:
            palindrome = False
            break

    return palindrome

# Approach 2
# Optimized code for checking if a string is a valid palindrome
def valid_palindrome_optimized(s: str) -> bool:
    # Remove all special characters, punctuation, and spaces
    modified_string = re.sub(r'[^\w]', '', s)

    # Convert the whole string to lowercase
    modified_string = modified_string.lower()

    # Check if the string is a palindrome
    return modified_string == modified_string[::-1]

s = "race a car"
results = valid_palindrome_optimized(s)
print(results)

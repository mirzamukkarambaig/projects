import re

# Approach 1
def valid_palindrome(s: str) -> bool:
    # Remove all special characters, punctuation, and spaces, and underscores
    s = re.sub(r'[^a-zA-Z0-9]', '', s)

    # Convert the whole string to lowercase
    s = s.lower()

    # Length of the modified string
    n = len(s)

    # Check if the string is a palindrome
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False

    return True

# Approach 2
# Optimized code for checking if a string is a valid palindrome
def valid_palindrome_optimized(s: str) -> bool:
    # Remove all special characters, punctuation, and spaces, and underscores
    s = re.sub(r'[^a-zA-Z0-9]', '', s)

    # Convert the whole string to lowercase
    s = s.lower()

    # Check if the string is a palindrome
    return s == s[::-1]

s = "ab_a"
results = valid_palindrome_optimized(s)
print(results)

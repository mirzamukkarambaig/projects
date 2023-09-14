class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all special characters, punctuation, and spaces, and underscores
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        # Convert the whole string to lowercase
        s = s.lower()

        # Check if the string is a palindrome
        return s == s[::-1]
        
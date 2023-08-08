
class Solution:
    def isPalindrome_str(self, x: int) -> bool:
        """
        Check if an integer is a palindrome using string conversion.
        
        A palindrome is a number that reads the same backward as forward.
        
        Args:
        - x (int): The integer to check.
        
        Returns:
        - bool: True if x is a palindrome, False otherwise.
        """
        return str(x) == str(x)[::-1]

    def isPalindrome_int(self, x: int) -> bool:
        """
        Check if an integer is a palindrome using integer operations.
        
        A palindrome is a number that reads the same backward as forward.
        
        Args:
        - x (int): The integer to check.
        
        Returns:
        - bool: True if x is a palindrome, False otherwise.
        """
        # A negative number cannot be a palindrome
        if x < 0:
            return False
        
        # Store the original number for later comparison
        original_x = x
        reversed_x = 0
        
        # Reverse the integer
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10
        
        # Check if the reversed integer is the same as the original
        return original_x == reversed_x

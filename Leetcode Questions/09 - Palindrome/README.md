# Palindrome Checker

This code provides two methods to check if a given integer is a palindrome. A palindrome is a number that reads the same backward as forward.

## Methods

### isPalindrome_str

This method checks if an integer is a palindrome by converting the number to a string and comparing it to its reverse.

```python
def isPalindrome_str(self, x: int) -> bool:
```

### isPalindrome_int

This method checks if an integer is a palindrome using integer operations, without converting the number to a string.

```python
def isPalindrome_int(self, x: int) -> bool:
```

## Usage

You can use the `Solution` class to check if a given integer is a palindrome using either of the methods:

```python
solution = Solution()
result_str = solution.isPalindrome_str(121) # Returns True
result_int = solution.isPalindrome_int(121) # Returns True
```

## Requirements

- Python 3.x

## License

Feel free to use, modify, and distribute this code as you see fit.

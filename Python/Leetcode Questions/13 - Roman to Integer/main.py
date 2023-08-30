class Solution:
    def romanToInt(self, s: str) -> int:
        decoder = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        prev_value = 0  # Initialize a variable to keep track of the previous value
        for i in range(len(s) - 1, -1, -1):
            value = decoder.get(s[i])
            # If the current value is smaller than the previous value, subtract it; otherwise, add it.
            if value < prev_value:
                sum -= value
            else:
                sum += value
            prev_value = value  # Update the previous value for the next iteration
        return sum

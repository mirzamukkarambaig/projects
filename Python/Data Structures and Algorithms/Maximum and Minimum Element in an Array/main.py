# Approach 1
import sys

# Maximum size for integers in Python on this platform
INT_MAX = sys.maxsize

# Minimum size for integers in Python on this platform
INT_MIN = -sys.maxsize - 1

my_list = [5, 15, 50, 3, 67, 100]

minimum = INT_MAX
maximum = INT_MIN

for i in my_list:  # Loop through the actual elements in my_list, not the indices
    if minimum > i:  # Compare with i, not my_list[i]
        minimum = i
    if maximum < i:  # Compare with i, not my_list[i]
        maximum = i

print(f"Maximum: {maximum}, Minimum: {minimum}")

# Approach 2
my_list.sort()
maximum = my_list[-1]
minimum = my_list[0]

print(f"Maximum: {maximum}, Minimum: {minimum}")

# Approach 3
# Using built-in functions to find minimum and maximum
minimum = min(my_list)
maximum = max(my_list)

print(f"Maximum: {maximum}, Minimum: {minimum}")


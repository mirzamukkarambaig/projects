# Approach 1: Manual Iteration
import sys

# Define maximum and minimum integer values based on system limits
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize - 1

# Initialize the list of numbers
my_list = [5, 15, 50, 3, 67, 100]

# Initialize variables to hold the minimum and maximum values
minimum = INT_MAX
maximum = INT_MIN

# Loop through each element in the list to find the minimum and maximum
for i in my_list:
    if minimum > i:  # Update the minimum value if a smaller number is found
        minimum = i
    if maximum < i:  # Update the maximum value if a larger number is found
        maximum = i

# Display the calculated maximum and minimum values
print(f"Maximum: {maximum}, Minimum: {minimum}")

# Approach 2: Using Sorting
# Sort the list in ascending order
my_list.sort()

# The last element is the maximum and the first element is the minimum
maximum = my_list[-1]
minimum = my_list[0]

# Display the calculated maximum and minimum values
print(f"Maximum: {maximum}, Minimum: {minimum}")

# Approach 3: Using Built-in Functions
# Use Python's built-in min() and max() functions to find the minimum and maximum
minimum = min(my_list)
maximum = max(my_list)

# Display the calculated maximum and minimum values
print(f"Maximum: {maximum}, Minimum: {minimum}")

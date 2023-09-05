# List of integers containing both positive and negative numbers
my_list = [2, 1, -3, 4, -1, 2, 1, -5, 4]

# Approach 1: Using if-statements for comparison
# Initialize maximum_sum to store the maximum subarray sum
# Initialize current_sum to store the sum of the current subarray
maximum_sum = float('-inf')
current_sum = 0

# Loop through each element in the list
for i in my_list:
    # Add the current element to current_sum
    current_sum += i
    
    # Update maximum_sum if the current_sum is greater
    if current_sum > maximum_sum:
        maximum_sum = current_sum
    
    # Reset current_sum if it becomes negative
    if current_sum < 0:
        current_sum = 0

# Print the maximum subarray sum calculated using Approach 1
print(maximum_sum)

# Approach 2: Using Python's max() function for comparison
# Initialize max_sum to store the maximum subarray sum
# Initialize current_sum to store the sum of the current subarray
max_sum = float('-inf')
current_sum = 0

# Loop through each element in the list
for num in my_list:
    # Add the current element to current_sum
    current_sum += num
    
    # Update max_sum to be the maximum of max_sum and current_sum
    max_sum = max(max_sum, current_sum)
    
    # Reset current_sum to zero if it becomes negative
    current_sum = max(0, current_sum)

# Print the maximum subarray sum calculated using Approach 2
print(max_sum)

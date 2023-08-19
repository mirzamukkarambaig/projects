# Two Sum Problem Solver
This repository contains a Python implementation of the Two Sum problem. The function twoSum in the Solution class finds two numbers in an array that add up to a given target.

# Problem Description
Given an array of integers (nums) and an integer (target), the function twoSum returns the indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice. The function can return the answer in any order.

# Usage
```python
# Create an instance of the Solution class
solver = Solution()

# Define the array of integers and the target
nums = [2, 7, 11, 15]
target = 9

# Call the twoSum function
result = solver.twoSum(nums, target)

# Output should be: [0, 1]
print(result)
```

# Methodology
The function uses a dictionary (hash table) to store numbers and their indices from the array. It calculates the complement of each number (i.e., target - num) and checks if the complement is already in the dictionary. If it is, the function returns the indices of the complement and the current number. If the complement is not in the dictionary, the function adds the current number and its index to the dictionary.

# Time and Space Complexity
The time complexity of the function is O(n), where n is the length of the input array, because it makes a single pass through the array.
The space complexity is also O(n), because in the worst-case scenario, it may store every number from the array in the dictionary.

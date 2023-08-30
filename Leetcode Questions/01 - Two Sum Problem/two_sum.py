class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, returns the indices of the 
        two numbers such that they add up to target.

        Args:
        nums (List[int]): The list of integers.
        target (int): The target integer.

        Returns:
        List[int]: The indices of the two numbers from nums that add up to target. 
        """

        # Initialize an empty dictionary to store the numbers and their indices
        number_dict = {}

        # Iterate over the list of numbers along with their indices
        for i, num in enumerate(nums):
            # Compute the complement of the current number with respect to the target
            complement = target - num

            # If the complement is in the dictionary, we found the pair of numbers that add up to target
            if complement in number_dict:
                # Return the indices of the complement and the current number
                return [number_dict[complement], i]

            # If the complement is not in the dictionary, add the current number and its index to the dictionary
            number_dict[num] = i

        # If no pair of numbers adds up to the target, return None. 
        # Although the problem guarantees a solution exists, this line is for completeness.
        return None

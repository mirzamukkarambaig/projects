class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_dict = {}
        for i, num in enumerate(nums):
            if num in number_dict:
                return True
            else:
                number_dict[num] = i
        return False


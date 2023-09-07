class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_dict = {}
        for i, num in enumerate(nums):
            if num in number_dict:
                return True
            else:
                number_dict[num] = i
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False

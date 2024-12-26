class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums) - 1

        for i in range(len(nums)):
            if nums[i] == val:
                while k >= i and nums[k] == val:
                    k -= 1 
                if k >= i:
                    nums[i] = nums[k]
                    k -= 1

        return k + 1
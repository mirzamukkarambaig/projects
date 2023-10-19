class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = sorted(nums1 + nums2)
        print(sorted_array)
    
        length = len(sorted_array)
    
        half = length // 2
    
        if (length % 2 == 0):
            print((sorted_array[half - 1] + sorted_array[half]) / 2)
            return (sorted_array[half - 1] + sorted_array[half]) / 2
        else:
            print(sorted_array[half])
            return sorted_array[half]
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqs = defaultdict(int)
        
        # Increment the count for each character in s
        for char in s:
            freqs[char] += 1
        
        # Decrement the count for each character in t
        for char in t:
            freqs[char] -= 1

        # Check if all counts are zero
        return all(count == 0 for count in freqs.values())

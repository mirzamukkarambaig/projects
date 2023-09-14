from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:
    if(len(s) != len(t)):
        return False
    
    s_freqs, t_freqs = {}, {}
    
    for char in s:
        s_freqs[char] = s_freqs.get(char, 0) + 1
        
    for char in t:
        t_freqs[char] = t_freqs.get(char, 0) + 1

    return s_freqs == t_freqs

def check_anagram_sorting(s, t):
    return sorted(s) == sorted(t)

def isAnagram_optimized(self, s: str, t: str) -> bool:
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

s = "anagram"
t = "nagaram"

print(check_anagram_sorting(s, t))
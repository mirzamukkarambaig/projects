from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs or "" in strs:
        return ""
    
    # Find the shortest string in the list
    min_str = min(strs, key=len)
    
    # Initialize longest common prefix to an empty string
    lcp = ""
    
    # Loop through each character in the shortest string
    for i in range(len(min_str)):
        char = min_str[i]
        
        # Check if this character is common in all strings
        if all(s[i] == char for s in strs):
            lcp += char
        else:
            break
            
    return lcp

# Example usage
strs1 = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs1))  # Output should be "fl"

strs2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs2))  # Output should be ""

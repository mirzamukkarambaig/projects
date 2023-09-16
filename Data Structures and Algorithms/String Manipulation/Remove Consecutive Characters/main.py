def remove(s: str) -> str:
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            # Takes the first appearance of repeating character i 
            # connects it with the rest of the string 
            # reinitializes the string s
            s = s[:i] + s[i + 1:] 
        else:
            i += 1  

    return s

def remove_optimized(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            i += 1  # Skip the next character
        else:
            result.append(s[i])  # Add the current character to the result
        i += 1  
    return ''.join(result)  # Convert the list back to a string

print(remove("aabbcc"))  
print(remove_optimized("aaabbbccc"))  

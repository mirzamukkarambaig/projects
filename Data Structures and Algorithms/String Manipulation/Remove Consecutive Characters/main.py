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

print(remove("aabbcc"))  
print(remove("aaabbbccc"))  

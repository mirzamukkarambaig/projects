def valid_parentheses(s: str) -> bool:
    if len(s) % 2 != 0: # Parentheses must be in pairs thus the lenght must be even
        return False
    
    stack = []
    mappings = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mappings.values():  
            stack.append(char)
        elif char in mappings.keys():  
            if (not stack) or (mappings[char] != stack.pop()):
                return False
        else:
            return False  
            
    return not stack  

s = "(){}"

print(valid_parentheses(s))

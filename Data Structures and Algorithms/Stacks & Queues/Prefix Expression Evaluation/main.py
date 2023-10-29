def prefix_evaluation(string: str) -> int:
    stack = []

    # Reverse the string and iterate over it
    for char in reversed(string):
        if '0' <= char <= '9':
            stack.append(int(char))
        else:
            # Ensuring there are enough operands in the stack
            if len(stack) < 2:
                raise ValueError("Invalid prefix expression")

            operand1 = stack.pop()
            operand2 = stack.pop()

            mapping = {
                "+": lambda: operand1 + operand2,
                "-": lambda: operand1 - operand2,
                "*": lambda: operand1 * operand2,
                "/": lambda: operand1 / operand2,
                "^": lambda: operand1 ** operand2  
            }
            
            if char in mapping:
                stack.append(mapping[char]())  
            else:
                raise ValueError(f"Unknown operator: {char}")

    # If the evaluation is correct, only one value should remain
    if len(stack) != 1:
        raise ValueError("Invalid prefix expression")
    
    return stack.pop()

print(prefix_evaluation("+-32*45"))

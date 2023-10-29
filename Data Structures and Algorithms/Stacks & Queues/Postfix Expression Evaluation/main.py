def evaluate_operator(operator, operand1, operand2):
    mapping = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else float('inf'),  # Handling division by zero
        "^": lambda x, y: x ** y
    }

    if operator not in mapping:
        raise ValueError(f"Unknown operator: {operator}")
    
    return mapping[operator](operand1, operand2)


def postfix_evaluation(expression: str) -> int:
    stack = []

    # Splitting the string by whitespace to handle multi-digit numbers and operators
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():  # Using isdigit() to check for numbers
            stack.append(int(token))
        else:
            # Ensuring there are enough operands in the stack
            if len(stack) < 2:
                raise ValueError(f"Invalid prefix expression: insufficient operands for operator {token}")

            operand2 = stack.pop()
            operand1 = stack.pop()

            result = evaluate_operator(token, operand1, operand2)
            stack.append(result)

    # If the evaluation is correct, only one value should remain
    if len(stack) != 1:
        raise ValueError("Invalid prefix expression: imbalanced operators and operands")
    
    return stack.pop()

print(postfix_evaluation("4 5 * 3 2 - +"))

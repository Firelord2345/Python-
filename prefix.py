def evaluate_prefix(expression):
    stack = []  # Move the stack inside the function
    # Split the expression by spaces and reverse the order of tokens
    tokens = expression.split()[::-1]

    for i in tokens:
        if i.isdigit():  # Check if the token is a number
            stack.append(int(i))
        elif i == "+":
            op2 = stack.pop()  # Pop the second operand
            op1 = stack.pop()  # Pop the first operand
            result = op1 + op2
            stack.append(result)
        elif i == "-":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 - op2
            stack.append(result)
        elif i == "*":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 * op2
            stack.append(result)
        elif i == "/":
            op2 = stack.pop()
            op1 = stack.pop()
            if op2 == 0:
                raise ValueError("Cannot divide by zero")
            result = op1 / op2
            stack.append(result)
    
    return stack[0]  # Return the final result after all operations

expression = "* + 2 3 4"
result = evaluate_prefix(expression)
print("Result:", result)

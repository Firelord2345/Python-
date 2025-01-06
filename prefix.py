stack = []

def evaluate_prefix(expression):
    # Split the expression by spaces
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
            result = op1 / op2
            stack.append(result)
    
    return stack[0]  # Return the final result after all operations
expression = "* + 2 3 4"
result = evaluate_prefix(expression)
print("Result:", result)
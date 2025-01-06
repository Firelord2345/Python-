stack = []

def evaluate_postfix(expression):
    # Split the expression by spaces
    tokens = expression.split()

    for i in tokens:
        if i.lstrip('-').isdigit():  # Check if the token is a number also lstrip is used for handling negative numbers
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

# Example usage:
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
expression = "3 4 + 2 * 7 /"
result = evaluate_postfix(expression)
print("Result:", result)

s = "]"
dict = {"{": "}", "(": ")", "[": "]"}
stack = []

def valid_paranthesis(s):
    for i in s:
        if i in dict:  # Check if it’s an opening bracket
            stack.append(i)
        elif stack and dict[stack[-1]] == i:  # Check for matching closing bracket
            stack.pop()
        else:
            return False 
       
    return len(stack) == 0

print(valid_paranthesis(s))  

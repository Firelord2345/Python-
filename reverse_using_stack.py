stack=[]
def reverse_string(input_string):
    li=[]
    for i in input_string:
        stack.append(i)
    while stack:
        li.append(stack.pop())
    return ''.join(li)
        
        
        
    
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed String:", reversed_string)

# import re
# inp=input("Enter a text")
# def palin(inp):

#     result = re.sub(r"[^a-zA-Z]", "", inp)
#     return result==result[::-1]
# print(palin(inp))
inp = input("Enter a text")

def palin(inp):
    if not isinstance(inp, str):
        inp = ""  # Replace non-string input with an empty string

    # Check if the string is a palindrome
    return inp == inp[::-1]

print(palin(inp))


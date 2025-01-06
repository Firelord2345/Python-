import re
inp=input("Enter a text")
def palin(inp):

    result = re.sub(r"[^a-zA-Z]", "", inp)
    return result==result[::-1]
print(palin(inp))

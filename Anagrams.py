# inp1=input("String1:\t")
# inp2=input("String2:\t")
# char_dict1 = {char: inp1.count(char) for char in inp1}
# char_dict2={char: inp2.count(char) for char in inp2}

# def anagrams(inp1,inp2):
#     if len(inp1)==len(inp2):
#         for _ in inp1:
#             if char_dict1[_]!=char_dict2[_]:
#                 return False
#         return True
# print(anagrams(inp1,inp2))
inp1 = input("String1:\t")
inp2 = input("String2:\t")

def anagrams(inp1, inp2):
    if len(inp1) == len(inp2):
        # Create frequency dictionaries for both strings
        char_dict1 = {char: inp1.count(char) for char in inp1}
        char_dict2 = {char: inp2.count(char) for char in inp2}
        
        # Compare the dictionaries
        if char_dict1 == char_dict2:
            return True
    return False

print(anagrams(inp1, inp2))

ini = "swiss"
def first_non_rep(ini):
    dic = {char: ini.count(char) for char in ini}
    for char in ini:
        if dic[char] == 1:
            return char
    return None  # In case there is no non-repeating character

print(first_non_rep(ini))

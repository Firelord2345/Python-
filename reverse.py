# st = "Hi My Name is Andrei"
# st1 = st.split(" ")

# # Reverse the entire list of words
# st1 = st1[::-1]

# # Reverse the characters in each word
# for i in range(len(st1)):
#     st1[i] = st1[i][::-1]

# print(st1)
st = "Hi My Name is Andrei"
st1 = st.split(" ")

# Reverse the entire list of words
for i in range(len(st1) // 2):
    st1[i], st1[len(st1) - i - 1] = st1[len(st1) - i - 1], st1[i]

# Reverse the characters in each word
for i in range(len(st1)):
    st2 = list(st1[i])  # Convert word to list of characters
    for j in range(len(st2) // 2): 
        st2[j], st2[len(st2) - j - 1] = st2[len(st2) - j - 1], st2[j]
    st1[i] = ''.join(st2)  # Convert list back to string

print(st1)


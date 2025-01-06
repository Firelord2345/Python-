array=[2,1,1,2,3,5,1,2,4]
class NoRepeatingElementError(Exception):
    pass
# array=[2,1,2,3, 4,5]
# array=[2 ,3, 4,5]
repeating={}
# def first_repeating_occurrence():
#     for i in array:
#         if i  not in repeating:
#             repeating[i]=1
#         elif i in repeating:
#             repeating[i]+=1
#             return i
#     raise NoRepeatingElementError("No repeating elements found")
def first_recurring_character(input):
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[i] == input[j]:
                return input[i]
    return None

print(first_recurring_character(array))
# print(first_repeating_occurrence())
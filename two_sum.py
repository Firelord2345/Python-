target_sum = 7
lit = [2, 3, 4, 1]
dict = {}

def two_sum(target_sum):
    for num in lit:
        complement = target_sum - num
        if complement in dict:
            return [complement, num]
        else:
            dict[num] = True

print(two_sum(target_sum))

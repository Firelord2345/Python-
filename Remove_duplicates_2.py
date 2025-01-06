
nums = [1, 1, 1, 2, 2, 3]

def removeDuplicates(nums):
    k = 0
    for i in range(len(nums)):
        if k < 2 or nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1
    return k

k = removeDuplicates(nums)
print(nums[:k])
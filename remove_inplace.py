def removeElement(nums, val) :
    i=0
    k=0
    while i<len(nums):
        if(nums[i]!=val):
            nums[k]=nums[i]
            k+=1
        i+=1
    return k

nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print(k)  # Output: 2
print(nums[:k])  # Output: [2, 2]

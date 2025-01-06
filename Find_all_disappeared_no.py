from typing import List
nums=[4,3,2,7,8,2,3,1]
def cyclic_sort(nums:List[int])->List[int]:
    li=[]
    i=0
    while i<len(nums):
        correct_index=nums[i]-1
        if nums[correct_index]!=nums[i]:
            nums[correct_index],nums[i]=nums[i],nums[correct_index]
        else:
            i+=1
    
    for i in range(len(nums)):
        if i+1!=nums[i]:
            li.append(i+1)
    return li
print(cyclic_sort(nums))
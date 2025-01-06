nums=[3,4,-1,1]
from typing import List

def cyclic_sort(nums:List[int])->List[int]:
    
    i=0
    while i<len(nums):
        correct_index=nums[i]-1
        if correct_index<len(nums) and correct_index>=0 and nums[correct_index]!=nums[i]:
            nums[correct_index],nums[i]=nums[i],nums[correct_index]
        else:
            i+=1
    
    for i in range(len(nums)):
        if i+1!=nums[i]:
            return i+1
    return len(nums)+1
    
print(cyclic_sort(nums))
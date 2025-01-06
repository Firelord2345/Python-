from typing import List
nums=[1,3,4,2,2]
def cyclic_sort(nums:List[int])->List[int]:
    i=0
    while i<len(nums):
        correct_index=nums[i]-1
        if nums[correct_index]!=nums[i]:
            nums[correct_index],nums[i]=nums[i],nums[correct_index]
        else:
            i+=1
    
    return correct_index+1
print(cyclic_sort(nums))
        
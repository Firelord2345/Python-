INTEGER_MAX=-1000

nums=[4,5,1,2,3]
def selection_sort(nums):
    
    for j in range(len(nums)-1):  
        end=len(nums)-j
        start=0
        z=max_value(nums,start,end)
        temp=nums[z]
        nums[z]=nums[len(nums)-1-j]
        nums[len(nums)-1-j]=temp
        
    return nums
def max_value(nums,start,end):
    max=start
    for i in range(end):
        if nums[max]<nums[i]:
            max=i
    return max
        
        
        
        
print(selection_sort(nums))
             
    
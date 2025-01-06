nums=[3,1,5,4,2]
def bubble_sort(nums):
    temp=0
    
    for i in range(len(nums)-1):
        boolean=False
        for j in range(1,len(nums)-i):
              
              if nums[j-1]>nums[j]:
                  temp=nums[j-1]
                  nums[j-1]=nums[j]
                  nums[j]=temp
                  boolean=True
              
        if boolean==False:
                  break
        
                  
    return nums
print(bubble_sort(nums))                
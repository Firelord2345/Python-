def Peak(nums):
    start=0
    end=len(nums)-1
    while start<end:
        mid = start + (end - start) // 2

        if nums[mid]>nums[mid+1]:
            end=mid
        else:
             start=mid+1
        
    return start
nums = [1,2,3,1]
print(Peak(nums))
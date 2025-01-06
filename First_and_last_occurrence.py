def searchRange( nums, target: int) :
    first_occur=binary_search(nums,target,False)  
    last_occur=binary_search(nums,target,True)  
    return [first_occur,last_occur]
def binary_search(nums,target,Last):
    start=0
    end=len(nums)-1
    while start<=end:
        mid = start + (end - start) // 2

        if nums[mid]==target:
            result=mid
            if Last:
                start=mid+1
            else:
                end=mid-1
        elif nums[mid]>target:
             end=mid-1
        else:
            start=mid+1
    return result
nums = [5,7,7,8,8,10]
print(searchRange(nums,7))
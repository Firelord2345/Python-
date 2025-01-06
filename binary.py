def binary_search(nums,target):
    start=0
    end=len(nums)-1
    while start<=end:
        mid = start + (end - start) // 2

        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
             end=mid-1
        else:
            start=mid+1
    return -1
nums=[2,3,5,9,14,16,18]
print(binary_search(nums,5))
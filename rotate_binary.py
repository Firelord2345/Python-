def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the target
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Search in the left half
            else:
                left = mid + 1  # Search in the right half
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
                
    return -1  # Target not found
nums = [4,5,6,7,0,1,2]
print(search(nums,-1))
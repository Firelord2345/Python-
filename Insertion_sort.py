from typing import List

nums = [5, 3, 4, 1, 2]

def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                # Swap using Python's tuple unpacking
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
    return nums

print(insertion_sort(nums))


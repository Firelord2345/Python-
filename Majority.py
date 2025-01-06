nums = [2, 2, 1, 1, 1, 2, 2]

# Boyer-Moore Voting Algorithm
def majority(nums):
    candidate = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = nums[i]
                count = 1
    return candidate

k = majority(nums)

# Verify if the candidate is indeed the majority element
def majority_num(k, nums):
    count = sum(1 for num in nums if num == k)  # Count occurrences of k
    if count > len(nums) // 2:
        return k
    else:
        return None  # No majority element exists

result = majority_num(k, nums)
print(result)

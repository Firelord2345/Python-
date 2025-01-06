# y=[-2,1,-3,4,-1,2,1,-5,4]
y = [1, 2, 3, 7, 5]

li=[]
def kadanes():
     current_sum=0
     max_so_far=0
     for i in y:
          
          current_sum=max(i,current_sum+i)
          max_so_far=max(current_sum,max_so_far)

     return max_so_far
# This handles subarray sum for negative numbers
# def subarray_with_given_sum(arr, target_sum):
#     prefix_sum = 0
#     prefix_map = {}  # To store prefix sum and its index

#     for end in range(len(arr)):
#         prefix_sum += arr[end]  # Update the prefix sum
        
#         # If prefix sum matches the target, subarray starts from index 0
#         if prefix_sum == target_sum:
#             return arr[0:end+1]
        
#         # Check if (current_sum - target_sum) is in the map
#         if (prefix_sum - target_sum) in prefix_map:
#             start = prefix_map[prefix_sum - target_sum] + 1
#             return arr[start:end+1]
        
#         # Store the current prefix sum with its index
#         prefix_map[prefix_sum] = end
    
#     return "No subarray found"

def subarray_with_given_sum(arr, target_sum):
    start = 0
    current_sum = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        # Shrink the window as long as the current sum is greater than the target
        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1

        # Check if the current sum matches the target
        if current_sum == target_sum:
            return arr[start:end+1]

    return []  # Return an empty list if no subarray with the target sum is found


target_sum = kadanes()
print(target_sum)
print(subarray_with_given_sum(y, target_sum))


y=[-2,1,-3,4,-1,2,1,-5,4]
li=[]
def kadanes():
     current_sum=0
     max_so_far=0
     for i in y:
          
          current_sum=max(i,current_sum+i)
          max_so_far=max(current_sum,max_so_far)

     return max_so_far
def subarray_with_given_sum(arr, target_sum):
    prefix_sum = 0
    prefix_map = {}  # To store prefix sum and its index

    for end in range(len(arr)):
        prefix_sum += arr[end]  # Update the prefix sum
        
        # If prefix sum matches the target, subarray starts from index 0
        if prefix_sum == target_sum:
            return arr[0:end+1]
        
        # Check if (current_sum - target_sum) is in the map
        if (prefix_sum - target_sum) in prefix_map:
            start = prefix_map[prefix_sum - target_sum] + 1
            return arr[start:end+1]
        
        # Store the current prefix sum with its index
        prefix_map[prefix_sum] = end
    
    return "No subarray found"


target_sum = kadanes()
print(subarray_with_given_sum(y, target_sum))


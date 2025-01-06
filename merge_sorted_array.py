def merge_sorted(arr1, arr2):
    li = []
    i = j = 0
    
    # Compare elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            li.append(arr1[i])
            i += 1
        else:
            li.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1 or arr2
    li.extend(arr1[i:])
    li.extend(arr2[j:])
    
    return li

# Test the function
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted(arr1, arr2))

    
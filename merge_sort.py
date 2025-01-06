def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    i=j=0
    merge=[]
    while i<len(left) and j<len(right):
         if left[i]<right[j]:
             merge.append(left[i])
             i+=1
         else:
             merge.append(right[j])
             j+=1
         
    merge.extend(left[i:])
    merge.extend(right[j:])
    return merge
    
        
             
    
arr = [38, 27, 43, 3, 9, 82, 10]
arr=merge_sort(arr)
print("Sorted array:", arr)
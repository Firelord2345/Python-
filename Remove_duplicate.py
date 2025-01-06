nums = [1, 1, 2]
def removeDuplicates(nums) :
  i=0
  k=1
  for i in range(len(nums)-1):
       if nums[i]!=nums[i+1]:
           nums[k]=nums[i+1]
           k+=1
           
  return k
k=removeDuplicates(nums)

print(nums[:k])
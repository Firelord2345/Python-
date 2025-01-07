# s = "a good   example"

# def reverseWords(s: str) -> str:
#     s = s.split(" ")[::-1]  # Split the string into words and reverse the list
#     li=[]
#     for i in s:
#         if i !='':
#             li.append(i)
#     return ' '.join(li).strip(" ")      # Join the reversed list with spaces

# print(reverseWords(s))  # Correctly call the function with the argument `s`
from typing import List
nums =[2,3,1,1,4]
def jump(self, nums: List[int]) -> int:
        farthest = 0  # variable to keep track of the farthest index we can reach
        count=0
        for i in range(len(nums)):
           
            
            # Update the farthest position we can reach from index i
            farthest = max(farthest, i + nums[i])
            
            # If farthest position can reach or surpass the last index, return True
            if farthest >= len(nums) - 1:
                count+=1
                break
        
        return count
print(jump(nums))

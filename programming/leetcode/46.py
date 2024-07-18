class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
        def perm(i):
            if i == len(nums):
                yield nums[:]
                
            for j in range(i, len(nums)):
                swap(i, j)
                yield from perm(i+1)
                swap(i, j)
                
        return list(perm(0))
            
           
         
        
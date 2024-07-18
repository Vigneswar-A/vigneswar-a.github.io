class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        
        res = 0
        minprefix = []
        maxprefix = []
        minval = inf
        maxval = -inf
        
        for i in range(len(nums)):
            
            minval = min(minval, nums[-i-1])
            maxval = max(maxval, nums[i])
            
            minprefix.append(minval)
            maxprefix.append(maxval)
            
        minprefix.reverse()
        res = 0
        for i in range(len(nums)):
            if minprefix[i] == maxprefix[i]:
                res += 1
            
       
       
        return res
      
            
            
             
            

        
        
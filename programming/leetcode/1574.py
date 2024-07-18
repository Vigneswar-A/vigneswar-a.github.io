class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        fmax = smax = 0
        
        for i in nums:
            if i >= fmax:
                smax = fmax
                fmax = i
            elif i > smax:
                smax = i
                
        return (fmax-1)*(smax-1)
            
        
        
        
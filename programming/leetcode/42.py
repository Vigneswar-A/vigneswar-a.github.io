class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = list(accumulate(height, max))
        suffix = list(accumulate(height[::-1], max))[::-1]
        res = 0
        for i in range(len(height)):
            res += min(prefix[i], suffix[i])-height[i]
            
        return res
        
        
        
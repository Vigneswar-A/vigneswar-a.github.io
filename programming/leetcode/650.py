class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(prev=float('inf'), count=1):
            
            if count == n:
                return 0
            
            if count > n:
                return float('inf')
            
            return min(1+dp(prev, count+prev), 2+dp(count, 2*count))
        
        return dp()
                
                
        
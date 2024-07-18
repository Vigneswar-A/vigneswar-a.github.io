class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        @cache
        def dp(fence=0, prev=0):
            if fence == n:
                return 1
            res = 0
            if prev == 2:
                return (k-1) * dp(fence+1, 1)
            return (k-1) * dp(fence+1, 1) + dp(fence+1, prev+1)
        
        return dp()
                    
                    
                    
        
        
        
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        
        @cache
        def dp(i, k):
            if i == endPos and k == 0:
                return 1
            elif k == 0:
                return 0
            
            return (dp(i+1, k-1)+dp(i-1, k-1))%(10**9+7)
        
        return dp(startPos, k)
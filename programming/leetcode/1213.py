class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        
        
        
        @cache
        def dp(n):
            if n == 0:
                return 1
            if n == 2:
                return 1
            if n == 1:
                return 0
            
            ans = 0
            for k in range(1, n):
                
                ans += dp(k-1)*dp(n-k-1)
            return ans
        
        return dp(numPeople)%(10**9 + 7)
                    
        
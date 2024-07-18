class Solution:
    def countArrangement(self, n: int) -> int:
        
        @cache
        def dp(idx=1, bitmask=0):
            if idx == n+1:
                return 1
            res = 0
            for i in range(1, n+1):
                if bitmask&(1<<i) == 0 and (i%idx == 0 or idx%i == 0):
                    res += dp(idx+1, bitmask|(1<<i))
            
            return res
                   
        return dp()
                    
                
        
class Solution:
    def numOfWays(self, n: int) -> int:
        
        @cache
        def dp(i=0, c1=-1, c2=-1, c3=-1):
            if i == n:
                return 1
            res = 0
            for x in range(3):
                for y in range(3):
                    for z in range(3):
                        if c1 != x and c2 != y and c3 != z and x != y and y != z:
                            
                            res += dp(i+1, x, y, z)
            return res%(1000000007)
        
        return dp()
                
        
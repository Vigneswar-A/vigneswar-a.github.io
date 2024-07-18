class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        
        @cache
        def dp(rem=n, prev=-1, count=0):
            if rem == 0:
                return 1
            res = 0
            for i in range(6):
                if prev == i:
                    if count < rollMax[i]:
                        res += dp(rem-1, prev, count+1)
                else:
                    res += dp(rem-1, i, 1)       
            return res
        
        return dp()%1000000007
        
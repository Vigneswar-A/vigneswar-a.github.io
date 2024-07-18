class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
        n = len(prices)
        @cache
        def dp(i=0):
            if i >= n:
                return 0
            
            res = inf
            for j in range(i, 2*i+2):
                res = min(res, prices[i]+dp(j+1))
                
            return res
        
        return dp()
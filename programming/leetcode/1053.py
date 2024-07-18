class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        
        n = len(prices)
        
        @cache
        def dp(i=0, target=target):
            if i == n and target == 0:
                return 0
            elif i == n or target < 0:
                return inf
            
            x = float(prices[i])
            return min(dp(i+1, target-ceil(x))+ceil(x)-x, dp(i+1, target-floor(x))+x-floor(x))
        
        
        res = dp()
        return f"{res:.3f}" if res != inf else "-1"
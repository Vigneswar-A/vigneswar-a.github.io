class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        @cache
        def dp(idx=0, hold=0):
            if idx == len(prices):
                return 0
            
            if hold:
                return max(dp(idx+1, hold), dp(idx+1)+prices[idx]-fee)
                
            return max(dp(idx+1), dp(idx+1, 1)-prices[idx])
        
        return dp()
        """
    
        """
        n = len(prices)
        dp = [[0,0] for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            dp[i][1] = max(dp[i+1][1], dp[i+1][0] + prices[i] - fee)
            dp[i][0] = max(dp[i+1][0], dp[i+1][1] - prices[i])
            
        return dp[0][0]
        """
        
        hold = not_hold = 0
        
        for i in range(len(prices)-1, -1, -1):
            hold = max(hold, not_hold + prices[i] - fee)
            not_hold = max(not_hold, hold-prices[i])
            
        return not_hold
    
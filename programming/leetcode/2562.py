class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        
        dp = [0]*(high + max(one, zero) + 1)   
        for i in range(high,-1,-1):
            dp[i] = (dp[i] + (i >= low) + dp[i+one] + dp[i+zero])%1000000007
            
        return dp[0]
        
        
        
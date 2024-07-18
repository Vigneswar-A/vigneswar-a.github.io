class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp={0:0,1:1,2:1}
        
        for i in range(0,n+1):
                dp[i]=dp[i//2]+i%2*dp[i//2+1]
        
        return max(list(dp.values())[:n+1])
        
        
        
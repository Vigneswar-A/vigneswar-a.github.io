class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        
        mod = 1000000007
        
        memo = [[0]*(k+1) for _ in range(n+1)]
        
        def dp(candies=n, bags=k):
            if memo[candies][bags] != 0:
                return memo[candies][bags]
                              
            if candies == bags or bags == 1:
                return 1
            
            if candies < bags:
                return 0
            
            res = (bags*dp(candies-1, bags) + dp(candies-1, bags-1))%mod
            memo[candies][bags] = res
            return res
            
        return dp()

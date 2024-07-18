class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:

        offers.sort(key = lambda t : t[1])
        dp = [0]*(n+1)
        k = 0

        for i in range(n):
            while k < len(offers) and offers[k][1] == i:
                dp[i] = max(dp[i], dp[offers[k][0]-1]+offers[k][2], dp[i-1])
                k += 1
            dp[i] = max(dp[i], dp[i-1])

        return dp[-2]
            
        
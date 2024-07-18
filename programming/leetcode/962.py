class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        n = len(s)
        dp = [[0, 0] for _ in range(n)]


        for i in range(n):
            dp[i][0] = dp[i-1][0] + (s[i] == '1')
            dp[i][1] = min(dp[i-1][0]+(s[i] == '0'), dp[i-1][1]+(s[i] == '0'))

        return min(dp[-1])
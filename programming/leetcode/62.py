class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                dp[i][j] += (i and dp[i-1][j])+(j and dp[i][j-1])
                
        return dp[-1][-1]
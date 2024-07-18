class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        
        for i in range(m):
            for j in range(n):
                if i and j:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])
                elif i:
                    dp[i][j] = dp[i-1][j]
                elif j:
                    dp[i][j] = dp[i][j-1]
                
                dp[i][j] += grid[i][j]
                
        return dp[-2][-2]
        
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = int(obstacleGrid[0][0] == 0)
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] += dp[i-1][j] + dp[i][j-1]
                
        return dp[-2][-2]
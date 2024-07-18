class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
        m,n = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(n+1)] for _ in range(m+1)]
        dp2 = [[[0, 0] for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j] != "W":
                    dp[i][j][0] += dp[i+1][j][0]
                    dp[i][j][1] += dp[i][j+1][1]
                if grid[i][j] == "E":
                    if i and grid[i-1][j] != "W":
                        dp[i-1][j][0] += 1
                    if j and grid[i][j-1] != "W":
                        dp[i][j-1][1] += 1
                        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "W":
                    dp2[i][j][0] += dp2[i-1][j][0]
                    dp2[i][j][1] += dp2[i][j-1][1]
                if grid[i][j] == "E":
                    if i < m-1 and grid[i+1][j] != "W":
                        dp2[i+1][j][0] += 1
                    if j < n-1 and grid[i][j+1] != "W":
                        dp2[i][j+1][1] += 1


        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    ans = max(ans, sum(dp[i][j]) + sum(dp2[i][j]))
                
        return ans
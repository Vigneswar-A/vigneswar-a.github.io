class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)] # U L
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dp[i][j][0] = dp[i-1][j][0] + 1
                    dp[i][j][1] = dp[i][j-1][1] + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for dist in range(min(m-i, n-j)):
                    if dp[i][j+dist][1] > dist and dp[i+dist][j][0] > dist \
                    and dp[i+dist][j+dist][0] > dist and dp[i+dist][j+dist][1] > dist:
                        res = max(res, dist+1)

                        
        return res**2
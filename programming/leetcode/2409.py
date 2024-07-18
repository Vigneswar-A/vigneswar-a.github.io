class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        
        m,n = len(grid),len(grid[0])
        
        dp = [[1]*n for _ in range(m)]
        ans = 0
        for i,j in sorted(((i,j) for i in range(m) for j in range(n)), key=lambda t:grid[t[0]][t[1]]):
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                if 0 <= i+dx < m and 0 <= j+dy < n and grid[i+dx][j+dy] > grid[i][j]:
                    dp[i+dx][j+dy] += dp[i][j]
            ans = (ans+dp[i][j])%(1000000007)
        
        return ans
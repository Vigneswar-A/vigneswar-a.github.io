class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        
        @cache
        def dp(i, j, opens):
            if opens < 0:
                return False

            
            if i == m-1 and j == n-1:
                return opens == 0
            
            for dx,dy in [(0,1),(1,0)]:
                if 0 <= i+dx < m and 0 <= j+dy < n and dp(i+dx, j+dy, opens+(grid[i+dx][j+dy] == '(')-(grid[i+dx][j+dy] == ')')):
                    return True
                
                
        return dp(0, 0, (grid[0][0] == '(')-(grid[0][0] == ')'))
        
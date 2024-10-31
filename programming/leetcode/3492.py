class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        row_prefix = [[(0, 0)]*(len(grid[0])+1) for _ in range(len(grid)+1)]
        col_prefix = [[(0, 0)]*(len(grid[0])+1) for _ in range(len(grid)+1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x,y = row_prefix[i-1][j]
                x += grid[i][j] == 'X'
                y += grid[i][j] == 'Y'
                row_prefix[i][j] = (x,y)
                
                x,y = col_prefix[i][j-1]
                x += grid[i][j] == 'X'
                y += grid[i][j] == 'Y'
                col_prefix[i][j] = (x,y)
            
        visited = set()
        def dp(i=0, j=0, x=0, y=0):       
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            return (dp(i+1, j, x+col_prefix[i+1][j][0], y+col_prefix[i+1][j][1]) if i+1 < len(grid) else 0) + (dp(i, j+1, x+row_prefix[i][j+1][0], y+row_prefix[i][j+1][1]) if j+1 < len(grid[0]) else 0) + (x and  x == y)
        
        ans = dp(0, 0, grid[0][0] == 'X', grid[0][0] == 'Y')
        return ans

            
        
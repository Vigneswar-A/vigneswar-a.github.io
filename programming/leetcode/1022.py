class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        def get_neighbour(x,y):
            for nx,ny in ((x,y+1),(x,y-1),(x-1,y),(x+1,y)):
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    yield nx,ny

        emptys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    emptys += 1

        res = 0
        
        def backtrack(x=0, y=0, count=0):
            nonlocal res
            if (x,y) == end:
                res += (count == emptys+1)
                return
            grid[x][y] = -1
            for nx,ny in get_neighbour(x,y):
                backtrack(nx,ny,count+1)
            grid[x][y] = 0
                
        backtrack(*start)
        return res



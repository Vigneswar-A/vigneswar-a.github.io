class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        m,n = len(grid), len(grid[0])
        visited = set()
        def dfs(x, y, px, py, c):
            if (x, y) in visited:
                return True  
            visited.add((x, y))
            
            for dx,dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                if 0 <= x+dx < m and 0 <= y+dy < n and (x+dx != px or y+dy != py) and grid[x+dx][y+dy] == c:
                    if dfs(x+dx, y+dy, x, y, c):
                        return True
                    
            return False
                    
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and dfs(i, j, -1, -1, grid[i][j]):
                    return True
        
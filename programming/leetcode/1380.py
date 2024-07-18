class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        
        visited = set()
        def dfs(x, y):
            
            stack = [(x, y)]
            touches_out = False
            
            while stack:
                x, y = stack.pop()
                
                if (x,y) in visited:
                    continue
                    
                if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                    touches_out = True
                    continue
                
                if grid[x][y] == 1:
                    continue
                
                visited.add((x, y))
                
                stack.extend((x+dx,y+dy) for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)])
                
            return 0 if touches_out else 1
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i, j) not in visited:
                    ans += dfs(i, j)
                    
        return ans
                    
                
                
            
            
            
        
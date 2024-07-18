class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
       
        visited = set()
        def dfs(x, y):
            temp = len(visited)
            flag = False
            if (x,y) in visited:
                return 0
            stack = [(x,y)]
            while stack:
                x,y = stack.pop()
               
           
                   
                if (x,y) in visited:
                    continue
                
                visited.add((x,y))
                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    if not (0 <= x+dx < m and 0 <= y+dy < n):
                        flag = True
                        continue
                    if grid[x+dx][y+dy]:
                        stack.append((x+dx, y+dy))
                   
            return len(visited)-temp if not flag else 0
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += dfs(i,j)
                    
                    
        
        return res
                          
                
        
        
            
            
            
            
        
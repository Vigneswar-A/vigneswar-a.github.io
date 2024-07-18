
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        dirhash = dict(zip(directions, 'ABCD'))
        
        def dfs(x, y):
            stack = [(x, y)]
            hash = ''
            
            while stack:
                x, y = stack.pop()
                grid[x][y] = 0
                
                for dx,dy in directions:
                    if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] == 1:
                        hash += dirhash[dx,dy]
                        stack.append((x+dx, y+dy))
                    hash += 'X'
                        
            return hash
                        
        islands = set()
        m,n = len(grid),len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands.add(dfs(i, j))
                    

        return len(islands)
    

                        
                
                
                    
            
    
    
    
    
    
    
        
        
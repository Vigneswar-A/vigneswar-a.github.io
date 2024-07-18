class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m  , n = len(grid) , len(grid[0])
        directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        max_area = 0
        nei = lambda x,y : ((x+dx,y+dy) for dx,dy in directions if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy])
        
        seen = set()
        for i in range(m):
            
            for j in range(n):
                
                if grid[i][j]:
                    
                    stack = [(i,j)]
                    area = 0
                    while stack:
                        x,y = stack.pop()
                        if (x,y) in seen:
                            continue
                        area += 1
                        seen.add((x,y))
                        stack.extend(nei(x,y))
                        
                    
                    max_area = max(max_area , area)
                
        return max_area
    
            
            
            
            
        
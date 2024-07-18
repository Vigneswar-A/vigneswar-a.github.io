class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        m, n = len(grid), len(grid[0])
        
        def get_land():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i,j
                    
                
        queue = deque([get_land()])
        perimeter = 0
        visited = {queue[0]}
        
        
        while queue:
            x,y = queue.popleft()

            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                if  0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] == 1 and (x+dx, y+dy) not in visited:
                    visited.add((x+dx, y+dy))
                    queue.append((x+dx, y+dy))
                elif (x+dx, y+dy) not in visited:
                    perimeter += 1
                
                    
        [[1,1],
         [1,1]]
        
        return perimeter
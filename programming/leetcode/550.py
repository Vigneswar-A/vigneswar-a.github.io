class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        
        m, n = len(grid), len(grid[0])
        queue = deque([])
        directions = [(0,1), (-1,0), (0,-1), (1,0)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    queue.append((i,j))
                    break
            
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx,dy in directions:
                    if 0 <= dx+x < m and 0 <= dy+y < n and grid[x+dx][y+dy] != 'X':
                        queue.append((x+dx, y+dy))
                        if grid[x+dx][y+dy] == '#':
                            return depth
                        else:
                            grid[x+dx][y+dy] = 'X'  
                                   

        return -1       
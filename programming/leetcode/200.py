class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def bfs(x,y):
            if (x,y) in seen:
                return 0
            queue = deque([(x,y)])
            
            while queue:
                x,y = queue.popleft()
                if (x,y) in seen:
                    continue
                seen.add((x,y))
                for dx,dy in directions:
                    if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and grid[x+dx][y+dy] == '1':
                        queue.append((x+dx, y+dy))
            return 1
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += bfs(i, j)
                    
        return res
                
            
        
        
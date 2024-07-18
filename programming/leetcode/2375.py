class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dist = [[inf]*n for _ in range(m)]
        
        heap = [(0, 0, 0)]
        visited = set()
        
        while heap:
            c, x ,y = heappop(heap)
            if x==m-1 and y ==n-1:
                return c
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
               
                if 0 <= x+dx < m and 0 <= y+dy < n and c+grid[x+dx][y+dy] < dist[x+dx][y+dy]:
                    heappush(heap, (c+grid[x+dx][y+dy], x+dx, y+dy))
                    dist[x+dx][y+dy] = c+grid[x+dx][y+dy]
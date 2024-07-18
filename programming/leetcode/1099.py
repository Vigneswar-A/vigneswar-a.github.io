class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        
        heap = [(-grid[0][0],0,0)]
        m,n = len(grid),len(grid[0])
        visited = set()
        while heap:
            score,x,y = heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if (x,y) == (m-1,n-1):
                return -score
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                if 0 <= (x+dx) < m and 0 <= (y+dy) < n:
                    heappush(heap, (max(score, -grid[x+dx][y+dy]), x+dx, y+dy))
            
        
        
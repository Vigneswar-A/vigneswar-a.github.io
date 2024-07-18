class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i, j))
                    grid[i][j] = -1

        d = 1
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                grid[x][y] = d
                for nx,ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if (0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0):
                        queue.append((nx, ny))
                        grid[nx][ny] = -1
            d += 1

        heap = [(-grid[0][0], 0, 0)]
        while heap:
            d, x, y = heappop(heap)
            if x == y == n-1:
                return -d-1
            for nx,ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if (0 <= nx < n and 0 <= ny < n and grid[nx][ny] != -1):
                    heappush(heap, (max(-grid[nx][ny], d), nx, ny))
                    grid[nx][ny] = -1
        
        
                
                
                    
            
            
            
            
            
            
        
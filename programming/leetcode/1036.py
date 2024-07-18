class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        queue = deque([])
        m,n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    
        
        time = 0
        while queue:
            time += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for ni, nj in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni,nj))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time-1 if time else 0
                
                
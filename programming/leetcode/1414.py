class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        m,n = len(grid),len(grid[0])
        visited = set()
        
        def is_valid(x,y):
            return (0 <= x < m and 0 <= y < n)
        
        queue = deque([(0,0,k)])
        moves = 0
        visited = set()

        while queue:
            for _ in range(len(queue)):
                x,y,k = queue.popleft()
                if k < 0 or (x,y,k) in visited:
                    continue
                visited.add((x,y,k))
                if x == m-1 and y == n-1:
                    return moves
                for dx,dy in directions:
                    if is_valid(x+dx, y+dy):
                        queue.append((x+dx, y+dy, k-grid[x][y]))
            moves += 1
        return -1
    
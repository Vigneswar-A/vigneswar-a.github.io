class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        m, n = len(grid), len(grid[0])
        heap = [(m+n,1,0,0)]
        visited = set()
        while heap:
            h, d, x, y = heappop(heap)
            if x == m-1 and y == n-1:
                return d
            if ((x, y)) in visited:
                continue
            visited.add((x, y))
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx == dy == 0) or not (0 <= x+dx < m and 0 <= y+dy < n) or grid[x+dx][y+dy]:
                        continue
                    heappush(heap, (max(m-(x+dx),n-(y+dy))+d, d+1, x+dx, y+dy))
            
        return -1
                  
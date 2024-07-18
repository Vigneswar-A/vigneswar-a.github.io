class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        m,n = len(grid), len(grid[0])

        dirmap = {1:(0,1), 2:(0,-1), 3:(1,0), 4:(-1,0)}
        visited = set()

        while heap:
            cost, x, y = heapq.heappop(heap)

            if x == m-1 and y == n-1:
                return cost

            if (x,y) in visited:
                continue

            visited.add((x,y))

            for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    heapq.heappush(heap, (cost+((dx,dy)!=dirmap[grid[x][y]]), x+dx, y+dy))

        

        



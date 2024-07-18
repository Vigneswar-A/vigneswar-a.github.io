class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)
        n = len(grid)
        visited = set()

        while heap:

            cost,x,y = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if (x,y) == (n-1,n-1):
                return cost

            for dx,dy in [(1,0), (-1,0), (0,-1), (0,1)]:
                if 0 <= x+dx < n and 0 <= y+dy < n:
                    heapq.heappush(heap, (max(cost, grid[x+dx][y+dy]), x+dx, y+dy))


            
                

            
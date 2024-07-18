class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        
        m,n = len(maze),len(maze[0])
        directions = {'l' : (0, -1), 'r': (0, 1), 'u':(-1, 0), 'd':(1, 0)}
        heap = []
        
        x,y = ball
        
        for d,(dx,dy) in directions.items():
            if (0 <= x+dx < m and 0 <= y+dy < n) and maze[x+dx][y+dy] == 0:
                heapq.heappush(heap, (1, d, x+dx, y+dy))

        visited = set()
        while heap:
            paths = []
            dist,p,x,y = heapq.heappop(heap)
            if (x, y, p[-1]) in visited:
                continue
            visited.add((x, y, p[-1]))
            if [x,y] == hole:
                return p

            dx,dy = directions[p[-1]]
            if not (0 <= x+dx < m and 0 <= y+dy < n) or maze[x+dx][y+dy] == 1:
                for d,(dx,dy) in directions.items():
                    if (0 <= x+dx < m and 0 <= y+dy < n) and maze[x+dx][y+dy] == 0:
                        heapq.heappush(heap, (dist+1, p+d, x+dx, y+dy))
            else:
                heapq.heappush(heap, (dist+1, p, x+dx, y+dy))

        return "impossible"

        
                    
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        
        m,n = len(grid), len(grid[0])
        island = set()
        flag = False
        for i in range(m):
            if flag:
                break
            for j in range(n):
                if flag:
                    break
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    while stack:
                        x,y = stack.pop()
                        if (x,y) in island:
                            continue
                        island.add((x,y))
                        for dx,dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                            if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] == 1:
                                stack.append((x+dx, y+dy))
                        
                    flag = True
                    break
                            
        def bfs(x, y):
            visited = set()
            dist = -1
            queue = deque([(x, y)])
            while queue:
                dist += 1
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    if (x,y) in visited:
                        continue
                    visited.add((x,y))
                    for dx,dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                        if 0 <= x+dx < m and 0 <= y+dy < n:
                            if grid[x+dx][y+dy] == 1 and (x+dx, y+dy) not in island:
                                return dist
                            elif grid[x+dx][y+dy] == 0:
                                queue.append((x+dx, y+dy))
            
            return inf
           
        
        ans = inf
        for x,y in island:
            ans = min(ans, bfs(x,y))        
        return ans                  
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        queue = deque([entrance])
        m,n = len(maze), len(maze[0])
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        seen = set()
        dist = 0
        while queue:
            dist += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                if (x,y) in seen:
                    continue
                seen.add((x,y))
                for dx, dy in directions:
                    if 0 <= x+dx < m and 0 <= y+dy < n:
                        if maze[x+dx][y+dy] == '.':
                            queue.append((x+dx, y+dy))
                    elif dist > 1:
                        return dist - 1
        return -1
                
            
        
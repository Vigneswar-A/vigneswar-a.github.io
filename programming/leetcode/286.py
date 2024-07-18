class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    
        dist = 0
        visited = set()
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = min(rooms[r][c], dist)
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                    if 0 <= r+dr < m and 0 <= c+dc < n and rooms[r+dr][c+dc] != -1:
                        queue.append((r+dr, c+dc))
                        
            dist += 1
            
        
                
        
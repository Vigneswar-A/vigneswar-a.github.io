class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        check = lambda x,y : (0 <= x < m and 0 <= y < n)
        
        def get_neighbours(x,y,dx,dy): 
            if dx:
                if check(x+dx,y) and maze[x+dx][y] != 1:
                    return [(x+dx,y,dx,0)]
                paths = []
                if check(x,y-1) and maze[x][y-1] == 0:
                    paths.append((x,y-1,0,-1))
                if check(x,y+1) and maze[x][y+1] == 0:
                    paths.append((x,y+1,0,1))  
                return paths
            
            if dy:
                if check(x,y+dy) and maze[x][y+dy] != 1:
                    return [(x,y+dy,0,dy)]
                paths = []
                if check(x-1,y) and maze[x-1][y] == 0:
                    paths.append((x-1,y,-1,0))
                if check(x+1,y) and maze[x+1][y] == 0:
                    paths.append((x+1,y,1,0))
                return paths
            
        queue = collections.deque([])
        x,y = start
        if check(x+1,y) and maze[x+1][y] == 0:
            queue.append((x+1,y,1,0))
        if check(x-1,y) and maze[x-1][y] == 0:
            queue.append((x-1,y,-1,0))
        if check(x,y+1) and maze[x][y+1] == 0:
            queue.append((x,y+1,0,1))
        if check(x,y-1) and maze[x][y-1] == 0:
            queue.append((x,y-1,0,-1))
            
        seen = set()
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                x,y,dx,dy = queue.popleft()
                if (x,y,dx,dy) in seen:
                    continue
                seen.add((x,y,dx,dy))
                if [x,y] == destination and (not check(x+dx,y+dy) or maze[x+dx][y+dy] == 1):
                    return distance
                queue.extend(get_neighbours(x,y,dx,dy))
    
        return -1  
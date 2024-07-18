class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        m = len(maze)
        n = len(maze[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()

        def is_wall(x, y):
            return maze[x][y] == 1 if 0 <= x < m and 0 <= y < n else 1

        @cache
        def dp(x, y, dx, dy):
            if (x, y, dx, dy) in visited:
                return False
            visited.add((x, y, dx, dy))
            if [x,y] == destination and is_wall(x+dx, y+dy):
                return True            
            if is_wall(x+dx, y+dy):
                return any((not is_wall(x+dx, y+dy)) and dp(x+dx, y+dy, dx, dy) for dx,dy in directions)
            return dp(x+dx, y+dy, dx, dy)

        return any(dp(*start, dx, dy) for dx,dy in directions)
        
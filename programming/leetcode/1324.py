class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        #topright, bottomleft, topleft, bottomright

        @cache
        def backtrack(r, c, position):
            if grid[r][c] == 1 and position == 1:
                if c+1 == len(grid[0]):
                    return -1
                if grid[r][c+1] == -1:
                    return -1
                return backtrack(r, c+1, 0)

            if grid[r][c] == 1 and position == 0:
                if r+1 == len(grid):
                    return c
                return backtrack(r+1, c, 1)

            if grid[r][c] == -1 and position == 1:
                if c == 0:
                    return -1
                if grid[r][c-1] == 1:
                    return -1
                return backtrack(r, c-1, 0)

            if grid[r][c] == -1 and position == 0:
                if r+1 == len(grid):
                    return c
                return backtrack(r+1, c, 1)

        res = []
        for col in range(len(grid[0])):
            res.append(backtrack(0, col, 1 if grid[0][col] == 1 else 1))
        return res

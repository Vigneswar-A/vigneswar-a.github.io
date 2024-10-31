class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        res = 0
        n = len(grid)
        for i in range(n):
            row = 0
            col = 0
            for j in range(n):
                row = max(row, grid[i][j])
                col = max(col, grid[j][i])
                res += bool(grid[i][j])
            res += row+col
        return res
        
        
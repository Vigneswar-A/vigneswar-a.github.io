class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        @cache
        def dp(r, c):
            res = 0
            for nr,nc in ((r-1, c+1), (r, c+1), (r+1,c+1)):
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[r][c] < grid[nr][nc]:
                    res = max(res, dp(nr, nc)+1)
            return res
        
        return max(dp(i, 0) for i in range(len(grid)))
            
        
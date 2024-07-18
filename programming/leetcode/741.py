class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        @cache
        def dp(x1=0, y1=0, x2=0, y2=0):
            if x1 == y1 == x2 == y2 == n-1:
                return grid[x1][y1]
            if not (0 <= x1 < n and 0 <= x2 < n and 0 <= y1 < n and 0 <= y2 < n):
                return -float('inf')
            if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                return -float('inf')
            
            if x1 == x2 and y1 == y2:
                res = grid[x1][y1]
            else:
                res = grid[x1][y1] + grid[x2][y2]

        
            return max(dp(x1+1, y1, x2+1, y2), dp(x1+1, y1, x2, y2+1), dp(x1, y1+1, x2+1, y2), dp(x1, y1+1, x2, y2+1)) + res

        
        res = dp()
        return res if res != -float('inf') else 0
            
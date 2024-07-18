class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        @cache
        def dp(r=0, pc=-1):
            if r == n:
                return 0
            
            res = inf
            for c in range(n):
                if c == pc:
                    continue
                res = min(res, dp(r+1, c)+grid[r][c])
            return res
        
        return dp()
            
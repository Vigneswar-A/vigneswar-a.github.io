class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        directions = (-1, 0, 1)

        @cache
        def dp(x=0, y1=0, y2=n-1):    
            if not (0 <= x < m and 0 <= y1 < n and 0 <= y2 < n):
                return -float('inf')
            
            if x == m-1:
                return grid[x][y1]+grid[x][y2] if y1 != y2 else grid[x][y1]

            if y1 == y2:
                res = grid[x][y1]
            else:
                res = grid[x][y1] + grid[x][y2]

            curr = 0
            
            for dy1 in directions:
                for dy2 in directions:
                    curr = max(curr, dp(x+1, y1+dy1, y2+dy2))
                    
            return curr+res

        
        res = dp()
        return res if res != -float('inf') else 0
            
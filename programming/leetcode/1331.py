class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0
        seen = set()
        m,n = len(grid),len(grid[0])
        def backtrack(x , y , gold):
            nonlocal res
            res = max(res , gold)
            seen.add((x,y))
            for dx,dy in directions:
                if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] and (x+dx,y+dy) not in seen:
                    backtrack(x+dx , y+dy , gold+grid[x+dx][y+dy])
            seen.remove((x,y))

                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    backtrack(i, j, grid[i][j])
                
        return res
            
        
        
        
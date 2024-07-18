class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        lastrow = set(grid[-1])
        rows = {}
        for i in range(len(grid)):
            for j in grid[i]:
                rows[j] = i
                
        @cache    
        def dp(num):
            if rows[num] == len(grid)-1:
                return num
            
            res = inf
            for col in range(len(grid[0])):
                res = min(res, dp(grid[rows[num]+1][col])+moveCost[num][col]+num)
                
            return res
        
        return min(dp(i) for i in grid[0])
    
                
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        directions = [(-2 , -1) , (-2 , 1), (-1 , -2), (-1 , 2), (1 , -2), (1 , 2), (2 , -1), (2, 1)]
    
        @cache
        def travel(x=row , y=column , moves=k):         
            if moves == 0:
                return 1
            
            res = 0
            for dx,dy in directions:
                if (0 <= x+dx < n and 0 <= y+dy < n):
                    res += travel(x+dx , y+dy , moves-1)
                    
            return res
        
        return travel()/(8**k)
                
        
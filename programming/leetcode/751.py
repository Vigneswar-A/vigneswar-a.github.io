class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        counts = Counter()
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for offset in range(j+1,n):
                        if grid[i][offset] == 1:
                            res += counts[j,offset]
                            counts[j,offset] += 1
                   
        return res
                            
        
                    
                    
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m,n = len(grid),len(grid[0])
        rows = Counter()
        cols = Counter()
        
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
                
        diff = [[2*rows[i]+2*cols[j]-m-n for j in range(n)] for i in range(m)]
        
        return diff
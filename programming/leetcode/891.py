class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m): 
            score = sum((1-grid[i][k])*2**(n-k-1) for k in range(n))-sum(grid[i][k]*2**(n-k-1) for k in range(n))
            if score > 0:
                for j in range(n):
                    grid[i][j] = 1-grid[i][j]
                    
        for i in range(n): 
            score = sum((1-grid[k][i])*2**(n-i-1) for k in range(m))-sum(grid[k][i]*2**(n-i-1) for k in range(m))
            if score > 0:
                for j in range(m):
                    grid[j][i] = 1-grid[j][i]
                    
        return sum(int(''.join(map(str, row)), 2) for row in grid)
                    
        
            
            
        
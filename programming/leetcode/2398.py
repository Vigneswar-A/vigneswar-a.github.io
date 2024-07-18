class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        n = len(grid)
        
        diag = lambda i,j : i == j or i == n-j-1
        
        for i in range(n):
            for j in range(n):
                if diag(i, j) and grid[i][j] == 0 or not diag(i, j) and grid[i][j]:
                    return False
                
    
        return True
        
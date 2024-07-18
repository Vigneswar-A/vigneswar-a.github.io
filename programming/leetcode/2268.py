class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        new_grid = [[0]*n for _ in range(m)]
        row_ops = set()
        col_ops = set()

        while True:
            for i,j in product(range(m), range(n)):
                if new_grid[i][j] != grid[i][j] and i not in row_ops:
                    for k in range(n):
                        new_grid[i][k] = int(not new_grid[i][k])
                    row_ops.add(i)
                    break
                elif new_grid[i][j] != grid[i][j] and j not in col_ops:
                    for k in range(m):
                        new_grid[k][j] = int(not new_grid[k][j])
                    col_ops.add(j)
                    break
                elif new_grid[i][j] != grid[i][j]:
                    return False
            else:  
                return True
                
                
                    
            
                        
        
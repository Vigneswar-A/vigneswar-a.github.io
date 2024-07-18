class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        row, col = [0]*m,[0]*n

        arr = sorted(product(range(m),range(n)), key = lambda x : grid[x[0]][x[1]])
        
        for i,j in arr:
            grid[i][j] = row[i] = col[j] = max(row[i],col[j])+1
        
        return  grid
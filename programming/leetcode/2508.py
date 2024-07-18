class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        def getsum(tup):
            i,j = tup
            try:
                return grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
            
            except:
                return -inf
            
            
        return max(map(getsum,((i,j) for i in range(len(grid)) for j in range(len(grid[0])))))
        
            
        
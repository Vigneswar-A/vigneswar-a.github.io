class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        @cache
        def dp(i, j):
            if j < 0 or j == len(matrix[0]):
                return inf
            
            if i == len(matrix):
                return 0
            
            return min(dp(i+1, j+1), dp(i+1, j-1), dp(i+1, j))+matrix[i][j]
        
        return min(dp(0, j) for j in range(len(matrix[0])))
            
            
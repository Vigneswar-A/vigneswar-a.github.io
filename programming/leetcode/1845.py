class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for col in range(n):
            for row in range(m-2,-1,-1):
                if matrix[row][col]:
                    matrix[row][col] += matrix[row+1][col]

        res = 0
        for row in matrix:
            row.sort(reverse=1)
            for i in range(n):
                res = max(res, row[i]*(i+1))
        return res
                
                
                
                    
        
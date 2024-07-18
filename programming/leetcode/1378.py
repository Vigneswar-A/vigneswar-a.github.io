class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        matrix = [[0] * n for _ in range(m)]

        for i,j in indices:
            
            for k in range(m):
                matrix[k][j] += 1
            
            for k in range(n):
                matrix[i][k] += 1
        
        return sum(i%2 for row in matrix for i in row)
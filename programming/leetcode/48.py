class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(n := len(matrix)):
            for j in range(i , n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
            matrix[i].reverse()
        
        
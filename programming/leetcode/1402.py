class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        ans = 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] and i < m-1 and j < n-1:
                    matrix[i][j] = min(matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]) + 1
                for side in range(min(m-i, n-j)):
                    if matrix[i][j] > side:
                        ans += 1

        return ans
                    
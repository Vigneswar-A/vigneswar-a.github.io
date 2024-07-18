class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        return -((n := len(mat))%2*mat[n//2][n//2] - sum(mat[i][i] + mat[i][-i - 1] for i in range(n)))
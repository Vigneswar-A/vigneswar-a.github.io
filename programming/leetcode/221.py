class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m,n = len(matrix),len(matrix[0])

        dp = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                res = max(res, dp[i][j])

        return res**2
                    

                
        
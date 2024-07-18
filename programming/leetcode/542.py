class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        
        dp = [[inf]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
                    
                    
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j] - 1, dp[i][j+1] if j+1 < n else inf, dp[i+1][j] if i+1 < m else inf) + 1
                    
        return dp
class Solution:
    def calculateMinimumHP(self, dp: List[List[int]]) -> int:
        m, n = len(dp), len(dp[0])
        ans = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    dp[i][j] = max(-dp[i][j]+1, 1)
                elif i == m-1:
                    dp[i][j] = max(dp[i][j+1]-dp[i][j], 1)
                elif j == n-1:
                    dp[i][j] = max(dp[i+1][j]-dp[i][j], 1)
                else:
                    dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-dp[i][j], 1)
                    
        return dp[0][0]
                    
        
                
        
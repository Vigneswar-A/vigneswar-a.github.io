class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n-1,-1,-1):
            for j in range(n):
                if s[i] == s[j] and (dp[i+1][j-1] or i+1  == j):
                    dp[i][j] = True


        for i in range(1, n-1):
            for j in range(i, n-1):
                if dp[0][i-1] and dp[i][j] and dp[j+1][n-1]:
                    return True
                
        return False
                    
        
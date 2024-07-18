class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        res = 0
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] or i+1 == j
                    
                if dp[i][j] == 1:
                    res += 1
                    
        return res
        
        
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
    
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        res = 0
        
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == j:
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                res = max(res, dp[i][j])
        return res
    
        
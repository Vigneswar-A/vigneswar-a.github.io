class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        m,n = len(s1),len(s2)
        dp = [[inf]*(n+1) for _ in range(m+1)]
        min_len = inf
        min_end = -1
        dp[0][0] = 0
        for i in range(1, m+1):
            dp[i][0] = 0
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j]+1


            if dp[i][n] < min_len:
                min_len = dp[i][n]
                min_end = i
                
        return s1[min_end-min_len:min_end] if min_end != -1 else ""
                    
                    
        
        
                
            
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(n):
            dp[i][i] = 0
            
        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                dp[i][j] = dp[i+1][j-1]+(s[i] != s[j])

        @cache
        def dp2(i=0, k=k):
            if i == len(s) and k == 0:
                return 0
            elif i == len(s) or k == 0:
                return inf
            
            res = inf
            for j in range(i, n):
                res = min(res, dp[i][j]+dp2(j+1, k-1))

            return res
        
        return dp2()
                
                    
                    
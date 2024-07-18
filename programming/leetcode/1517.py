class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        n = len(s)
        dp = [0]*n + [1]
        
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if int(s[i:j+1]) <= k and s[i] != '0':
                    dp[i] = (dp[i] + dp[j+1])%1000000007
                else:
                    break
        
        return dp[0]

        
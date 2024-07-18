class Solution:
    def strangePrinter(self, s: str) -> int:
        
        
        @cache
        def dp(l, r):
            j = -1
            ans = inf
            for i in range(l, r):
                if s[i] != s[r] and j == -1:
                    j = i
                if j != -1:
                    ans = min(ans, dp(j, i)+dp(i+1, r)+1)
            return ans if j != -1 else 0
                
        
        return dp(0, len(s)-1)+1
                
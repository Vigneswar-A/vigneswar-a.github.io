class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)
        
        @cache
        def dp(i=0):
            if i == n:
                return 0
            res = inf
            for nxt in range(i, n):
                sub = s[i:nxt+1]
                if sub == sub[::-1]:
                    res = min(res, dp(nxt+1)+1)
            return res
        
        return dp() - 1
                    
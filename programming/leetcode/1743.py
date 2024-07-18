class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        @cache
        def dp(i=0, j=0, k=0):
            if i == len(s) or j == len(t):
                if k:
                    return 0
                else:
                    return -inf
            
            if s[i] == t[j]:
                return k+dp(i+1,j+1, k)
            
            if not k:
                return 1+dp(i+1, j+1, 1)

            return 0
        
        return sum(dp(i, j) for i in range(len(s)) for j in range(len(t)) if dp(i, j) != -inf)
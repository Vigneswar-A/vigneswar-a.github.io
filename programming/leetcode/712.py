class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        @cache
        def dp(i=0, j=0):
            if i == m and j == n:
                return 0
            elif i == m or j == n:
                return sum(ord(s2[k]) for k in range(j, n))+sum(ord(s1[k]) for k in range(i, m))
                
            if s1[i] == s2[j]:
                return dp(i+1, j+1)
            return min(ord(s1[i])+dp(i+1,j), ord(s2[j])+dp(i,j+1))
        return dp()
                       
                       
                    
            
        
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dp(i=0, j=0):
            if j == len(p):
                return i == len(s)
            if j+1 < len(p) and p[j+1] == '*':
                if dp(i, j+2):
                    return True
                t = i
                while t < len(s) and (s[t] == p[j] or p[j]== '.'):
                    if dp(t+1, j):
                        return True
                    t += 1
            elif i < len(s) and s[i] == p[j] or p[j] == '.':
                return dp(i+1, j+1)
                    
        return dp()
                    
                    
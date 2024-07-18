class Solution:
    def shortestPalindrome(self, s: str) -> str:
        old = len(s)
        old_s = s
        s = s + "#" + s[::-1]
        n = len(s)
        pi = [0]*n
        i = 1
        j = 0
        while i < n:
            if s[i] == s[j]:
                pi[i] = j+1
                i += 1
                j += 1
            elif j:
                j = pi[j-1]
            else:
                i += 1

        x = pi[-1]-1
        return s[x+1:old][::-1] + old_s
            
        
        
            
                
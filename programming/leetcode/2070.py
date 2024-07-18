class Solution:
    def isDecomposable(self, s: str) -> bool:
        i = 0
        flag = False
        
        while i < len(s):
            if i + 2 < len(s) and s[i] == s[i+1] == s[i+2]:
                i += 3
            elif i+1 < len(s) and s[i] == s[i+1]:
                i += 2
                flag = True
            else:
                return False
            
        return flag
                
            
        
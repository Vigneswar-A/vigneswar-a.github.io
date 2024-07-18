class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        i = len(s)-1
        j = len(t)-1
        
        while i >= 0 or j >= 0:
            
            cnt = 0
            while i >= 0:
                if s[i] == '#':
                    cnt += 1
                    i -= 1
                elif cnt:
                    i -= 1
                    cnt -= 1
                else:
                    break
    
            cnt = 0
            while j >= 0:
                if t[j] == '#':
                    cnt += 1
                    j -= 1
                elif cnt:
                    j -= 1
                    cnt -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            i -= 1
            j -= 1
            
        return i == j
                
                    
                
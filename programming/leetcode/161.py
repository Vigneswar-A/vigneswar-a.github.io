class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        #case 0 both are equal already
        if s == t:
            return False
        
        #case 1 insert
        if len(s) < len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    break
            else:
                return s + t[-1] == t
            return s[:i] + t[i] + s[i:] == t
        
        #case 2 delete
        if len(s) > len(t):
            for i in range(len(t)):
                if s[i] != t[i]:
                    break 
            else:
                return s[:-1] == t
            return s[:i] + s[i+1:] == t
        
        #case 4 replace
        for i in range(len(s)):
            if s[i] != t[i]:
                break
        return s[:i] + t[i] + s[i+1:] == t
        
            
        
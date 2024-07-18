class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        values = {c : ord(c)-ord('a')+1 for c in string.ascii_lowercase}
        
        res = ""
        while not (n == 0 and k == 0):
            for c in string.ascii_lowercase:
                if (k-values[c]) <= 26*(n-1):
                    n -= 1
                    k -= values[c]
                    res += c
                    break
                    
        return res
                    
        
            
            
            
                
        
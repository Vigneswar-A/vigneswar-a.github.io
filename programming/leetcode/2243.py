class Solution:
    def checkString(self, s: str) -> bool:
        s = s.__iter__()
        
        while next(s,"b") != "b":
            pass
                
        for c in s:
            if c == "a":
                return False
        
        return True
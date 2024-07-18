class Solution:
    def greatestLetter(self, s: str) -> str:
        
        for c in string.ascii_lowercase[::-1]:
            if c in s and c.upper() in s:
                return c.upper()
            
        return ""
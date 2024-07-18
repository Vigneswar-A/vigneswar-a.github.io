class Solution:
    def removePalindromeSub(self, s: str) -> int:        
        return int(s and s==s[::-1] or 2)
        
        
        
        
        
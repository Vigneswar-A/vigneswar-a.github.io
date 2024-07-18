class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        @cache
        def dp(i=0, j=len(s)-1, k=k):
            if k == -1:
                return False
            
            if i >= j:
                return True           
            
            if s[i] == s[j]:
                return dp(i+1, j-1, k)
            
            return dp(i+1, j, k-1) or dp(i, j-1, k-1)
        
        
        return dp()
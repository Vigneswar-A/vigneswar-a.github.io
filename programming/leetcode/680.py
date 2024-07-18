class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(l=0, r=len(s)-1, flag=True):
            while l < r:
                if s[l] != s[r]:
                    return flag and (helper(l+1, r, False) or helper(l, r-1, False))
                l += 1
                r -= 1
                
            return True
                
        return helper()
                    
                    
                
                
class Solution:
    def minInsertions(self, s: str) -> int:
        
        
        def longest_palindromic_subsequence(s):
            
            @cache
            def dp(left=0, right=len(s)-1):
                if left >= right:
                    return left == right 
                if s[left] == s[right]:
                    return dp(left+1, right-1)+2
                return max(dp(left+1, right), dp(left, right-1))
            
            return dp()
            
                
            
        return len(s) - longest_palindromic_subsequence(s)
                        
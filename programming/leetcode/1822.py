class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def dp(i=0, j=len(s)-1, prev=None):
            if i >= j:
                return 0
            if s[i] == s[j] and s[i] != prev:
                return dp(i+1, j-1, s[i]) + 2
            return max(dp(i+1, j, prev), dp(i, j-1, prev))
        
        res = dp()
        del dp
        return res

        
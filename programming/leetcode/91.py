class Solution:
    def numDecodings(self, s: str) -> int:
        
        valids = {str(i) for i in range(1, 27)}
        
        @cache
        def dp(s):
            if s == '':
                return 1
            
            res = 0
            for i in range(1, len(s)+1):
                if s[:i] in valids:
                    res += dp(s[i:])
                    
            return res
        
        
        return dp(s)
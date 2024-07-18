class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @cache
        def dp(i=0):
            if i == len(s):
                return 0
            
            res = inf
            for j in range(len(s)):
                if s[i:j+1] in dictionary:
                    res = min(res, dp(j+1))
            return min(res, dp(i+1)+1)
        
        return dp()
                    
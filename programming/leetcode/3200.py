class Solution:
    def stringCount(self, n: int) -> int:
        
        MOD = 10**9+7
        @cache
        def dp(i=0, s="leet"):
            if i == n:
                return not s
            
            return (dp(i+1, s.replace("l", "")) + dp(i+1, s.replace("e", "", 1)) + dp(i+1, s.replace("t", "")) + 23*dp(i+1, s))%MOD
        
        return dp()
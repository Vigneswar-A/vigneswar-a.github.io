class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1
        
        @cache
        def dp(A, B):
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0:
                return 1
            if B <= 0:
                return 0
            return (dp(A-100, B)+dp(A-75, B-25)+dp(A-50, B-50)+dp(A-25, B-75))/4
        
        return dp(n, n)
            
        
        
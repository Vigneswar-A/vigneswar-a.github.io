class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        
        n = len(rods)
        
        @cache
        def dp(i, D):
            if i == n:
                return 0 if D == 0 else -inf
            return max(dp(i+1, D+rods[i])+rods[i], dp(i+1, D-rods[i]), dp(i+1, D))
        
        return dp(0, 0)
        
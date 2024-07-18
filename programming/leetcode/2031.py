class Solution:
    def twoEggDrop(self, n: int) -> int:
        @cache
        def dp(egg=2, floors=n):
            if egg == 1 or floors == 0:
                return floors
            res = inf
            for i in range(1, floors+1):
                res = min(res, max(dp(egg-1, i-1), dp(egg, floors-i)))
            return res+1

        return dp()
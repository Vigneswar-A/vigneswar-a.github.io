class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        @cache
        def dp(eggs=k, floors=n):
            if eggs == 1 or floors == 0:
                return floors
            left = 1
            right = floors
            
            while right - left > 1:
                i = left+right >> 1
                t1 = dp(eggs-1, i-1)
                t2 = dp(eggs, floors-i)
                
                if t1 < t2:
                    left = i
                elif t2 < t1:
                    right = i
                else:
                    left = right = i

            return 1 + min(max(dp(eggs-1, i-1), dp(eggs, floors-i)) for i in range(left, right+1))
        return dp()
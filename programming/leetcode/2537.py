class Solution:
    def minimumTime(self, power: List[int]) -> int:
        end = 0
        for i in range(len(power)):
            end |= (1<<i)

        @cache
        def dp(gain=1,bitmask=0):
            if bitmask == end:
                return 0
            res = float('inf')
            for i in range(len(power)):
                if bitmask&(1<<i):
                    continue
                bitmask |= (1<<i)
                res = min(res, dp(gain+1, bitmask) + ceil(power[i]/gain))
                bitmask ^= (1<<i)
            return res


        return dp()


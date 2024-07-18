class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        @cache
        def dp(steps=steps, pos=0):
            if pos < 0 or pos > arrLen-1:
                return 0
            if steps == 0:
                return pos == 0
            return (dp(steps-1, pos-1) + dp(steps-1, pos+1) + dp(steps-1, pos))%1000000007

        return dp()
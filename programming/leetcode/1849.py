class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [[0,0] for _ in range(n)] # maximum negative/positive subarraysum ending with i
        res = 0

        for i in range(n):
            dp[i][0] = min(dp[i-1][0]+nums[i] , nums[i])
            dp[i][1] = max(dp[i-1][1]+nums[i], nums[i])

            res = max(res, dp[i][0], dp[i][1], key = abs)

        return abs(res)

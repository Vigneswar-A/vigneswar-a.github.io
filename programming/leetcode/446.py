class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        dp = defaultdict(Counter)
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] += dp[j][d]+1
                res += dp[j][d]

        return res
                
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[0,-inf,-inf] for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = max(dp[i-1][(0+nums[i])%3]+nums[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][(1+nums[i])%3]+nums[i], dp[i-1][1])
            dp[i][2] = max(dp[i-1][(2+nums[i])%3]+nums[i], dp[i-1][2])
        
        return dp[-1][0]

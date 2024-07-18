class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        
        
        dp = [[-inf,-inf] for _ in range(len(nums))] #(pos, neg)
        res = -inf
        
        for i in range(len(nums)):
            dp[i][0] = max(dp[i-1][1]+nums[i], nums[i])
            dp[i][1] = (max(dp[i-1][0]-nums[i], 0) if i else -inf)
            res = max(res, *dp[i])
        
        return res